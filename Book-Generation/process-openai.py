# -*- coding: utf-8 -*-
"""
File-Level Multi-API Key Content Generation System
Each worker takes one complete JSON file and processes it fully (outline + content) with one API key.
Parallel processing at the file level, sequential processing within each file.
"""
import json
import os
import argparse
import time
import random
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import sys
import traceback
import re
import sqlite3
import threading
import concurrent.futures
from dataclasses import dataclass
import uuid

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

# === Data Classes ===
@dataclass
class FileTask:
    """Represents a complete file processing task"""
    task_id: str
    file_path: Path
    output_folder: Path
    model_name: str
    
    def __post_init__(self):
        if not self.task_id:
            self.task_id = f"file_{uuid.uuid4().hex[:8]}"

@dataclass
class APIKeyStats:
    """Statistics for an API key"""
    key_name: str
    total_files: int = 0
    successful_files: int = 0
    failed_files: int = 0
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    active_files: int = 0
    last_used: float = 0
    
    @property
    def success_rate(self) -> float:
        if self.total_files == 0:
            return 100.0
        return (self.successful_files / self.total_files) * 100
    
    @property
    def load_score(self) -> float:
        """Lower score = better choice for assignment"""
        return self.active_files * 1000 + self.failed_files * 100 + self.total_files

# === Database Logger ===
class DatabaseLogger:
    """Thread-safe SQLite logging for tracking progress"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.connection = self._init_database()
        self.lock = threading.Lock()
    
    def _init_database(self) -> sqlite3.Connection:
        """Initialize the SQLite database"""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Files table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Files (
                file_id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT UNIQUE NOT NULL,
                filename TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                api_key_used TEXT,
                total_sections INTEGER,
                processed_sections INTEGER DEFAULT 0,
                failed_sections INTEGER DEFAULT 0,
                started_at TIMESTAMP,
                completed_at TIMESTAMP,
                processing_time REAL,
                error_message TEXT
            )
        ''')
        
        # Sections table
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
        
        # API Usage table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS APIUsage (
                usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
                api_key_name TEXT NOT NULL,
                file_id INTEGER,
                request_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                success BOOLEAN,
                response_time REAL,
                error_message TEXT
            )
        ''')
        
        conn.commit()
        return conn
    
    def register_file(self, file_path: str, filename: str, total_sections: int) -> int:
        """Register a new file and return file_id"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO Files (file_path, filename, total_sections)
                VALUES (?, ?, ?)
            """, (file_path, filename, total_sections))
            
            cursor.execute("SELECT file_id FROM Files WHERE file_path = ?", (file_path,))
            file_id = cursor.fetchone()['file_id']
            self.connection.commit()
            return file_id
    
    def start_file_processing(self, file_id: int, api_key: str):
        """Mark file as started"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Files 
                SET status = 'processing', api_key_used = ?, started_at = ?
                WHERE file_id = ?
            """, (api_key, datetime.now(), file_id))
            self.connection.commit()
    
    def complete_file_processing(self, file_id: int, status: str, processing_time: float, 
                               processed: int, failed: int, error_msg: str = None):
        """Mark file as completed"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                UPDATE Files 
                SET status = ?, completed_at = ?, processing_time = ?, 
                    processed_sections = ?, failed_sections = ?, error_message = ?
                WHERE file_id = ?
            """, (status, datetime.now(), processing_time, processed, failed, error_msg, file_id))
            self.connection.commit()
    
    def log_section_processing(self, file_id: int, section_number: str, section_name: str, 
                             stage: str, status: str, error_msg: str = None):
        """Log section processing result"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO Sections 
                (file_id, section_number, section_name, stage, status, completed_at, error_message)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (file_id, section_number, section_name, stage, status, datetime.now(), error_msg))
            self.connection.commit()
    
    def log_api_usage(self, api_key: str, file_id: int, success: bool, 
                     response_time: float = None, error_msg: str = None):
        """Log API usage"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO APIUsage (api_key_name, file_id, success, response_time, error_message)
                VALUES (?, ?, ?, ?, ?)
            """, (api_key, file_id, success, response_time, error_msg))
            self.connection.commit()
    
    def should_process_file(self, file_path: str) -> bool:
        """Check if file should be processed"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("SELECT status FROM Files WHERE file_path = ?", (file_path,))
            result = cursor.fetchone()
            return not result or result['status'] != 'completed'
    
    def close(self):
        """Close database connection"""
        self.connection.close()

# === File Processor (Worker) ===
class FileProcessor:
    """Processes a complete file with single API key"""
    
    def __init__(self, api_key: str, key_name: str, model_name: str, logger: DatabaseLogger):
        self.api_key = api_key
        self.key_name = key_name
        self.model_name = model_name
        self.logger = logger
        
        # Initialize OpenAI client
        try:
            self.client = OpenAI(api_key=api_key)
        except Exception as e:
            raise Exception(f"Failed to initialize OpenAI client for {key_name}: {e}")
        
        # Statistics for this processor
        self.stats = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'processing_time': 0
        }
    
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
                self.stats['processing_time'] += response_time
                
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
                                return False, last_error, response_time
                    else:
                        self.stats['successful_requests'] += 1
                        return True, content, response_time
                else:
                    last_error = "Empty response from OpenAI API"
                    if attempt == retries:
                        self.stats['failed_requests'] += 1
                        return False, last_error, response_time
                
            except Exception as e:
                last_error = f"API Error: {type(e).__name__}: {str(e)}"
                if "rate_limit" in str(e).lower():
                    if attempt < retries:
                        time.sleep(random.uniform(5, 15))
                        continue
                elif "invalid" in str(e).lower() and "model" in str(e).lower():
                    self.stats['failed_requests'] += 1
                    return False, last_error, time.time() - start_time
                elif "authentication" in str(e).lower():
                    self.stats['failed_requests'] += 1
                    return False, last_error, time.time() - start_time
                
                if attempt == retries:
                    self.stats['failed_requests'] += 1
                    return False, last_error, time.time() - start_time
            
            if attempt < retries:
                wait_time = random.uniform(1, 3) * (attempt + 1)
                time.sleep(wait_time)
        
        self.stats['failed_requests'] += 1
        return False, last_error or "Unknown error after all retries", time.time() - start_time
    
    def process_complete_file(self, task: FileTask) -> bool:
        """Process a complete file (outline + content stages)"""
        file_path = task.file_path
        output_folder = task.output_folder
        
        print_info(f"[{self.key_name}] Starting file: {file_path.name}")
        
        # Load input data
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                input_data = json.load(f)
            
            if not isinstance(input_data, list):
                print_error(f"[{self.key_name}] Invalid JSON format in {file_path.name}")
                return False
                
        except Exception as e:
            print_error(f"[{self.key_name}] Failed to load {file_path.name}: {e}")
            return False
        
        # Filter valid sections
        valid_sections = [s for s in input_data if s.get("generated_section_content_md", "").strip()]
        if not valid_sections:
            print_warning(f"[{self.key_name}] No valid sections in {file_path.name}")
            return False
        
        # Register file and start processing
        file_id = self.logger.register_file(str(file_path.resolve()), file_path.name, len(valid_sections))
        self.logger.start_file_processing(file_id, self.key_name)
        
        start_time = time.time()
        chapter_name = valid_sections[0].get('chapter_name', file_path.stem)
        
        try:
            # Create output folder for this file
            file_output_folder = output_folder / file_path.stem
            file_output_folder.mkdir(parents=True, exist_ok=True)
            
            outline_success = 0
            outline_failed = 0
            content_success = 0
            content_failed = 0
            
            # Stage 1: Process outlines
            print_info(f"[{self.key_name}] Processing outlines for {file_path.name}")
            for section in valid_sections:
                section_number = section.get('section_number')
                section_name = section.get('section_name', '')
                content = section.get('generated_section_content_md', '')
                
                # Generate outline
                prompt = self._generate_outline_prompt(chapter_name, chapter_name, section_name, content)
                success, result, response_time = self._call_openai_api(prompt, "json", retries=3, temperature=0.5)
                
                # Log API usage
                self.logger.log_api_usage(self.key_name, file_id, success, response_time, 
                                        str(result) if not success else None)
                
                if success:
                    section['section_outline_response'] = result
                    outline_success += 1
                    self.logger.log_section_processing(file_id, section_number, section_name, 
                                                     'outline', 'completed')
                else:
                    outline_failed += 1
                    self.logger.log_section_processing(file_id, section_number, section_name, 
                                                     'outline', 'failed', str(result))
                
                # Small delay between requests
                time.sleep(0.5)
            
            # Save after outline stage
            outline_path = file_output_folder / "outline.json"
            with open(outline_path, 'w', encoding='utf-8') as f:
                json.dump(input_data, f, indent=2, ensure_ascii=False)
            
            # Stage 2: Process content
            print_info(f"[{self.key_name}] Processing content for {file_path.name}")
            for section in valid_sections:
                section_number = section.get('section_number')
                section_name = section.get('section_name', '')
                outline = section.get('section_outline_response')
                
                if not outline or (isinstance(outline, dict) and outline.get('error')):
                    content_failed += 1
                    self.logger.log_section_processing(file_id, section_number, section_name, 
                                                     'content', 'failed', 'No valid outline')
                    continue
                
                # Generate content
                prompt = self._generate_content_prompt(chapter_name, chapter_name, section_name, outline)
                success, result, response_time = self._call_openai_api(prompt, "text", retries=3, temperature=0.7)
                
                # Log API usage
                self.logger.log_api_usage(self.key_name, file_id, success, response_time, 
                                        str(result) if not success else None)
                
                if success:
                    section['enhanced_section_content_md'] = result
                    content_success += 1
                    self.logger.log_section_processing(file_id, section_number, section_name, 
                                                     'content', 'completed')
                else:
                    content_failed += 1
                    self.logger.log_section_processing(file_id, section_number, section_name, 
                                                     'content', 'failed', str(result))
                
                # Small delay between requests
                time.sleep(0.5)
            
            # Save final outputs
            content_path = file_output_folder / "content.json"
            with open(content_path, 'w', encoding='utf-8') as f:
                json.dump(input_data, f, indent=2, ensure_ascii=False)
            
            # Assemble final article
            enhanced_sections = [s.get('enhanced_section_content_md', '') 
                               for s in input_data 
                               if s.get('enhanced_section_content_md')]
            
            if enhanced_sections:
                final_article = "\n\n---\n\n".join(enhanced_sections)
                final_path = file_output_folder / "final_article.md"
                with open(final_path, 'w', encoding='utf-8') as f:
                    f.write(final_article)
            
            # Save metadata
            metadata = {
                "source_file": file_path.name,
                "processed_at": datetime.now().isoformat(),
                "api_key_used": self.key_name,
                "total_sections": len(valid_sections),
                "successful_outlines": outline_success,
                "successful_content": content_success,
                "failed_outlines": outline_failed,
                "failed_content": content_failed,
                "output_files": {
                    "outline": "outline.json",
                    "content": "content.json", 
                    "final_article": "final_article.md"
                }
            }
            metadata_path = file_output_folder / "processing_metadata.json"
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump([metadata], f, indent=2, ensure_ascii=False)
            
            # Determine final status
            processing_time = time.time() - start_time
            total_processed = outline_success + content_success
            total_failed = outline_failed + content_failed
            
            if total_failed == 0:
                status = 'completed'
                print_success(f"[{self.key_name}] Completed {file_path.name} ({total_processed} sections)")
            else:
                status = 'partial'
                print_warning(f"[{self.key_name}] Partial completion {file_path.name} ({total_processed} success, {total_failed} failed)")
            
            # Log completion
            self.logger.complete_file_processing(file_id, status, processing_time, 
                                               total_processed, total_failed)
            
            return status == 'completed'
            
        except Exception as e:
            processing_time = time.time() - start_time
            error_msg = f"Exception processing file: {e}"
            self.logger.complete_file_processing(file_id, 'failed', processing_time, 0, 0, error_msg)
            print_error(f"[{self.key_name}] Exception in {file_path.name}: {error_msg}")
            return False
    
    def get_stats(self) -> Dict:
        """Get processor statistics"""
        success_rate = (self.stats['successful_requests'] / self.stats['total_requests'] * 100) if self.stats['total_requests'] > 0 else 100
        return {
            'key_name': self.key_name,
            'total_requests': self.stats['total_requests'],
            'successful_requests': self.stats['successful_requests'],
            'failed_requests': self.stats['failed_requests'],
            'success_rate': success_rate,
            'processing_time': self.stats['processing_time']
        }

# === Main Manager ===
class FileManagerSystem:
    """Main system that manages multiple API keys and distributes files"""
    
    def __init__(self, input_folder: str, output_folder: str, model_name: str = "gpt-5-mini"):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.model_name = model_name
        
        # Initialize database logger
        db_path = self.output_folder / "file_manager_processing.db"
        self.logger = DatabaseLogger(db_path)
        
        # Discover API keys
        self.api_keys = self._discover_api_keys()
        
        # API key statistics
        self.api_stats = {
            f"key_{i+1}": APIKeyStats(f"key_{i+1}") 
            for i in range(len(self.api_keys))
        }
        
        self.lock = threading.Lock()
        
        print_success(f"Initialized File Manager with {len(self.api_keys)} API keys")
    
    def _discover_api_keys(self) -> List[str]:
        """Discover all available OpenAI API keys"""
        api_keys = []
        
        # Primary key
        primary_key = os.getenv('OPENAI_API_KEY')
        if primary_key:
            api_keys.append(primary_key)
        
        # Numbered keys
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
    
    def discover_files(self) -> List[Path]:
        """Discover JSON files to process"""
        try:
            json_files = list(self.input_folder.glob("*.json"))
            valid_files = []
            
            for file_path in sorted(json_files):
                if self.logger.should_process_file(str(file_path)):
                    valid_files.append(file_path)
                else:
                    print_warning(f"{file_path.name}: Already completed, skipping")
            
            return valid_files
        except Exception as e:
            print_error(f"Error discovering files: {e}")
            return []
    
    def process_all_files(self, max_workers: int = None) -> bool:
        """Process all files using multiple workers"""
        
        print_header("File Manager Content Generation System")
        print(f"Model: {self.model_name}")
        print(f"API Keys: {len(self.api_keys)}")
        print(f"Input Folder: {self.input_folder}")
        print(f"Output Folder: {self.output_folder}")
        
        # Discover files
        files_to_process = self.discover_files()
        if not files_to_process:
            print_error("No files to process")
            return False
        
        print_success(f"Found {len(files_to_process)} files to process")
        
        # Set max workers (default to number of API keys)
        max_workers = max_workers or len(self.api_keys)
        max_workers = min(max_workers, len(self.api_keys))  # Can't exceed number of keys
        
        print_info(f"Using {max_workers} workers")
        
        # Create file tasks
        tasks = []
        for file_path in files_to_process:
            task = FileTask(
                task_id="",
                file_path=file_path,
                output_folder=self.output_folder,
                model_name=self.model_name
            )
            tasks.append(task)
        
        # Process files in parallel
        successful_files = 0
        failed_files = 0
        
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                # Create processors (one per worker)
                processors = []
                for i in range(max_workers):
                    api_key = self.api_keys[i % len(self.api_keys)]
                    key_name = f"key_{(i % len(self.api_keys)) + 1}"
                    processor = FileProcessor(api_key, key_name, self.model_name, self.logger)
                    processors.append(processor)
                
                # Submit tasks
                future_to_task = {}
                for i, task in enumerate(tasks):
                    processor = processors[i % len(processors)]
                    future = executor.submit(processor.process_complete_file, task)
                    future_to_task[future] = (task, processor)
                
                # Collect results
                for future in concurrent.futures.as_completed(future_to_task):
                    task, processor = future_to_task[future]
                    try:
                        success = future.result()
                        if success:
                            successful_files += 1
                        else:
                            failed_files += 1
                            
                        # Update API stats
                        with self.lock:
                            key_name = processor.key_name
                            if key_name in self.api_stats:
                                stats = self.api_stats[key_name]
                                stats.total_files += 1
                                if success:
                                    stats.successful_files += 1
                                else:
                                    stats.failed_files += 1
                                
                                # Update request stats
                                proc_stats = processor.get_stats()
                                stats.total_requests += proc_stats['total_requests']
                                stats.successful_requests += proc_stats['successful_requests']
                                stats.failed_requests += proc_stats['failed_requests']
                        
                        print_progress(successful_files + failed_files, len(tasks), "files")
                        
                    except Exception as e:
                        print_error(f"Exception processing {task.file_path.name}: {e}")
                        failed_files += 1
            
            # Show final summary
            self._show_final_summary(successful_files, failed_files)
            
            return failed_files == 0
            
        finally:
            self.logger.close()
    
    def _show_final_summary(self, successful_files: int, failed_files: int):
        """Show final processing summary"""
        print_header("Final Processing Summary")
        
        print_section("File Processing Results")
        print(f"Successfully processed: {successful_files} files")
        print(f"Failed: {failed_files} files")
        print(f"Total files: {successful_files + failed_files}")
        
        print_section("API Key Performance")
        for key_name, stats in self.api_stats.items():
            if stats.total_files > 0:
                print(f"{key_name:8} | Files: {stats.total_files:3} | Success: {stats.successful_files:3} | "
                      f"Failed: {stats.failed_files:2} | Rate: {stats.success_rate:5.1f}% | "
                      f"Requests: {stats.total_requests:4}")
        
        print_section("Output Information")
        print(f"Output Directory: {self.output_folder}")
        print("Each file processed into its own subfolder containing:")
        print("  - outline.json (after outline stage)")
        print("  - content.json (after content stage)")
        print("  - final_article.md (assembled final content)")
        print("  - processing_metadata.json (processing details)")

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

# === Main Entry Point ===
def main():
    """Main entry point"""
    load_dotenv()
    
    parser = argparse.ArgumentParser(
        description='File-Level Multi-API Key Content Generation System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python script.py /path/to/json/folder
  python script.py /path/to/json/folder --model gpt-5-mini
  python script.py /path/to/json/folder --workers 4

Environment Variables:
  OPENAI_API_KEY      - Primary API key  
  OPENAI_API_KEY_1    - Additional API key 1
  OPENAI_API_KEY_2    - Additional API key 2
  ... and so on

How It Works:
  - Each worker gets assigned one complete JSON file
  - Worker processes the entire file (outline + content) with one API key
  - Parallel processing at file level, sequential within each file
  - Each file gets its own output subfolder with all results

Features:
  - Perfect resume functionality with SQLite logging
  - Load balancing across multiple API keys
  - File-level parallelization (cleaner than section-level)
  - Complete isolation: one API key = one file at a time
  - Detailed progress tracking and statistics

Output Structure:
  output_folder/
    ├── file1_name/
    │   ├── outline.json
    │   ├── content.json
    │   ├── final_article.md
    │   └── processing_metadata.json
    ├── file2_name/
    │   └── ... (same structure)
    └── file_manager_processing.db
        """
    )
    
    parser.add_argument('input_folder', help='Path to folder containing JSON files')
    parser.add_argument('--output-folder', help='Output folder (default: input_folder/results)')
    parser.add_argument('--model', default='gpt-5-mini', help='OpenAI model to use (default: gpt-5-mini)')
    parser.add_argument('--workers', type=int, help='Maximum number of parallel workers (default: number of API keys)')
    
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
        system = FileManagerSystem(
            input_folder=str(input_folder),
            output_folder=output_folder,
            model_name=args.model
        )
        
        success = system.process_all_files(max_workers=args.workers)
        
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