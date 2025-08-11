#!/usr/bin/env python3
"""
Indian Languages MCQ Translator
Translates English MCQ questions to Indian languages using OpenAI API
with live batch saving every 10 questions for real-time review
"""

import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

class IndianLanguagesMCQTranslator:
    """Translate MCQ questions from English to Indian languages using OpenAI API"""
    
    def __init__(self, model_name: str = "gpt-5-mini"):
        self.model_name = model_name
        self.setup_openai_client()
        self.translated_questions = []
        self.total_questions = 0
        self.successful_translations = 0
        self.failed_translations = 0
        self.target_language = ""
        self.target_language_native = ""
        self.output_file_path = None
        self.batch_size = 10
    
    def setup_openai_client(self):
        """Initialize OpenAI client"""
        try:
            api_key = os.getenv('OPENAI_API_KEY')
            if not api_key:
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            
            self.client = OpenAI(api_key=api_key)
            print("✅ OpenAI client initialized successfully")
            
        except Exception as e:
            print(f"❌ Failed to initialize OpenAI client: {e}")
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
    
    def translate_single_question(self, question_data: Dict) -> Optional[Dict]:
        """Translate a single MCQ question to target Indian language using OpenAI API"""
        
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

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_prompt}
                ],
                # temperature=0.2,  # Removed - gpt-5-mini only supports default (1)
                max_completion_tokens=2500
            )
            
            if response.choices and response.choices[0].message:
                content = response.choices[0].message.content.strip()
                
                # Clean JSON response
                if content.startswith('```json'):
                    content = content.replace('```json', '').replace('```', '').strip()
                
                # Parse JSON
                translated_question = json.loads(content)
                
                # Validate structure
                required_fields = ['question', 'options', 'correct', 'explanations']
                if not all(field in translated_question for field in required_fields):
                    print(f"⚠️  Invalid translation structure for question")
                    return None
                
                # Validate options and explanations count
                if (len(translated_question['options']) != 4 or 
                    len(translated_question['explanations']) != 4):
                    print(f"⚠️  Invalid options/explanations count")
                    return None
                
                # Ensure correct answer index is preserved
                if translated_question['correct'] != question_data['correct']:
                    print(f"⚠️  Correct answer index changed during translation")
                    translated_question['correct'] = question_data['correct']
                
                return translated_question
                
        except json.JSONDecodeError as e:
            print(f"⚠️  JSON parsing error: {e}")
            return None
        except Exception as e:
            print(f"⚠️  Translation API error: {e}")
            return None
        
        return None
    
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
    
    def translate_questions_with_live_save(self, questions: List[Dict], original_data: Dict) -> List[Dict]:
        """Translate all questions with live batch saving every 10 questions"""
        self.total_questions = len(questions)
        
        print(f"\n🔄 Starting translation of {self.total_questions} questions to {self.target_language}...")
        print(f"💾 Progress will be saved every {self.batch_size} questions to: {self.output_file_path}")
        print("="*80)
        print(f"{'STATUS':<12} {'PROGRESS':<12} {'%':<8} {'BATCH':<8} {'QUESTION PREVIEW'}")
        print("="*80)
        
        for i, question_data in enumerate(questions, 1):
            # Show preview of question being translated
            question_preview = question_data['question'][:45] + "..." if len(question_data['question']) > 45 else question_data['question']
            
            current_batch = ((i - 1) // self.batch_size) + 1
            batch_info = f"B{current_batch:02d}"
            
            print(f"{'TRANSLATING':<12} {i:3d}/{self.total_questions:<3d}      {i/self.total_questions*100:5.1f}%  {batch_info:<8} {question_preview}")
            
            # Attempt translation with retries
            max_retries = 3
            translated_question = None
            
            for attempt in range(max_retries):
                translated_question = self.translate_single_question(question_data)
                if translated_question:
                    break
                elif attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
            
            if translated_question:
                self.translated_questions.append(translated_question)
                self.successful_translations += 1
                status = "✅ SUCCESS   "
            else:
                # Keep original question if translation fails
                self.translated_questions.append(question_data)
                self.failed_translations += 1
                status = "❌ FAILED    "
            
            # Update progress line
            print(f"\r{status:<12} {i:3d}/{self.total_questions:<3d}      {i/self.total_questions*100:5.1f}%  {batch_info:<8} {question_preview}")
            
            # Save progress every 10 questions or at the end
            if i % self.batch_size == 0 or i == self.total_questions:
                print(f"\n💾 Saving batch {current_batch}...")
                success = self.save_progress_batch(original_data)
                if success:
                    completed_questions = len(self.translated_questions)
                    print(f"✅ Progress saved! {completed_questions}/{self.total_questions} questions completed ({completed_questions/self.total_questions*100:.1f}%)")
                    print(f"📁 File updated: {self.output_file_path}")
                else:
                    print("⚠️  Failed to save progress")
                print("="*80)
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
        
        return self.translated_questions
    
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
        """Display translation summary"""
        print("\n" + "="*60)
        print("📊 TRANSLATION SUMMARY")
        print("="*60)
        print(f"🎯 Target Language: {self.target_language} ({self.target_language_native})")
        print(f"📚 Total Questions: {self.total_questions}")
        print(f"✅ Successful Translations: {self.successful_translations}")
        print(f"❌ Failed Translations: {self.failed_translations}")
        
        if self.total_questions > 0:
            success_rate = (self.successful_translations / self.total_questions) * 100
            print(f"📈 Success Rate: {success_rate:.1f}%")
        
        print(f"📁 Output File: {self.output_file_path}")
        print("="*60)
    
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
        
        # Translate questions with live saving
        translated_questions = self.translate_questions_with_live_save(original_questions, mcq_data)
        
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
        translator = IndianLanguagesMCQTranslator()
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