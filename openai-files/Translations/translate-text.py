#!/usr/bin/env python3
"""
Indian Languages MCQ Translator with Multi-API Key Parallel Processing
Translates English MCQ questions to Indian languages using multiple OpenAI API keys in parallel
with live batch saving every 10 questions and detailed error reporting
"""

import json
import os
import sys
import time
import threading
import concurrent.futures
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

class EnhancedAPIKeyManager:
    """Enhanced API key manager with load balancing and monitoring for translation"""
    
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name
        self.api_keys = self.discover_api_keys()
        self.clients = self.initialize_clients()
        
        # Enhanced tracking
        self.usage_stats = {f"key_{i+1}": 0 for i in range(len(self.api_keys))}
        self.active_requests = {f"key_{i+1}": 0 for i in range(len(self.api_keys))}
        self.last_used = {f"key_{i+1}": 0 for i in range(len(self.api_keys))}
        self.errors = {f"key_{i+1}": 0 for i in range(len(self.api_keys))}
        
        self.lock = threading.Lock()
        
    def discover_api_keys(self) -> List[str]:
        """Discover all available OpenAI API keys from environment"""
        api_keys = []
        
        # Check for primary key
        primary_key = os.getenv('OPENAI_API_KEY')
        if primary_key:
            api_keys.append(primary_key)
        
        # Check for numbered keys
        i = 1
        while True:
            key = os.getenv(f'OPENAI_API_KEY_{i}')
            if key:
                api_keys.append(key)
                i += 1
            else:
                break
        
        if not api_keys:
            raise ValueError("No OpenAI API keys found in environment variables")
        
        return api_keys
    
    def initialize_clients(self) -> List[OpenAI]:
        """Initialize OpenAI clients for each API key"""
        clients = []
        for i, api_key in enumerate(self.api_keys):
            try:
                client = OpenAI(api_key=api_key)
                clients.append(client)
            except Exception as e:
                raise Exception(f"Failed to initialize API client {i+1}: {e}")
        return clients
    
    def get_next_client(self) -> Tuple[OpenAI, str, int]:
        """Get the next available client using intelligent load balancing"""
        with self.lock:
            # Find the key with least active requests and lowest usage
            best_key = None
            best_score = float('inf')
            
            for i, key_name in enumerate(self.usage_stats.keys()):
                # Score based on active requests (priority) and total usage
                score = (self.active_requests[key_name] * 100) + self.usage_stats[key_name]
                
                if score < best_score:
                    best_score = score
                    best_key = key_name
                    best_index = i
            
            # Update tracking
            self.usage_stats[best_key] += 1
            self.active_requests[best_key] += 1
            self.last_used[best_key] = time.time()
            
            return self.clients[best_index], best_key, best_index
    
    def release_client(self, key_name: str, success: bool = True):
        """Release a client after use"""
        with self.lock:
            if key_name in self.active_requests:
                self.active_requests[key_name] = max(0, self.active_requests[key_name] - 1)
                if not success:
                    self.errors[key_name] += 1
    
    def get_usage_summary(self) -> Dict:
        """Get comprehensive usage summary"""
        with self.lock:
            return {
                'total_keys': len(self.api_keys),
                'usage_stats': self.usage_stats.copy(),
                'active_requests': self.active_requests.copy(),
                'error_counts': self.errors.copy(),
                'total_requests': sum(self.usage_stats.values()),
                'total_errors': sum(self.errors.values())
            }
    
    def print_api_keys_discovered(self):
        """Print discovered API keys to terminal"""
        print("🔑 API KEYS DISCOVERED:")
        print("="*40)
        for i, key in enumerate(self.api_keys, 1):
            # Show only first 8 and last 4 characters for security
            masked_key = f"{key[:8]}...{key[-4:]}" if len(key) > 12 else f"{key[:4]}...{key[-2:]}"
            print(f"  {i}. OPENAI_API_KEY{'_' + str(i) if i > 1 else '':<15} : {masked_key}")
        print(f"🚀 Total API Keys: {len(self.api_keys)}")
        print(f"⚡ Max Parallel Workers: {min(len(self.api_keys) * 2, 10)}")
        print("="*40)

class ParallelIndianMCQTranslator:
    """Translate MCQ questions from English to Indian languages using multiple API keys in parallel"""
    
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.model_name = model_name
        self.setup_enhanced_api_manager()
        self.translated_questions = []
        self.total_questions = 0
        self.successful_translations = 0
        self.failed_translations = 0
        self.target_language = ""
        self.target_language_native = ""
        self.output_file_path = None
        self.batch_size = 10
        self.max_workers = min(len(self.api_manager.api_keys) * 2, 10)  # 2 workers per API key, max 10
        
        # Thread-safe data structures
        self.data_lock = threading.Lock()
    
    def setup_enhanced_api_manager(self):
        """Initialize enhanced API manager with multiple keys"""
        try:
            self.api_manager = EnhancedAPIKeyManager(self.model_name)
            print("✅ Enhanced API Manager initialized successfully")
            self.api_manager.print_api_keys_discovered()
            
        except Exception as e:
            print(f"❌ Failed to initialize API manager: {e}")
            sys.exit(1)
    
    def get_indian_language_choice(self) -> Tuple[str, str]:
        """Get Indian language choice from user"""
        print("\n🇮🇳 SELECT INDIAN LANGUAGE")
        print("="*50)
        
        # Indian languages with native scripts
        indian_languages = {
            "1": ("Hindi", "हिन्दी"),
            "2": ("Bengali", "বাংলা"),
            "3": ("Telugu", "తెలుగు"),
            "4": ("Marathi", "मराठी"),
            "5": ("Tamil", "தமிழ்"),
            "6": ("Gujarati", "ગુજરાતી"),
            "7": ("Urdu", "اردو"),
            "8": ("Kannada", "ಕನ್ನಡ"),
            "9": ("Odia", "ଓଡ଼ିଆ"),
            "10": ("Punjabi", "ਪੰਜਾਬੀ"),
            "11": ("Malayalam", "മലയാളം"),
            "12": ("Assamese", "অসমীয়া"),
            "13": ("Maithili", "मैथिली"),
            "14": ("Sanskrit", "संस्कृत"),
            "15": ("Nepali", "नेपाली"),
            "16": ("Sindhi", "سنڌي"),
            "17": ("Konkani", "कोंकणी"),
            "18": ("Dogri", "डोगरी"),
            "19": ("Kashmiri", "कॉशुर"),
            "20": ("Manipuri", "ꯃꯤꯇꯩ ꯂꯣꯟ"),
            "21": ("Bodo", "बर'"),
            "22": ("Santhali", "ᱥᱟᱱᱛᱟᱲᱤ")
        }
        
        # Display options in a nice format
        print("📚 CONSTITUTIONAL LANGUAGES:")
        for key, (english, native) in indian_languages.items():
            print(f"{key:2}. {english:<12} ({native})")
        
        while True:
            choice = input(f"\n🎯 Enter your choice (1-{len(indian_languages)}): ").strip()
            
            if choice in indian_languages:
                selected_lang = indian_languages[choice]
                print(f"✅ Selected: {selected_lang[0]} ({selected_lang[1]})")
                return selected_lang
            else:
                print(f"❌ Please enter a valid choice (1-{len(indian_languages)})")
    
    def load_mcq_file(self, file_path: str) -> Optional[Dict]:
        """Load the English MCQ JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Validate structure
            if 'timer' not in data or 'instructions' not in data or 'questions' not in data:
                print("❌ Invalid MCQ file structure. Expected: timer, instructions, questions")
                return None
            
            return data
            
        except FileNotFoundError:
            print(f"❌ File not found: {file_path}")
            return None
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON file: {file_path}")
            return None
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return None
    
    def translate_single_question(self, question_data: Dict) -> Tuple[Optional[Dict], str, str]:
        """Translate a single MCQ question to target Indian language using OpenAI API with load balancing"""
        
        system_message = f"""You are an expert translator specializing in translating UPSC Civil Services examination content from English to {self.target_language}. You maintain academic precision and use terminology appropriate for Indian government competitive examinations.

CRITICAL REQUIREMENTS:
1. Translate ALL content to {self.target_language}: question text, all 4 options, and all 4 explanations
2. Maintain the exact same JSON structure 
3. Keep the same correct answer index (0, 1, 2, or 3)
4. Use standard {self.target_language} terms for government, administrative, and constitutional concepts
5. Maintain formal academic tone suitable for UPSC examinations
6. Ensure explanations remain comprehensive and educationally valuable

INDIAN CONTEXT GUIDELINES:
- Use established {self.target_language} equivalents for Indian government terms
- For constitutional and legal terms, use standard translations used in official {self.target_language} documents
- Keep technical terms precise and academically appropriate
- Maintain the educational intent and complexity level
- Use formal register appropriate for competitive examinations in India"""

        user_prompt = f"""Translate the following UPSC MCQ question from English to {self.target_language}. This is for Indian Civil Services preparation, so use appropriate {self.target_language} terminology for Indian governance, constitution, and administrative concepts.

English MCQ Question:
{json.dumps(question_data, indent=2, ensure_ascii=False)}

Return ONLY the translated JSON with this exact structure:
{{
  "question": "{self.target_language} question text here...",
  "options": ["{self.target_language} option 1", "{self.target_language} option 2", "{self.target_language} option 3", "{self.target_language} option 4"],
  "correct": {question_data['correct']},
  "explanations": {{
    "0": "{self.target_language} explanation for option 0",
    "1": "{self.target_language} explanation for option 1", 
    "2": "{self.target_language} explanation for option 2",
    "3": "{self.target_language} explanation for option 3"
  }}
}}

Return ONLY the JSON, no other text:"""

        # Get next available client using load balancing
        client, key_name, key_index = self.api_manager.get_next_client()
        failure_reason = "Unknown error"

        try:
            response = client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_prompt}
                ],
                max_completion_tokens=2500
            )
            
            if response.choices and response.choices[0].message:
                content = response.choices[0].message.content.strip()
                
                # Clean JSON response
                if content.startswith('```json'):
                    content = content.replace('```json', '').replace('```', '').strip()
                
                # Parse JSON
                try:
                    translated_question = json.loads(content)
                except json.JSONDecodeError as e:
                    failure_reason = f"JSON Parse Error: {str(e)[:60]}..."
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name, failure_reason
                
                # Validate structure
                required_fields = ['question', 'options', 'correct', 'explanations']
                missing_fields = [field for field in required_fields if field not in translated_question]
                if missing_fields:
                    failure_reason = f"Missing fields: {', '.join(missing_fields)}"
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name, failure_reason
                
                # Validate options and explanations count
                if len(translated_question.get('options', [])) != 4:
                    failure_reason = f"Invalid options count: {len(translated_question.get('options', []))} (expected 4)"
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name, failure_reason
                
                if len(translated_question.get('explanations', {})) != 4:
                    failure_reason = f"Invalid explanations count: {len(translated_question.get('explanations', {}))} (expected 4)"
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name, failure_reason
                
                # Check if explanations have correct keys
                expected_keys = {'0', '1', '2', '3'}
                actual_keys = set(str(k) for k in translated_question.get('explanations', {}).keys())
                if expected_keys != actual_keys:
                    failure_reason = f"Invalid explanation keys: {actual_keys} (expected: {expected_keys})"
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name, failure_reason
                
                # Check for empty content
                if not translated_question.get('question', '').strip():
                    failure_reason = "Empty question text after translation"
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name, failure_reason
                
                if any(not str(opt).strip() for opt in translated_question.get('options', [])):
                    failure_reason = "One or more empty options after translation"
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name, failure_reason
                
                # Ensure correct answer index is preserved
                if translated_question.get('correct') != question_data['correct']:
                    translated_question['correct'] = question_data['correct']
                
                self.api_manager.release_client(key_name, success=True)
                return translated_question, key_name, "Success"
            else:
                failure_reason = "Empty response from API"
                self.api_manager.release_client(key_name, success=False)
                return None, key_name, failure_reason
                
        except Exception as e:
            failure_reason = f"API Error: {str(e)[:60]}..."
            self.api_manager.release_client(key_name, success=False)
            return None, key_name, failure_reason
        
        return None, key_name, failure_reason
    
    def print_failure_box(self, question_index: int, failure_reason: str, api_key: str, question_preview: str):
        """Print a nice formatted box showing why a translation failed"""
        box_width = 80
        
        print("\n" + "┌" + "─" * (box_width - 2) + "┐")
        print(f"│{'🚨 TRANSLATION FAILURE':^{box_width - 2}}│")
        print("├" + "─" * (box_width - 2) + "┤")
        print(f"│ Question #{question_index:<{box_width - 15}} │")
        print(f"│ API Key: {api_key:<{box_width - 12}} │")
        print("├" + "─" * (box_width - 2) + "┤")
        print(f"│ Reason: {failure_reason:<{box_width - 11}} │")
        print("├" + "─" * (box_width - 2) + "┤")
        print(f"│ Question: {question_preview[:box_width - 13]:<{box_width - 13}} │")
        if len(question_preview) > box_width - 13:
            print(f"│           {question_preview[box_width - 13:box_width - 13 + box_width - 13]:<{box_width - 13}} │")
        print("├" + "─" * (box_width - 2) + "┤")
        print(f"│{'⚠️  Original English question will be kept in output':^{box_width - 2}}│")
        print("└" + "─" * (box_width - 2) + "┘")
    
    def translate_single_question_with_retry(self, question_data: Dict, question_index: int) -> Tuple[Optional[Dict], str, bool]:
        """Translate a single question with retry logic and detailed error reporting"""
        max_retries = 3
        last_api_key = "unknown"
        last_failure_reason = "Unknown error"
        
        for attempt in range(max_retries):
            try:
                translated_question, api_key_used, result_status = self.translate_single_question(question_data)
                last_api_key = api_key_used
                
                if translated_question and result_status == "Success":
                    return translated_question, api_key_used, True
                else:
                    last_failure_reason = result_status
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)  # Exponential backoff
                    
            except Exception as e:
                last_failure_reason = f"Exception: {str(e)[:50]}..."
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
        
        # Show detailed failure information in a box
        question_preview = question_data.get('question', '')[:60] + "..." if len(question_data.get('question', '')) > 60 else question_data.get('question', '')
        self.print_failure_box(question_index + 1, last_failure_reason, last_api_key, question_preview)
        
        return None, last_api_key, False
    
    def save_progress_batch(self, original_data: Dict) -> bool:
        """Save current progress to file (called every 10 questions)"""
        try:
            # Create the translated MCQ structure with current progress
            translated_data = {
                "timer": original_data["timer"],
                "instructions": original_data["instructions"],  # Keep instructions in English for now
                "questions": self.translated_questions,
                "translation_info": {
                    "source_language": "English",
                    "target_language": self.target_language,
                    "target_language_native": self.target_language_native,
                    "translation_timestamp": datetime.now().isoformat(),
                    "openai_model": self.model_name,
                    "total_questions_target": self.total_questions,
                    "questions_completed": len(self.translated_questions),
                    "successful_translations": self.successful_translations,
                    "failed_translations": self.failed_translations,
                    "success_rate": f"{(self.successful_translations/len(self.translated_questions)*100):.1f}%" if len(self.translated_questions) > 0 else "0%",
                    "progress_percentage": f"{(len(self.translated_questions)/self.total_questions*100):.1f}%" if self.total_questions > 0 else "0%",
                    "last_updated": datetime.now().isoformat(),
                    "status": "IN_PROGRESS" if len(self.translated_questions) < self.total_questions else "COMPLETED"
                }
            }
            
            # Save file
            with open(self.output_file_path, 'w', encoding='utf-8') as f:
                json.dump(translated_data, f, indent=2, ensure_ascii=False)
            
            return True
            
        except Exception as e:
            print(f"⚠️  Error saving progress: {e}")
            return False
    
    def translate_questions_with_parallel_processing(self, questions: List[Dict], original_data: Dict) -> List[Dict]:
        """Translate all questions using parallel processing with multiple API keys"""
        self.total_questions = len(questions)
        
        print(f"\n🔄 Starting parallel translation of {self.total_questions} questions to {self.target_language}...")
        print(f"⚡ Using {len(self.api_manager.api_keys)} API keys with {self.max_workers} parallel workers")
        print(f"💾 Progress will be saved every {self.batch_size} questions to: {self.output_file_path}")
        print("="*90)
        print(f"{'STATUS':<12} {'PROGRESS':<12} {'%':<8} {'BATCH':<8} {'API':<8} {'QUESTION PREVIEW'}")
        print("="*90)
        
        # Create a list to track translation tasks
        translation_results = [None] * self.total_questions  # Pre-allocate results list
        completed_count = 0
        
        # Process questions in parallel using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all translation tasks
            future_to_index = {}
            for i, question_data in enumerate(questions):
                future = executor.submit(self.translate_single_question_with_retry, question_data, i)
                future_to_index[future] = i
            
            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_index):
                question_index = future_to_index[future]
                question_data = questions[question_index]
                
                try:
                    translated_question, api_key_used, success = future.result()
                    completed_count += 1
                    
                    current_batch = ((completed_count - 1) // self.batch_size) + 1
                    batch_info = f"B{current_batch:02d}"
                    
                    # Show preview of question
                    question_preview = question_data['question'][:40] + "..." if len(question_data['question']) > 40 else question_data['question']
                    
                    if success and translated_question:
                        translation_results[question_index] = translated_question
                        self.successful_translations += 1
                        status = "✅ SUCCESS   "
                        # Display progress normally
                        print(f"{status:<12} {completed_count:4d}/{self.total_questions:<4d}    {completed_count/self.total_questions*100:5.1f}%  {batch_info:<8} {api_key_used:<8} {question_preview}")
                    else:
                        # Keep original question if translation fails
                        translation_results[question_index] = question_data
                        self.failed_translations += 1
                        status = "❌ FAILED    "
                        # Display minimal progress (detailed error already shown in box)
                        print(f"{status:<12} {completed_count:4d}/{self.total_questions:<4d}    {completed_count/self.total_questions*100:5.1f}%  {batch_info:<8} {api_key_used:<8} {question_preview}")
                    
                    # Save progress every batch_size questions or at the end
                    if completed_count % self.batch_size == 0 or completed_count == self.total_questions:
                        # Filter out None values and save current progress
                        current_translations = [q for q in translation_results[:completed_count] if q is not None]
                        self.translated_questions = current_translations
                        
                        print(f"\n💾 Saving batch {current_batch}...")
                        success_save = self.save_progress_batch(original_data)
                        if success_save:
                            print(f"✅ Progress saved! {completed_count}/{self.total_questions} questions completed ({completed_count/self.total_questions*100:.1f}%)")
                            print(f"📁 File updated: {self.output_file_path}")
                        else:
                            print("⚠️  Failed to save progress")
                        print("="*90)
                    
                except Exception as e:
                    completed_count += 1
                    # Keep original question if translation fails
                    translation_results[question_index] = questions[question_index]
                    self.failed_translations += 1
                    print(f"❌ ERROR     {completed_count:4d}/{self.total_questions:<4d}    {completed_count/self.total_questions*100:5.1f}%  B{((completed_count-1)//self.batch_size)+1:02d}      ERROR    API error occurred")
        
        # Return final results (filter out any None values)
        final_results = [q for q in translation_results if q is not None]
        self.translated_questions = final_results
        return final_results
    
    def get_user_inputs(self) -> tuple:
        """Get input file, language choice, output folder, and output filename from user"""
        print("="*60)
        print("🇮🇳 Indian Languages MCQ Translator")
        print("="*60)
        
        # Get input file
        while True:
            input_file = input("📁 Enter path to English MCQ JSON file: ").strip()
            if not input_file:
                print("❌ Please enter a file path")
                continue
            if not os.path.exists(input_file):
                print(f"❌ File not found: {input_file}")
                continue
            if not input_file.lower().endswith('.json'):
                print("❌ Please provide a JSON file")
                continue
            break
        
        # Get target language
        self.target_language, self.target_language_native = self.get_indian_language_choice()
        
        # Get output folder
        while True:
            output_folder = input(f"\n💾 Enter output folder path: ").strip()
            if not output_folder:
                print("❌ Please enter an output folder path")
                continue
            
            # Create folder if it doesn't exist
            try:
                Path(output_folder).mkdir(parents=True, exist_ok=True)
                print(f"✅ Output folder ready: {output_folder}")
                break
            except Exception as e:
                print(f"❌ Cannot create folder: {e}")
                continue
        
        # Get output filename
        while True:
            output_filename = input(f"\n📝 Enter output filename (without .json): ").strip()
            if not output_filename:
                print("❌ Please enter a filename")
                continue
            
            # Add .json extension if not present
            if not output_filename.lower().endswith('.json'):
                output_filename += '.json'
            
            # Set the full output path
            self.output_file_path = Path(output_folder) / output_filename
            break
        
        return input_file, output_folder, output_filename
    
    def show_translation_summary(self):
        """Display comprehensive translation summary"""
        usage_summary = self.api_manager.get_usage_summary()
        
        print("\n" + "="*70)
        print("📊 TRANSLATION SUMMARY")
        print("="*70)
        print(f"🎯 Target Language: {self.target_language} ({self.target_language_native})")
        print(f"📚 Total Questions: {self.total_questions}")
        print(f"✅ Successful Translations: {self.successful_translations}")
        print(f"❌ Failed Translations: {self.failed_translations}")
        
        if self.total_questions > 0:
            success_rate = (self.successful_translations / self.total_questions) * 100
            print(f"📈 Success Rate: {success_rate:.1f}%")
        
        print(f"📁 Output File: {self.output_file_path}")
        
        # API Usage Summary
        print(f"\n🔑 API USAGE SUMMARY:")
        print("-" * 50)
        for key_name, requests in usage_summary['usage_stats'].items():
            errors = usage_summary['error_counts'][key_name]
            success_rate_key = ((requests - errors) / requests * 100) if requests > 0 else 0
            print(f"  {key_name}: {requests:3d} calls, {errors:2d} errors, {success_rate_key:5.1f}% success")
        
        print(f"\n📊 PARALLEL PROCESSING STATS:")
        print(f"  Total API Calls: {usage_summary['total_requests']}")
        print(f"  Total Errors: {usage_summary['total_errors']}")
        print(f"  Parallel Workers: {self.max_workers}")
        print(f"  Speed Improvement: ~{len(self.api_manager.api_keys)}x faster than single key")
        print("="*70)
    
    def run_translation(self) -> bool:
        """Main method to run the translation process"""
        
        # Get user inputs
        input_file, output_folder, output_filename = self.get_user_inputs()
        
        # Load English MCQ file
        print(f"\n🔍 Loading English MCQ file: {input_file}")
        mcq_data = self.load_mcq_file(input_file)
        
        if mcq_data is None:
            return False
        
    def run_translation(self) -> bool:
        """Main method to run the translation process"""
        
        # Get user inputs
        input_file, output_folder, output_filename = self.get_user_inputs()
        
        # Load English MCQ file
        print(f"\n🔍 Loading English MCQ file: {input_file}")
        mcq_data = self.load_mcq_file(input_file)
        
        if mcq_data is None:
            return False
        
        original_questions = mcq_data['questions']
        print(f"📚 Found {len(original_questions)} questions to translate")
        
        # Confirm translation
        confirm = input(f"\n🤔 Proceed with translating {len(original_questions)} questions to {self.target_language}? (y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ Translation cancelled")
            return False
        
        # Translate questions with parallel processing
        translated_questions = self.translate_questions_with_parallel_processing(original_questions, mcq_data)
        
        # Show summary
        self.show_translation_summary()
        
        # Final save with completion status
        print(f"\n💾 Finalizing translated MCQ file...")
        success = self.save_progress_batch(mcq_data)  # This will mark status as COMPLETED
        
        if success:
            print("="*60)
            print("✅ TRANSLATION COMPLETE!")
            print("="*60)
            print(f"📁 {self.target_language} MCQ file saved: {self.output_file_path}")
            print(f"⏱️  Timer: {mcq_data['timer']} seconds")
            print(f"📝 Questions: {len(translated_questions)}")
            print(f"🇮🇳 Language: {self.target_language} ({self.target_language_native})")
            print(f"📈 Success Rate: {(self.successful_translations/self.total_questions*100):.1f}%")
            print("="*60)
            print(f"🎯 Your {self.target_language} UPSC test file is ready!")
            return True
        else:
            print("❌ Failed to finalize translated file")
            return False

def main():
    """Main entry point"""
    load_dotenv()
    
    try:
        translator = ParallelIndianMCQTranslator()
        success = translator.run_translation()
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n🛑 Translation interrupted by user")
        print("💾 Progress has been saved automatically in batches")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()