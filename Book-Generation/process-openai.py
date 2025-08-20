# -*- coding: utf-8 -*-
"""
Simple Content Generation System - Single API Key Version
Processes JSON files with one API key sequentially.
Enhanced with detailed error reporting and diagnostics.
"""
import json
import os
import argparse
import time
import random
import gc
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import sys
import traceback
import re
import sqlite3

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# === Simple Console Output Functions ===
def print_header(text: str, char: str = "=", width: int = 70):
    """Print a header with decorative characters"""
    print("\n" + char * width)
    print(f" {text} ")
    print(char * width)

def print_section(text: str, char: str = "-", width: int = 50):
    """Print a section header"""
    print(f"\n{char * width}")
    print(f"{text}")
    print(char * width)

def print_success(text: str):
    """Print success message"""
    print(f"✓ {text}")

def print_error(text: str):
    """Print error message"""
    print(f"✗ {text}")

def print_warning(text: str):
    """Print warning message"""
    print(f"⚠ {text}")

def print_info(text: str):
    """Print info message"""
    print(f"ℹ {text}")

def print_progress(current: int, total: int, item: str = "items"):
    """Print progress information"""
    percentage = (current / total * 100) if total > 0 else 0
    print(f"Progress: {current}/{total} ({percentage:.1f}%) {item}")

# === Simple Database Logger ===
class SimpleLogger:
    """Basic SQLite logging for tracking progress"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.connection = self._init_database()
    
    def _init_database(self) -> sqlite3.Connection:
        """Initialize the SQLite database"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Simple files table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Files (
                file_id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT UNIQUE NOT NULL,
                filename TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                total_sections INTEGER,
                processed_sections INTEGER DEFAULT 0,
                failed_sections INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            )
        ''')
        
        # Simple sections table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sections (
                section_id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                section_number TEXT NOT NULL,
                section_name TEXT,
                stage TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                started_at TIMESTAMP,
                completed_at TIMESTAMP,
                error_message TEXT,
                FOREIGN KEY (file_id) REFERENCES Files (file_id),
                UNIQUE (file_id, section_number, stage)
            )
        ''')
        
        conn.commit()
        return conn
    
    def register_file(self, file_path: str, filename: str, total_sections: int) -> int:
        """Register a new file"""
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO Files (file_path, filename, total_sections)
            VALUES (?, ?, ?)
        """, (file_path, filename, total_sections))
        
        cursor.execute("SELECT file_id FROM Files WHERE file_path = ?", (file_path,))
        file_id = cursor.fetchone()['file_id']
        self.connection.commit()
        return file_id
    
    def log_section_start(self, file_id: int, section_number: str, section_name: str, stage: str):
        """Log section processing start"""
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO Sections 
            (file_id, section_number, section_name, stage, status, started_at)
            VALUES (?, ?, ?, ?, 'processing', ?)
        """, (file_id, section_number, section_name, stage, datetime.now()))
        self.connection.commit()
    
    def log_section_success(self, file_id: int, section_number: str, stage: str):
        """Log successful section completion"""
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE Sections 
            SET status = 'completed', completed_at = ?
            WHERE file_id = ? AND section_number = ? AND stage = ?
        """, (datetime.now(), file_id, section_number, stage))
        self.connection.commit()
    
    def log_section_failure(self, file_id: int, section_number: str, stage: str, error: str):
        """Log section failure"""
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE Sections 
            SET status = 'failed', completed_at = ?, error_message = ?
            WHERE file_id = ? AND section_number = ? AND stage = ?
        """, (datetime.now(), error, file_id, section_number, stage))
        self.connection.commit()
    
    def update_file_progress(self, file_id: int, processed: int, failed: int):
        """Update file processing progress"""
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE Files 
            SET processed_sections = ?, failed_sections = ?
            WHERE file_id = ?
        """, (processed, failed, file_id))
        self.connection.commit()
    
    def complete_file(self, file_id: int, status: str):
        """Mark file as completed"""
        cursor = self.connection.cursor()
        cursor.execute("""
            UPDATE Files 
            SET status = ?, completed_at = ?
            WHERE file_id = ?
        """, (status, datetime.now(), file_id))
        self.connection.commit()
    
    def should_process_file(self, file_path: str) -> bool:
        """Check if file should be processed"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT status FROM Files WHERE file_path = ?", (file_path,))
        result = cursor.fetchone()
        return not result or result['status'] != 'completed'
    
    def get_completed_sections(self, file_id: int, stage: str) -> set:
        """Get completed sections for a file and stage"""
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT section_number FROM Sections 
            WHERE file_id = ? AND stage = ? AND status = 'completed'
        """, (file_id, stage))
        return {row['section_number'] for row in cursor.fetchall()}
    
    def close(self):
        """Close database connection"""
        self.connection.close()

# === Simple Content Processor ===
class SimpleContentProcessor:
    """Simple content processor with single API key"""
    
    def __init__(self, model_name: str = "gpt-5-mini", logger: SimpleLogger = None):
        self.model_name = model_name
        self.logger = logger
        
        # Initialize single API key
        self.api_key = self._get_api_key()
        self.client = self._initialize_client()
        
        # Statistics
        self.stats = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'total_processing_time': 0
        }
        
        print_success(f"Initialized Simple Content Processor with model: {model_name}")
    
    def _get_api_key(self) -> str:
        """Get single API key from environment"""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable not found")
        return api_key
    
    def _initialize_client(self) -> OpenAI:
        """Initialize OpenAI client"""
        if not OpenAI:
            raise Exception("OpenAI library not available")
        
        try:
            client = OpenAI(api_key=self.api_key)
            return client
        except Exception as e:
            raise Exception(f"Failed to initialize OpenAI client: {e}")
    
    def _generate_outline_prompt(self, paper_title: str, chapter_name: str, 
                                section_name: str, section_content: str) -> str:
        """Generate prompt for outline creation"""
        return f"""
# Expert Persona

Your are an expert on newswriter, writing opinion column in indian express. You task is to Create a detailed bullet point summary of the following content. THe content is from the book why bharat matter by s jaishankar.


REQUIREMENTS:
- Cover ALL key details, break down text in bullet.
- Write quality bullet, long structure with every detail captured.
- Each bullet point should be comprehensive and standalone
- Preserve specific numbers, percentages, monetary values, and dates exactly
- Include all mentioned organizations, people, and place names
- Don't omit any substantial information from the original text
- Use clear, academic language suitable for study materials
- Format as bullet points starting with '•'
- Ensure bullet points flow logically and cover the entire content scope

Document Subject: {paper_title}
Current Chapter: {chapter_name}
Section Being Analyzed: {section_name}

# Content for Deep Strategic Analysis

--- START OF TEXT TO ANALYZE ---
{section_content}
--- END OF TEXT TO ANALYZE ---

# Your Expert Analysis Task

Breakdown the text, tell me what it is talking, the idea behind the text, what is being talked and what is being sayed. 

```json
{{
    "section_analysis": {{
       
    }},
    
}}
```
"""
    
    def _generate_content_prompt(self, paper_title: str, chapter_name: str, 
                                section_name: str, outline_json: Dict) -> str:
        """Generate prompt for content creation"""
        outline_str = json.dumps(outline_json, indent=2, ensure_ascii=False)
        
        return f"""
# Expert Author Persona
Your are an expert on newswriter, writing opinion column in indian express. So you job is write the outline as proper article.

# Your Expert Analysis (Outline) to Transform into Content
{outline_str}

# What you need to do:

Take the given outline and carefully expand it into a detailed, well-structured Markdown section written as part of an academic book on India's Strategic Culture and National Security Policy. Ensure that every topic, idea, and point mentioned in the outline is covered with depth and clarity, written in a style suitable for a serious academic book on Indian diplomacy. Focus on quality over length: expand meaningfully where needed, provide context and explanations for better understanding, but avoid unnecessary verbosity. Structure the section with a few clear headings (not too many) to guide the flow, and do not add introduction or conclusion paragraphs—write it as though it is directly part of a book chapter.
"""
    
    def _call_openai_api(self, prompt: str, response_type: str = "json", 
                        retries: int = 3, temperature: float = 0.5) -> Tuple[bool, Any, float]:
        """Make API call to OpenAI with retries"""
        start_time = time.time()
        last_error = None
        
        for attempt in range(retries + 1):
            try:
                self.stats['total_requests'] += 1
                
                system_content = "You are an expert analyst. Always respond with valid JSON." if response_type == "json" else "You are an expert writer and analyst."
                
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_content},
                        {"role": "user", "content": prompt}
                    ]
                )
                
                response_time = time.time() - start_time
                self.stats['total_processing_time'] += response_time
                
                if response.choices[0].message.content:
                    content = response.choices[0].message.content.strip()
                    
                    if response_type == "json":
                        # Clean and parse JSON
                        content = re.sub(r'^```(?:json)?\s*\n?', '', content, flags=re.MULTILINE)
                        content = re.sub(r'\n?```\s*$', '', content, flags=re.MULTILINE)
                        content = content.strip()
                        
                        start_brace = content.find('{')
                        end_brace = content.rfind('}')
                        if start_brace != -1 and end_brace != -1:
                            content = content[start_brace:end_brace + 1]
                        
                        try:
                            parsed_json = json.loads(content)
                            self.stats['successful_requests'] += 1
                            return True, parsed_json, response_time
                        except json.JSONDecodeError as json_err:
                            last_error = f"JSON Parse Error: {json_err}"
                            if attempt == retries:
                                self.stats['failed_requests'] += 1
                                print_error(f"JSON Parse Failed: {last_error}")
                                return False, last_error, response_time
                    else:
                        self.stats['successful_requests'] += 1
                        return True, content, response_time
                else:
                    last_error = "Empty response from OpenAI API"
                    if attempt == retries:
                        self.stats['failed_requests'] += 1
                        print_error(f"Empty Response: {last_error}")
                        return False, last_error, response_time
                
            except Exception as e:
                last_error = f"API Error: {type(e).__name__}: {str(e)}"
                if "rate_limit" in str(e).lower():
                    print_warning(f"Rate Limit Hit (attempt {attempt + 1}): {e}")
                    if attempt < retries:
                        time.sleep(random.uniform(5, 10))
                        continue
                elif "invalid" in str(e).lower() and "model" in str(e).lower():
                    self.stats['failed_requests'] += 1
                    print_error(f"Invalid Model Error: {e}")
                    print_error(f"Model used: {self.model_name}")
                    print_info("Check OpenAI documentation for current valid models")
                    return False, last_error, time.time() - start_time
                elif "authentication" in str(e).lower() or "api_key" in str(e).lower():
                    self.stats['failed_requests'] += 1
                    print_error(f"Authentication Error: {e}")
                    print_info("Tip: Check your OPENAI_API_KEY environment variable")
                    return False, last_error, time.time() - start_time
                else:
                    print_error(f"API Error (attempt {attempt + 1}): {e}")
                
                if attempt == retries:
                    self.stats['failed_requests'] += 1
                    print_error(f"Final API Error: {last_error}")
                    return False, last_error, time.time() - start_time
            
            if attempt < retries:
                wait_time = random.uniform(1, 3) * (attempt + 1)
                time.sleep(wait_time)
        
        self.stats['failed_requests'] += 1
        return False, last_error or "Unknown error after all retries", time.time() - start_time
    
    def process_section_outline(self, file_id: int, section: Dict, chapter_name: str) -> bool:
        """Process outline for a single section"""
        section_number = section.get('section_number')
        section_name = section.get('section_name', '')
        content = section.get('generated_section_content_md', '')
        
        if self.logger:
            self.logger.log_section_start(file_id, section_number, section_name, 'outline')
        
        print_info(f"Processing outline for section {section_number}: {section_name}")
        
        try:
            prompt = self._generate_outline_prompt(chapter_name, chapter_name, section_name, content)
            success, result, response_time = self._call_openai_api(prompt, "json", retries=3, temperature=0.5)
            
            if success:
                section['section_outline_response'] = result
                if self.logger:
                    self.logger.log_section_success(file_id, section_number, 'outline')
                print_success(f"Outline completed for section {section_number}")
                return True
            else:
                if self.logger:
                    self.logger.log_section_failure(file_id, section_number, 'outline', str(result))
                print_error(f"Outline failed for section {section_number}: {result}")
                return False
                
        except Exception as e:
            error_msg = f"Exception in outline processing: {e}"
            if self.logger:
                self.logger.log_section_failure(file_id, section_number, 'outline', error_msg)
            print_error(f"Outline exception for section {section_number}: {error_msg}")
            return False
    
    def process_section_content(self, file_id: int, section: Dict, chapter_name: str) -> bool:
        """Process content for a single section"""
        section_number = section.get('section_number')
        section_name = section.get('section_name', '')
        outline = section.get('section_outline_response')
        
        if not outline or (isinstance(outline, dict) and outline.get('error')):
            print_warning(f"Skipping content for section {section_number}: No valid outline")
            return False
        
        if self.logger:
            self.logger.log_section_start(file_id, section_number, section_name, 'content')
        
        print_info(f"Processing content for section {section_number}: {section_name}")
        
        try:
            prompt = self._generate_content_prompt(chapter_name, chapter_name, section_name, outline)
            success, result, response_time = self._call_openai_api(prompt, "text", retries=3, temperature=0.7)
            
            if success:
                section['enhanced_section_content_md'] = result
                if self.logger:
                    self.logger.log_section_success(file_id, section_number, 'content')
                print_success(f"Content completed for section {section_number}")
                return True
            else:
                if self.logger:
                    self.logger.log_section_failure(file_id, section_number, 'content', str(result))
                print_error(f"Content failed for section {section_number}: {result}")
                return False
                
        except Exception as e:
            error_msg = f"Exception in content processing: {e}"
            if self.logger:
                self.logger.log_section_failure(file_id, section_number, 'content', error_msg)
            print_error(f"Content exception for section {section_number}: {error_msg}")
            return False
    
    def get_stats(self) -> Dict:
        """Get processing statistics"""
        success_rate = (self.stats['successful_requests'] / self.stats['total_requests'] * 100) if self.stats['total_requests'] > 0 else 100
        avg_time = (self.stats['total_processing_time'] / self.stats['total_requests']) if self.stats['total_requests'] > 0 else 0
        
        return {
            'total_requests': self.stats['total_requests'],
            'successful_requests': self.stats['successful_requests'],
            'failed_requests': self.stats['failed_requests'],
            'success_rate': success_rate,
            'average_response_time': avg_time,
            'total_processing_time': self.stats['total_processing_time']
        }

# === Utility Functions ===
def load_json_file(file_path: str) -> Optional[List[Dict]]:
    """Load and parse JSON file"""
    if not Path(file_path).is_file():
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                print_error(f"Input file {file_path} is not a JSON list of objects.")
                return None
            return data
    except json.JSONDecodeError as e:
        print_error(f"Invalid JSON in file: {file_path}\n{e}")
    except Exception as e:
        print_error(f"Could not load JSON file: {file_path}\n{e}")
    return None

def save_json_file(data: List[Dict], file_path: str):
    """Save data to JSON file"""
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        temp_file_path = Path(file_path).with_suffix(f"{Path(file_path).suffix}.tmp")
        with open(temp_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        os.replace(temp_file_path, file_path)
    except Exception as e:
        print_error(f"Could not save JSON file: {file_path}\n{e}")

def save_text_file(content: str, file_path: str):
    """Save text content to file"""
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        temp_file_path = Path(file_path).with_suffix(f"{Path(file_path).suffix}.tmp")
        with open(temp_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        os.replace(temp_file_path, file_path)
    except Exception as e:
        print_error(f"Could not save text file: {file_path}\n{e}")

def discover_json_files(folder_path: Path) -> List[Path]:
    """Discover JSON files in folder"""
    try:
        json_files = list(folder_path.glob("*.json"))
        return sorted(json_files)
    except Exception as e:
        print_error(f"Error discovering files: {e}")
        return []

# === Main Content System ===
class SimpleContentSystem:
    """Main content processing system - simplified version"""
    
    def __init__(self, input_folder: str, output_folder: str, model_name: str = "gpt-5-mini"):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.model_name = model_name
        
        # Initialize logger
        db_path = self.output_folder / "simple_processing.db"
        self.logger = SimpleLogger(db_path)
        
        # Initialize processor
        self.processor = SimpleContentProcessor(model_name, self.logger)
        
        print_success("Simple Content System initialized")
    
    def show_startup_info(self):
        """Display startup information"""
        print_header("Simple Content Generation System")
        
        print(f"Model: {self.model_name}")
        print(f"Input Folder: {self.input_folder}")
        print(f"Output Folder: {self.output_folder}")
        print(f"Database: {self.output_folder / 'simple_processing.db'}")
        
        print_success("System ready to start processing")
        return True
    
    def discover_and_validate_files(self) -> List[Path]:
        """Discover and validate JSON files"""
        json_files = discover_json_files(self.input_folder)
        
        if not json_files:
            print_error(f"No JSON files found in {self.input_folder}")
            return []
        
        print_success(f"Found {len(json_files)} JSON files to process")
        
        # Validate file structures
        valid_files = []
        for file_path in json_files:
            if not self.logger.should_process_file(str(file_path)):
                print_warning(f"{file_path.name}: Already completed, skipping")
                continue
                
            data = load_json_file(str(file_path))
            if data:
                sections_with_content = [s for s in data if s.get("generated_section_content_md", "").strip()]
                if sections_with_content:
                    valid_files.append(file_path)
                    print_success(f"{file_path.name}: {len(sections_with_content)} sections with content")
                else:
                    print_warning(f"{file_path.name}: No sections with content found")
            else:
                print_error(f"{file_path.name}: Invalid JSON structure")
        
        return valid_files
    
    def process_single_file(self, file_path: Path) -> bool:
        """Process a single JSON file"""
        filename = file_path.name
        file_stem = file_path.stem
        
        # Create individual folder for this file
        file_output_folder = self.output_folder / file_stem
        file_output_folder.mkdir(parents=True, exist_ok=True)
        
        # Setup output paths
        stage1_output_path = file_output_folder / "outline.json"
        stage2_output_path = file_output_folder / "content.json"
        final_article_path = file_output_folder / "final_article.md"
        
        # Load input data
        input_data = load_json_file(str(file_path))
        if not input_data:
            print_error(f"Failed to load {filename}")
            return False
        
        # Get valid sections
        valid_sections = [s for s in input_data if s.get("generated_section_content_md", "").strip()]
        if not valid_sections:
            print_warning(f"No valid sections found in {filename}")
            return False
        
        # Register file
        file_id = self.logger.register_file(str(file_path.resolve()), filename, len(valid_sections))
        
        print_section(f"Processing file: {filename} (ID: {file_id})")
        print_info(f"Output folder: {file_output_folder}")
        print_info(f"Found {len(valid_sections)} sections to process")
        
        try:
            # Get chapter name from first section
            chapter_name = valid_sections[0].get('chapter_name', filename)
            
            # Stage 1: Process outlines sequentially
            print_section("Stage 1: Generating Outlines")
            outline_success = 0
            outline_failed = 0
            
            completed_outlines = self.logger.get_completed_sections(file_id, 'outline')
            
            for i, section in enumerate(valid_sections, 1):
                section_number = section.get('section_number')
                if section_number in completed_outlines:
                    print_info(f"Outline {section_number}: Already completed")
                    outline_success += 1
                    continue
                
                print_progress(i, len(valid_sections), "outline sections")
                success = self.processor.process_section_outline(file_id, section, chapter_name)
                
                if success:
                    outline_success += 1
                else:
                    outline_failed += 1
                
                # Update progress
                self.logger.update_file_progress(file_id, outline_success, outline_failed)
                
                # Small delay to avoid rate limits
                time.sleep(0.5)
            
            print_info(f"Outline stage: {outline_success} successful, {outline_failed} failed")
            
            if outline_failed > 0:
                print_warning(f"Some outlines failed. Continuing with content generation for successful ones.")
            
            # Save after outline stage
            save_json_file(input_data, str(stage1_output_path))
            
            # Stage 2: Process content sequentially
            print_section("Stage 2: Generating Content")
            content_success = 0
            content_failed = 0
            
            completed_content = self.logger.get_completed_sections(file_id, 'content')
            
            for i, section in enumerate(valid_sections, 1):
                section_number = section.get('section_number')
                if section_number in completed_content:
                    print_info(f"Content {section_number}: Already completed")
                    content_success += 1
                    continue
                
                print_progress(i, len(valid_sections), "content sections")
                success = self.processor.process_section_content(file_id, section, chapter_name)
                
                if success:
                    content_success += 1
                else:
                    content_failed += 1
                
                # Update progress
                self.logger.update_file_progress(file_id, content_success, content_failed)
                
                # Small delay to avoid rate limits
                time.sleep(0.5)
            
            print_info(f"Content stage: {content_success} successful, {content_failed} failed")
            
            # Save final outputs
            save_json_file(input_data, str(stage2_output_path))
            
            # Assemble final article
            print_info("Assembling final article...")
            enhanced_sections = [s.get('enhanced_section_content_md', '') 
                               for s in input_data 
                               if s.get('enhanced_section_content_md')]
            
            if enhanced_sections:
                final_article = "\n\n---\n\n".join(enhanced_sections)
                save_text_file(final_article, str(final_article_path))
            
            # Save metadata
            metadata = {
                "source_file": filename,
                "processed_at": datetime.now().isoformat(),
                "total_sections": len(valid_sections),
                "successful_outlines": outline_success,
                "successful_content": content_success,
                "output_files": {
                    "outline": "outline.json",
                    "content": "content.json", 
                    "final_article": "final_article.md"
                }
            }
            metadata_path = file_output_folder / "processing_metadata.json"
            save_json_file([metadata], str(metadata_path))
            
            # Mark file as completed
            final_status = 'completed' if (outline_failed == 0 and content_failed == 0) else 'partial'
            self.logger.complete_file(file_id, final_status)
            
            if final_status == 'completed':
                print_success(f"Successfully completed {filename}")
            else:
                print_warning(f"Partially completed {filename}")
            
            print_info(f"All outputs saved in: {file_output_folder}")
            return final_status == 'completed'
            
        except Exception as e:
            print_error(f"Error processing {filename}: {e}")
            self.logger.complete_file(file_id, 'failed')
            return False
    
    def show_final_summary(self):
        """Display final processing summary"""
        stats = self.processor.get_stats()
        
        print_header("Final Processing Summary")
        
        print_section("API Usage Summary")
        print(f"Total API Requests: {stats['total_requests']}")
        print(f"Successful Requests: {stats['successful_requests']}")
        print(f"Failed Requests: {stats['failed_requests']}")
        print(f"Success Rate: {stats['success_rate']:.1f}%")
        print(f"Average Response Time: {stats['average_response_time']:.2f}s")
        print(f"Total Processing Time: {stats['total_processing_time']:.2f}s")
        print(f"Output Directory: {self.output_folder}")
    
    def process_all_files(self, force_rerun: bool = False) -> bool:
        """Process all files in the input folder"""
        
        # Show startup info
        if not self.show_startup_info():
            return False
        
        # Discover and validate files
        valid_files = self.discover_and_validate_files()
        if not valid_files:
            return False
        
        # Process each file
        processed_files = 0
        failed_files = 0
        
        try:
            for i, file_path in enumerate(valid_files, 1):
                try:
                    print_progress(i, len(valid_files), "files")
                    success = self.process_single_file(file_path)
                    
                    if success:
                        processed_files += 1
                    else:
                        failed_files += 1
                        
                except KeyboardInterrupt:
                    print_warning("Process interrupted by user")
                    return False
                    
                except Exception as e:
                    print_error(f"Critical error processing {file_path.name}: {e}")
                    failed_files += 1
                    continue
            
            # Show final summary
            self.show_final_summary()
            
            print_section("File Processing Summary")
            print(f"Successfully processed: {processed_files} files")
            print(f"Failed: {failed_files} files")
            
            return failed_files == 0
            
        finally:
            # Ensure logger is properly closed
            self.logger.close()

# === Main Entry Point ===
def main():
    """Main entry point"""
    load_dotenv()
    
    parser = argparse.ArgumentParser(
        description='Simple Content Generation System - Single API Key Version',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python script.py /path/to/json/folder
  python script.py /path/to/json/folder --model gpt-5-mini
  python script.py /path/to/json/folder --output-folder /path/to/output

Environment Variables:
  OPENAI_API_KEY      - Your OpenAI API key (required)

Features:
  - Simple single API key processing
  - Sequential processing (no parallel workers)
  - Perfect resume functionality with SQLite logging
  - Two-stage processing: Outline Generation → Content Enhancement
  - Individual output folders for each processed file

Common Issues & Solutions:
  1. Invalid Model: Use 'gpt-5-mini' or 'gpt-4o' or other valid OpenAI models
  2. Rate Limits: Built-in delays between requests
  3. API Key: Ensure OPENAI_API_KEY environment variable is set
  4. Authentication: Check OpenAI account has sufficient credits
        """
    )
    
    parser.add_argument('input_folder', help='Path to folder containing JSON files')
    parser.add_argument('--output-folder', help='Output folder (default: input_folder/results)')
    parser.add_argument('--model', default='gpt-5-mini', help='OpenAI model to use (default: gpt-5-mini)')
    parser.add_argument('--force-rerun', action='store_true', help='Force rerun of already completed files')
    
    args = parser.parse_args()
    
    # Validate input folder
    input_folder = Path(args.input_folder)
    if not input_folder.exists():
        print_error(f"Folder not found: {input_folder}")
        sys.exit(1)
    
    if not input_folder.is_dir():
        print_error(f"Path is not a directory: {input_folder}")
        sys.exit(1)
    
    # Setup output folder
    output_folder = args.output_folder or str(input_folder / "results")
    
    # Initialize and run system
    try:
        system = SimpleContentSystem(
            input_folder=str(input_folder),
            output_folder=output_folder,
            model_name=args.model
        )
        
        success = system.process_all_files(force_rerun=args.force_rerun)
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print_warning("Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Critical error: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()