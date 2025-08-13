# -*- coding: utf-8 -*-
"""
Dual Manager Content Generation System V11 - SIMPLE PYTHON OUTPUT
- TWO-MANAGER ARCHITECTURE WITH SPECIALIZED RESPONSIBILITIES

Manager 1: API Processing Manager - Handles all API operations, load balancing, and content processing
Manager 2: Database Logging Manager - Handles all database operations, logging, and state management

Processes Wikipedia-generated JSON files with intelligent API key management and comprehensive logging.
Enhanced with detailed error reporting, diagnostics, and connectivity testing.
Uses simple Python output formatting (no Rich library).
"""
import json
import os
import argparse
import time
import random
import gc
from typing import Dict, List, Any, Optional, Tuple, Set
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import sys
import traceback
import re
import sqlite3
import copy
import threading
import concurrent.futures
from dataclasses import dataclass
from queue import Queue, Empty
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
class SectionTask:
    """Represents a section processing task"""
    task_id: str
    file_id: int
    file_path: str
    section_number: str
    section_name: str
    chapter_name: str
    stage: str  # 'outline' or 'content'
    section_data: Dict
    priority: int = 0
    
    def __post_init__(self):
        if not self.task_id:
            self.task_id = f"{self.file_id}_{self.section_number}_{self.stage}_{uuid.uuid4().hex[:8]}"

@dataclass
class APIKeyStats:
    """Statistics for an API key"""
    key_name: str
    total_requests: int = 0
    active_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    last_used: float = 0
    average_response_time: float = 0
    
    @property
    def success_rate(self) -> float:
        if self.total_requests == 0:
            return 100.0
        return (self.successful_requests / self.total_requests) * 100
    
    @property
    def load_score(self) -> float:
        """Lower score = better choice"""
        return (self.active_requests * 100) + self.failed_requests + (self.total_requests * 0.1)

@dataclass
class ProcessingEvent:
    """Event sent from API Manager to Logging Manager"""
    event_type: str  # 'file_started', 'section_started', 'section_completed', etc.
    file_id: int
    data: Dict
    timestamp: float = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()

# === Database Logging Manager (Manager 2) ===
class DatabaseLoggingManager:
    """Handles all database operations, logging, and state management"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.connection = self._init_database()
        self.lock = threading.Lock()
        self.event_queue = Queue()
        self.running = True
        
        # Statistics
        self.stats = {
            'files_processed': 0,
            'files_failed': 0,
            'sections_processed': 0,
            'sections_failed': 0,
            'total_api_calls': 0
        }
        
        # Start event processing thread
        self.event_processor = threading.Thread(target=self._process_events, daemon=True)
        self.event_processor.start()
    
    def _init_database(self) -> sqlite3.Connection:
        """Initialize the SQLite database with all required tables"""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Files table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Files (
                file_id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT UNIQUE NOT NULL,
                filename TEXT NOT NULL,
                stage1_output_path TEXT,
                stage2_output_path TEXT,
                final_article_path TEXT,
                total_sections INTEGER,
                file_status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                started_at TIMESTAMP,
                completed_at TIMESTAMP
            )
        ''')
        
        # Stages table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Stages (
                stage_id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                stage_name TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                started_at TIMESTAMP,
                completed_at TIMESTAMP,
                success_count INTEGER DEFAULT 0,
                failure_count INTEGER DEFAULT 0,
                FOREIGN KEY (file_id) REFERENCES Files (file_id),
                UNIQUE (file_id, stage_name)
            )
        ''')
        
        # Sections table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sections (
                section_id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_id INTEGER NOT NULL,
                section_number TEXT NOT NULL,
                section_name TEXT,
                chapter_name TEXT,
                stage TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                api_key_used TEXT,
                started_at TIMESTAMP,
                completed_at TIMESTAMP,
                processing_time REAL,
                error_message TEXT,
                retry_count INTEGER DEFAULT 0,
                FOREIGN KEY (file_id) REFERENCES Files (file_id),
                UNIQUE (file_id, section_number, stage)
            )
        ''')
        
        # API Usage table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS APIUsage (
                usage_id INTEGER PRIMARY KEY AUTOINCREMENT,
                api_key_name TEXT NOT NULL,
                request_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                file_id INTEGER,
                section_number TEXT,
                stage TEXT,
                success BOOLEAN,
                response_time REAL,
                error_message TEXT
            )
        ''')
        
        # Batch Sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS BatchSessions (
                session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                input_folder TEXT NOT NULL,
                output_folder TEXT NOT NULL,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                total_files INTEGER,
                processed_files INTEGER DEFAULT 0,
                failed_files INTEGER DEFAULT 0,
                session_status TEXT DEFAULT 'running'
            )
        ''')
        
        conn.commit()
        return conn
    
    def _process_events(self):
        """Process events from the API Manager"""
        while self.running:
            try:
                event = self.event_queue.get(timeout=1.0)
                self._handle_event(event)
                self.event_queue.task_done()
            except Empty:
                continue
            except Exception as e:
                print_error(f"Error processing event: {e}")
    
    def _handle_event(self, event: ProcessingEvent):
        """Handle a single event from the API Manager"""
        with self.lock:
            cursor = self.connection.cursor()
            
            try:
                if event.event_type == 'file_started':
                    self._handle_file_started(cursor, event)
                elif event.event_type == 'section_started':
                    self._handle_section_started(cursor, event)
                elif event.event_type == 'section_completed':
                    self._handle_section_completed(cursor, event)
                elif event.event_type == 'section_failed':
                    self._handle_section_failed(cursor, event)
                elif event.event_type == 'stage_completed':
                    self._handle_stage_completed(cursor, event)
                elif event.event_type == 'file_completed':
                    self._handle_file_completed(cursor, event)
                elif event.event_type == 'api_usage':
                    self._handle_api_usage(cursor, event)
                
                self.connection.commit()
                
            except Exception as e:
                self.connection.rollback()
                print_error(f"Database error: {e}")
    
    def _handle_file_started(self, cursor, event):
        """Handle file started event"""
        data = event.data
        cursor.execute("""
            UPDATE Files 
            SET file_status = 'processing', started_at = ?
            WHERE file_id = ?
        """, (datetime.fromtimestamp(event.timestamp), event.file_id))
        
        # Initialize stage records
        for stage in ['outline', 'content']:
            cursor.execute("""
                INSERT OR IGNORE INTO Stages (file_id, stage_name, status)
                VALUES (?, ?, 'pending')
            """, (event.file_id, stage))
    
    def _handle_section_started(self, cursor, event):
        """Handle section started event"""
        data = event.data
        cursor.execute("""
            INSERT OR REPLACE INTO Sections 
            (file_id, section_number, section_name, chapter_name, stage, status, api_key_used, started_at)
            VALUES (?, ?, ?, ?, ?, 'processing', ?, ?)
        """, (event.file_id, data['section_number'], data.get('section_name', ''), 
              data.get('chapter_name', ''), data['stage'], data['api_key'], 
              datetime.fromtimestamp(event.timestamp)))
    
    def _handle_section_completed(self, cursor, event):
        """Handle section completed event"""
        data = event.data
        processing_time = data.get('processing_time', 0)
        
        cursor.execute("""
            UPDATE Sections 
            SET status = 'completed', completed_at = ?, processing_time = ?
            WHERE file_id = ? AND section_number = ? AND stage = ?
        """, (datetime.fromtimestamp(event.timestamp), processing_time,
              event.file_id, data['section_number'], data['stage']))
        
        self.stats['sections_processed'] += 1
    
    def _handle_section_failed(self, cursor, event):
        """Handle section failed event"""
        data = event.data
        cursor.execute("""
            UPDATE Sections 
            SET status = 'failed', completed_at = ?, error_message = ?, retry_count = retry_count + 1
            WHERE file_id = ? AND section_number = ? AND stage = ?
        """, (datetime.fromtimestamp(event.timestamp), data.get('error', ''),
              event.file_id, data['section_number'], data['stage']))
        
        self.stats['sections_failed'] += 1
    
    def _handle_stage_completed(self, cursor, event):
        """Handle stage completed event"""
        data = event.data
        cursor.execute("""
            UPDATE Stages 
            SET status = ?, completed_at = ?, success_count = ?, failure_count = ?
            WHERE file_id = ? AND stage_name = ?
        """, (data['status'], datetime.fromtimestamp(event.timestamp),
              data['success_count'], data['failure_count'],
              event.file_id, data['stage']))
    
    def _handle_file_completed(self, cursor, event):
        """Handle file completed event"""
        data = event.data
        cursor.execute("""
            UPDATE Files 
            SET file_status = ?, completed_at = ?
            WHERE file_id = ?
        """, (data['status'], datetime.fromtimestamp(event.timestamp), event.file_id))
        
        if data['status'] == 'completed':
            self.stats['files_processed'] += 1
        else:
            self.stats['files_failed'] += 1
    
    def _handle_api_usage(self, cursor, event):
        """Handle API usage logging"""
        data = event.data
        cursor.execute("""
            INSERT INTO APIUsage 
            (api_key_name, file_id, section_number, stage, success, response_time, error_message)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (data['api_key'], event.file_id, data.get('section_number'),
              data.get('stage'), data['success'], data.get('response_time'),
              data.get('error')))
        
        self.stats['total_api_calls'] += 1
    
    # Public Interface Methods
    
    def log_event(self, event: ProcessingEvent):
        """Queue an event for processing"""
        self.event_queue.put(event)
    
    def register_file(self, file_path: str, filename: str, total_sections: int, 
                     stage1_path: str, stage2_path: str, final_path: str) -> int:
        """Register a new file and return file_id"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT OR IGNORE INTO Files 
                (file_path, filename, total_sections, stage1_output_path, stage2_output_path, final_article_path)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (file_path, filename, total_sections, stage1_path, stage2_path, final_path))
            
            cursor.execute("SELECT file_id FROM Files WHERE file_path = ?", (file_path,))
            file_id = cursor.fetchone()['file_id']
            self.connection.commit()
            return file_id
    
    def get_processed_sections(self, file_id: int, stage: str) -> Set[str]:
        """Get set of completed section numbers for a file and stage"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT section_number FROM Sections 
                WHERE file_id = ? AND stage = ? AND status = 'completed'
            """, (file_id, stage))
            return {row['section_number'] for row in cursor.fetchall()}
    
    def get_file_status(self, file_id: int) -> str:
        """Get current status of a file"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("SELECT file_status FROM Files WHERE file_id = ?", (file_id,))
            result = cursor.fetchone()
            return result['file_status'] if result else 'unknown'
    
    def get_stage_status(self, file_id: int, stage: str) -> str:
        """Get current status of a stage for a file"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT status FROM Stages WHERE file_id = ? AND stage_name = ?
            """, (file_id, stage))
            result = cursor.fetchone()
            return result['status'] if result else 'pending'
    
    def should_process_file(self, file_path: str) -> bool:
        """Check if a file should be processed (not already completed)"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT file_status FROM Files WHERE file_path = ?
            """, (file_path,))
            result = cursor.fetchone()
            return not result or result['file_status'] != 'completed'
    
    def get_processing_stats(self) -> Dict:
        """Get current processing statistics"""
        return self.stats.copy()
    
    def start_batch_session(self, input_folder: str, output_folder: str, total_files: int) -> int:
        """Start a new batch processing session"""
        with self.lock:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO BatchSessions (input_folder, output_folder, total_files)
                VALUES (?, ?, ?)
            """, (input_folder, output_folder, total_files))
            session_id = cursor.lastrowid
            self.connection.commit()
            return session_id
    
    def close(self):
        """Close the logging manager"""
        self.running = False
        if self.event_processor.is_alive():
            self.event_processor.join(timeout=5.0)
        self.connection.close()

# === API Processing Manager (Manager 1) ===
class APIProcessingManager:
    """Handles all API operations, load balancing, and content processing"""
    
    def __init__(self, model_name: str = "gpt-5-mini", logging_manager: DatabaseLoggingManager = None):
        self.model_name = model_name
        self.logging_manager = logging_manager
        
        # Discover and initialize API keys
        self.api_keys = self._discover_api_keys()
        self.clients = self._initialize_clients()
        
        # API key statistics and management
        self.api_stats = {
            f"key_{i+1}": APIKeyStats(f"key_{i+1}") 
            for i in range(len(self.api_keys))
        }
        
        self.lock = threading.Lock()
        
        print_success(f"Initialized API Processing Manager with {len(self.api_keys)} keys")
    
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
    
    def _initialize_clients(self) -> List[OpenAI]:
        """Initialize OpenAI clients for each API key"""
        if not OpenAI:
            raise Exception("OpenAI library not available")
        
        clients = []
        for i, api_key in enumerate(self.api_keys):
            try:
                client = OpenAI(api_key=api_key)
                clients.append(client)
            except Exception as e:
                raise Exception(f"Failed to initialize OpenAI client {i+1}: {e}")
        
        return clients
    
    def _get_best_api_key(self) -> Tuple[OpenAI, str, int, str]:
        """Get the best available API key using intelligent load balancing"""
        with self.lock:
            # Find the key with the lowest load score
            best_key = min(self.api_stats.keys(), key=lambda k: self.api_stats[k].load_score)
            best_index = int(best_key.split('_')[1]) - 1
            
            # Update statistics
            stats = self.api_stats[best_key]
            stats.total_requests += 1
            stats.active_requests += 1
            stats.last_used = time.time()
            
            return self.clients[best_index], best_key, best_index, self.api_keys[best_index]
    
    def _release_api_key(self, key_name: str, success: bool, response_time: float = 0):
        """Release an API key after use"""
        with self.lock:
            if key_name in self.api_stats:
                stats = self.api_stats[key_name]
                stats.active_requests = max(0, stats.active_requests - 1)
                
                if success:
                    stats.successful_requests += 1
                else:
                    stats.failed_requests += 1
                
                # Update average response time
                if response_time > 0:
                    if stats.average_response_time == 0:
                        stats.average_response_time = response_time
                    else:
                        stats.average_response_time = (stats.average_response_time + response_time) / 2
    
    def _generate_outline_prompt(self, paper_title: str, chapter_name: str, 
                                section_name: str, section_content: str) -> str:
        """Generate prompt for outline creation"""
        return f"""
# Expert Persona

You are a distinguished expert on India's Strategic Culture and National Security Policy with decades of experience analyzing Indian strategic thinking from a historical-civilizational perspective. You approach security analysis through the lens of India as a 'civilization-state' rather than just a nation-state.

# Your Analytical Framework

As an expert in Indian strategic culture, you understand that:
- India's strategic worldview is born from a predominant historical-civilizational perspective
- Strategic thinking must be analyzed through cultural, geopolitical, socio-economic, and historical factors
- India's approach engages with security from a global rather than purely national viewpoint
- Strategic culture draws from political culture and civilizational ethos
- Analysis should identify continuity and change in strategic thinking across different eras

# Current Analysis Task

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
        "main_themes": [],
        "key_concepts": [],
        "strategic_implications": [],
        "civilizational_context": "",
        "policy_relevance": ""
    }},
    "professor_summary": "Brief summary of the analysis"
}}
```
"""
    
    def _generate_content_prompt(self, paper_title: str, chapter_name: str, 
                                section_name: str, outline_json: Dict) -> str:
        """Generate prompt for content creation"""
        outline_str = json.dumps(outline_json, indent=2, ensure_ascii=False)
        
        return f"""
# Expert Author Persona
You are a distinguished expert and author specializing in India's Strategic Culture and National Security Policy. You are writing a comprehensive academic book that analyzes Indian strategic thinking through a historical-civilizational lens. Your writing style is scholarly yet accessible, combining deep analytical insight with clear exposition.

# Your Writing Approach
Your expertise allows you to:

- Analyze strategic culture through the framework of India as a 'civilization-state'
- Connect historical precedents to contemporary strategic thinking
- Examine the interplay between cultural ethos and security policy
- Identify patterns of continuity and change in strategic approaches
- Contextualize strategic decisions within broader geopolitical frameworks

# Your Expert Analysis (Outline) to Transform into Content
{outline_str}

# What you need to do:

Understand the outline, each aspect of it, then turn this outline into a detailed, well-structured Markdown section that's a part of book, expand on each of topic, idea, and everything which is being talked in the outline, and write it in a way that is suitable for an academic book on India's Strategic Culture and National Security Policy.
"""
    
    def _call_openai_api(self, client: OpenAI, prompt: str, response_type: str = "json", 
                        retries: int = 3, temperature: float = 0.5) -> Tuple[bool, Any, float]:
        """Make API call to OpenAI with retries and detailed error reporting"""
        start_time = time.time()
        last_error = None
        
        for attempt in range(retries + 1):
            try:
                system_content = "You are an expert analyst. Always respond with valid JSON." if response_type == "json" else "You are an expert writer and analyst."
                
                response = client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": system_content},
                        {"role": "user", "content": prompt}
                    ],
                    max_completion_tokens=8192
                )
                
                response_time = time.time() - start_time
                
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
                            return True, parsed_json, response_time
                        except json.JSONDecodeError as json_err:
                            last_error = f"JSON Parse Error: {json_err} | Raw content: {content[:200]}..."
                            if attempt == retries:
                                print_error(f"JSON Parse Failed: {last_error}")
                                return False, last_error, response_time
                    else:
                        return True, content, response_time
                else:
                    last_error = "Empty response from OpenAI API"
                    if attempt == retries:
                        print_error(f"Empty Response: {last_error}")
                        return False, last_error, response_time
                
            except Exception as e:
                last_error = f"API Error: {type(e).__name__}: {str(e)}"
                if "rate_limit" in str(e).lower():
                    print_warning(f"Rate Limit Hit (attempt {attempt + 1}): {e}")
                    if attempt < retries:
                        time.sleep(random.uniform(5, 10))  # Longer wait for rate limits
                        continue
                elif "invalid" in str(e).lower() and "model" in str(e).lower():
                    print_error(f"Invalid Model Error: {e}")
                    print_error(f"Model used: {self.model_name}")
                    print_info("Check OpenAI documentation for current valid models")
                    print_info("https://platform.openai.com/docs/models")
                    return False, last_error, time.time() - start_time
                elif "authentication" in str(e).lower() or "api_key" in str(e).lower():
                    print_error(f"Authentication Error: {e}")
                    print_info("Tip: Check your OPENAI_API_KEY environment variables")
                    return False, last_error, time.time() - start_time
                else:
                    print_error(f"API Error (attempt {attempt + 1}): {e}")
                
                if attempt == retries:
                    print_error(f"Final API Error: {last_error}")
                    return False, last_error, time.time() - start_time
            
            if attempt < retries:
                wait_time = random.uniform(1, 3) * (attempt + 1)  # Exponential backoff
                time.sleep(wait_time)
        
        return False, last_error or "Unknown error after all retries", time.time() - start_time
    
    def process_section_task(self, task: SectionTask) -> bool:
        """Process a single section task (outline or content) with detailed error reporting"""
        # Get best available API key
        client, key_name, key_index, actual_key = self._get_best_api_key()
        
        # Log section started
        if self.logging_manager:
            event = ProcessingEvent(
                event_type='section_started',
                file_id=task.file_id,
                data={
                    'section_number': task.section_number,
                    'section_name': task.section_name,
                    'chapter_name': task.chapter_name,
                    'stage': task.stage,
                    'api_key': key_name
                }
            )
            self.logging_manager.log_event(event)
        
        try:
            start_time = time.time()
            
            if task.stage == 'outline':
                # Generate outline
                prompt = self._generate_outline_prompt(
                    task.chapter_name,
                    task.chapter_name,
                    task.section_name,
                    task.section_data.get('generated_section_content_md', '')
                )
                
                success, result, response_time = self._call_openai_api(
                    client, prompt, "json", retries=3, temperature=0.5
                )
                
                if success:
                    task.section_data['section_outline_response'] = result
                else:
                    print_error(f"Outline failed for {task.section_number}: {result}")
                
            elif task.stage == 'content':
                # Generate content
                outline = task.section_data.get('section_outline_response')
                if not outline or isinstance(outline, dict) and outline.get('error'):
                    success, result = False, "No valid outline available"
                    response_time = 0
                    print_error(f"Content failed for {task.section_number}: {result}")
                else:
                    prompt = self._generate_content_prompt(
                        task.chapter_name,
                        task.chapter_name,
                        task.section_name,
                        outline
                    )
                    
                    success, result, response_time = self._call_openai_api(
                        client, prompt, "text", retries=3, temperature=0.7
                    )
                    
                    if success:
                        task.section_data['enhanced_section_content_md'] = result
                    else:
                        print_error(f"Content failed for {task.section_number}: {result}")
            
            processing_time = time.time() - start_time
            
            # Release API key
            self._release_api_key(key_name, success, response_time)
            
            # Log API usage
            if self.logging_manager:
                usage_event = ProcessingEvent(
                    event_type='api_usage',
                    file_id=task.file_id,
                    data={
                        'api_key': key_name,
                        'section_number': task.section_number,
                        'stage': task.stage,
                        'success': success,
                        'response_time': response_time,
                        'error': result if not success else None
                    }
                )
                self.logging_manager.log_event(usage_event)
            
            # Log section completion
            if self.logging_manager:
                if success:
                    event = ProcessingEvent(
                        event_type='section_completed',
                        file_id=task.file_id,
                        data={
                            'section_number': task.section_number,
                            'stage': task.stage,
                            'processing_time': processing_time
                        }
                    )
                else:
                    event = ProcessingEvent(
                        event_type='section_failed',
                        file_id=task.file_id,
                        data={
                            'section_number': task.section_number,
                            'stage': task.stage,
                            'error': str(result)
                        }
                    )
                self.logging_manager.log_event(event)
            
            return success
            
        except Exception as e:
            error_msg = f"Exception in process_section_task: {type(e).__name__}: {str(e)}"
            print_error(f"Critical error for {task.section_number}: {error_msg}")
            
            # Release API key on exception
            self._release_api_key(key_name, False)
            
            # Log failure
            if self.logging_manager:
                event = ProcessingEvent(
                    event_type='section_failed',
                    file_id=task.file_id,
                    data={
                        'section_number': task.section_number,
                        'stage': task.stage,
                        'error': error_msg
                    }
                )
                self.logging_manager.log_event(event)
            
            return False
    
    def process_file_stages(self, file_id: int, file_path: str, json_data: List[Dict], 
                           max_workers: int = 4) -> Tuple[bool, bool]:
        """Process both outline and content stages for a file"""
        
        # Log file started
        if self.logging_manager:
            event = ProcessingEvent(
                event_type='file_started',
                file_id=file_id,
                data={'file_path': file_path}
            )
            self.logging_manager.log_event(event)
        
        # Filter sections with content
        valid_sections = [s for s in json_data if s.get('generated_section_content_md', '').strip()]
        
        # Stage 1: Outline Generation
        outline_success = self._process_stage(
            file_id, file_path, valid_sections, 'outline', max_workers
        )
        
        if not outline_success:
            return False, False
        
        # Stage 2: Content Generation
        content_success = self._process_stage(
            file_id, file_path, valid_sections, 'content', max_workers
        )
        
        return outline_success, content_success
    
    def _process_stage(self, file_id: int, file_path: str, sections: List[Dict], 
                      stage: str, max_workers: int) -> bool:
        """Process a single stage (outline or content) for all sections"""
        
        print_section(f"Starting {stage} stage for {Path(file_path).name}")
        
        # Get already processed sections
        if self.logging_manager:
            processed_sections = self.logging_manager.get_processed_sections(file_id, stage)
        else:
            processed_sections = set()
        
        # Create tasks for unprocessed sections
        tasks = []
        for section in sections:
            section_number = section.get('section_number')
            if not section_number or section_number in processed_sections:
                continue
            
            # For content stage, only process sections with valid outlines
            if stage == 'content':
                outline = section.get('section_outline_response')
                if not outline or (isinstance(outline, dict) and outline.get('error')):
                    continue
            
            task = SectionTask(
                task_id="",
                file_id=file_id,
                file_path=file_path,
                section_number=section_number,
                section_name=section.get('section_name', ''),
                chapter_name=section.get('chapter_name', ''),
                stage=stage,
                section_data=section
            )
            tasks.append(task)
        
        if not tasks:
            print_success(f"All sections already processed for {stage} stage")
            return True
        
        print_info(f"Processing {len(tasks)} sections with {max_workers} workers")
        
        # Process tasks in parallel
        successful_tasks = 0
        failed_tasks = 0
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_task = {
                executor.submit(self.process_section_task, task): task 
                for task in tasks
            }
            
            # Collect results
            for future in concurrent.futures.as_completed(future_to_task):
                task = future_to_task[future]
                try:
                    success = future.result()
                    if success:
                        successful_tasks += 1
                        print_success(f"{stage.title()}: {task.section_number}")
                    else:
                        failed_tasks += 1
                        print_error(f"{stage.title()}: {task.section_number}")
                        
                except Exception as e:
                    failed_tasks += 1
                    print_error(f"Exception in {stage}: {task.section_number} - {e}")
        
        # Log stage completion
        if self.logging_manager:
            stage_status = 'completed' if failed_tasks == 0 else 'partial'
            event = ProcessingEvent(
                event_type='stage_completed',
                file_id=file_id,
                data={
                    'stage': stage,
                    'status': stage_status,
                    'success_count': successful_tasks,
                    'failure_count': failed_tasks
                }
            )
            self.logging_manager.log_event(event)
        
        print_info(f"{stage.title()} stage: {successful_tasks} successful, {failed_tasks} failed")
        return failed_tasks == 0
    
    def get_api_usage_summary(self) -> Dict:
        """Get comprehensive API usage summary"""
        with self.lock:
            summary = {
                'total_keys': len(self.api_keys),
                'key_stats': {}
            }
            
            total_requests = 0
            total_errors = 0
            
            for key_name, stats in self.api_stats.items():
                summary['key_stats'][key_name] = {
                    'total_requests': stats.total_requests,
                    'successful_requests': stats.successful_requests,
                    'failed_requests': stats.failed_requests,
                    'success_rate': stats.success_rate,
                    'average_response_time': stats.average_response_time,
                    'active_requests': stats.active_requests
                }
                total_requests += stats.total_requests
                total_errors += stats.failed_requests
            
            summary['total_requests'] = total_requests
            summary['total_errors'] = total_errors
            summary['overall_success_rate'] = ((total_requests - total_errors) / total_requests * 100) if total_requests > 0 else 100
            
            return summary

# === Utility Functions ===
def load_json_file(file_path: str) -> Optional[List[Dict]]:
    """Load and parse JSON file, expecting a list of dictionaries."""
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
    """Save data (list of dicts) to a JSON file."""
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        temp_file_path = Path(file_path).with_suffix(f"{Path(file_path).suffix}.tmp")
        with open(temp_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        os.replace(temp_file_path, file_path)
    except Exception as e:
        print_error(f"Could not save JSON file: {file_path}\n{e}")

def save_text_file(content: str, file_path: str):
    """Save text content to a file with error handling."""
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        temp_file_path = Path(file_path).with_suffix(f"{Path(file_path).suffix}.tmp")
        with open(temp_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        os.replace(temp_file_path, file_path)
    except Exception as e:
        print_error(f"Could not save text file: {file_path}\n{e}")

def discover_json_files(folder_path: Path) -> List[Path]:
    """Discover JSON files in the input folder"""
    try:
        json_files = list(folder_path.glob("*.json"))
        return sorted(json_files)
    except Exception as e:
        print_error(f"Error discovering files: {e}")
        return []

# === Main Content Processing System ===
class DualManagerContentSystem:
    """Main content processing system with dual manager architecture"""
    
    def __init__(self, input_folder: str, output_folder: str, model_name: str = "gpt-5-mini", max_workers: int = None):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.model_name = model_name
        
        # Initialize database logging manager
        db_path = self.output_folder / "dual_manager_processing.db"
        self.logging_manager = DatabaseLoggingManager(db_path)
        
        # Initialize API processing manager
        self.api_manager = APIProcessingManager(model_name, self.logging_manager)
        
        # Set max workers
        self.max_workers = max_workers or min(len(self.api_manager.api_keys) * 2, 8)
        
        print_success("Dual Manager System initialized")
        print_info(f"Max workers: {self.max_workers}")
    
    def show_startup_info(self):
        """Display startup information without API test"""
        print_header("Dual Manager Content Generation System")
        
        print(f"Model: {self.model_name}")
        print(f"API Keys: {len(self.api_manager.api_keys)}")
        print(f"Max Workers: {self.max_workers}")
        print(f"Input Folder: {self.input_folder}")
        print(f"Output Folder: {self.output_folder}")
        print(f"Database: {self.output_folder / 'dual_manager_processing.db'}")
        
        print_success("System ready to start processing")
        return True
    
    def show_error_diagnostics(self):
        """Show diagnostic information when errors occur"""
        print_section("Error Diagnostics")
        print(f"Model being used: {self.model_name}")
        print(f"Number of API keys: {len(self.api_manager.api_keys)}")
        
        print_info("Common Solutions:")
        print(f"1. Check model name: '{self.model_name}' - verify it exists in OpenAI docs")
        print("2. Visit: https://platform.openai.com/docs/models")
        print("3. Verify API keys are set: echo $OPENAI_API_KEY")
        print("4. Check rate limits: Wait 60 seconds and try again")
        print("5. Reduce workers: --workers 2")
        print("6. Check account billing: Ensure OpenAI account has credits")
    
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
            if not self.logging_manager.should_process_file(str(file_path)):
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
        """Process a single JSON file through both stages"""
        
        filename = file_path.name
        file_stem = file_path.stem
        
        # Setup output paths
        stage1_output_path = self.output_folder / f"outlined_{file_stem}.json"
        stage2_output_path = self.output_folder / f"enhanced_{file_stem}.json"
        final_article_path = self.output_folder / f"final_article_{file_stem}.md"
        
        # Load and validate input data
        input_data = load_json_file(str(file_path))
        if not input_data:
            print_error(f"Failed to load {filename}")
            return False
        
        # Count valid sections
        valid_sections = [s for s in input_data if s.get("generated_section_content_md", "").strip()]
        if not valid_sections:
            print_warning(f"No valid sections found in {filename}")
            return False
        
        # Register file with logging manager
        file_id = self.logging_manager.register_file(
            str(file_path.resolve()),
            filename,
            len(valid_sections),
            str(stage1_output_path),
            str(stage2_output_path),
            str(final_article_path)
        )
        
        print_section(f"Processing file: {filename} (ID: {file_id})")
        print_info(f"Found {len(valid_sections)} sections to process")
        
        try:
            # Process both stages through API manager
            outline_success, content_success = self.api_manager.process_file_stages(
                file_id, str(file_path), input_data, self.max_workers
            )
            
            if outline_success and content_success:
                # Save outputs
                save_json_file(input_data, str(stage1_output_path))
                save_json_file(input_data, str(stage2_output_path))
                
                # Assemble final article
                print_info("Assembling final article...")
                enhanced_sections = [s.get('enhanced_section_content_md', '') 
                                   for s in input_data 
                                   if s.get('enhanced_section_content_md')]
                final_article = "\n\n---\n\n".join(enhanced_sections)
                save_text_file(final_article, str(final_article_path))
                
                # Log file completion
                event = ProcessingEvent(
                    event_type='file_completed',
                    file_id=file_id,
                    data={'status': 'completed'}
                )
                self.logging_manager.log_event(event)
                
                print_success(f"Successfully completed {filename}")
                return True
            else:
                # Log file failure
                event = ProcessingEvent(
                    event_type='file_completed',
                    file_id=file_id,
                    data={'status': 'failed'}
                )
                self.logging_manager.log_event(event)
                
                print_error(f"Failed to complete {filename}")
                return False
                
        except Exception as e:
            print_error(f"Error processing {filename}: {e}")
            
            # Log file failure
            event = ProcessingEvent(
                event_type='file_completed',
                file_id=file_id,
                data={'status': 'failed'}
            )
            self.logging_manager.log_event(event)
            return False
    
    def show_final_summary(self):
        """Display final processing summary"""
        # Get API usage summary
        api_summary = self.api_manager.get_api_usage_summary()
        processing_stats = self.logging_manager.get_processing_stats()
        
        print_header("Final Processing Summary")
        
        # API Usage Summary
        print_section("API Usage Summary")
        for key_name, stats in api_summary['key_stats'].items():
            print(f"{key_name:8} | Requests: {stats['total_requests']:4} | "
                  f"Success: {stats['successful_requests']:4} | "
                  f"Failed: {stats['failed_requests']:3} | "
                  f"Rate: {stats['success_rate']:5.1f}% | "
                  f"Avg Time: {stats['average_response_time']:5.2f}s")
        
        print_section("Processing Summary")
        print(f"Files Processed: {processing_stats['files_processed']}")
        print(f"Files Failed: {processing_stats['files_failed']}")
        print(f"Sections Processed: {processing_stats['sections_processed']}")
        print(f"Sections Failed: {processing_stats['sections_failed']}")
        print(f"Total API Calls: {api_summary['total_requests']}")
        print(f"Overall Success Rate: {api_summary['overall_success_rate']:.1f}%")
        print(f"Output Directory: {self.output_folder}")
    
    def process_all_files(self, force_rerun: bool = False) -> bool:
        """Process all files in the input folder"""
        
        # Show startup info (no API test)
        if not self.show_startup_info():
            return False
        
        # Discover and validate files
        valid_files = self.discover_and_validate_files()
        if not valid_files:
            return False
        
        # Start batch session
        batch_id = self.logging_manager.start_batch_session(
            str(self.input_folder),
            str(self.output_folder),
            len(valid_files)
        )
        
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
                        # Show diagnostics for failed files
                        if failed_files == 1:  # Only show once per batch
                            self.show_error_diagnostics()
                        
                except KeyboardInterrupt:
                    print_warning("Process interrupted by user")
                    return False
                    
                except Exception as e:
                    print_error(f"Critical error processing {file_path.name}: {e}")
                    failed_files += 1
                    continue
            
            # Show final summary
            self.show_final_summary()
            
            return failed_files == 0
            
        finally:
            # Ensure logging manager is properly closed
            self.logging_manager.close()

# === Main Entry Point ===
def main():
    """Main entry point"""
    load_dotenv()
    
    parser = argparse.ArgumentParser(
        description='Dual Manager Content Generation System for Wikipedia JSON files - SIMPLE OUTPUT',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python script.py /path/to/json/folder
  python script.py /path/to/json/folder --model gpt-5-mini
  python script.py /path/to/json/folder --workers 4
  python script.py /path/to/json/folder --force-rerun

Environment Variables:
  OPENAI_API_KEY      - Primary API key  
  OPENAI_API_KEY_1    - Additional API key 1
  OPENAI_API_KEY_2    - Additional API key 2
  ... and so on (no limit)

Features:
  - Enhanced error reporting and diagnostics
  - Intelligent load balancing across multiple API keys
  - Perfect resume functionality with detailed logging
  - Two-stage processing: Outline Generation → Content Enhancement
  - Simple Python output (no Rich library dependencies)

Common Issues & Solutions:
  1. Invalid Model: Use 'gpt-5-mini' or 'gpt-4o' instead of custom models
  2. Rate Limits: Reduce --workers or wait between runs
  3. API Keys: Ensure OPENAI_API_KEY environment variables are set
  4. Authentication: Check OpenAI account has sufficient credits
        """
    )
    
    parser.add_argument('input_folder', help='Path to folder containing Wikipedia JSON files')
    parser.add_argument('--output-folder', help='Output folder (default: input_folder/results)')
    parser.add_argument('--model', default='gpt-5-mini', help='OpenAI model to use (default: gpt-5-mini)')
    parser.add_argument('--workers', type=int, help='Maximum number of parallel workers (default: API keys * 2)')
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
        system = DualManagerContentSystem(
            input_folder=str(input_folder),
            output_folder=output_folder,
            model_name=args.model,
            max_workers=args.workers
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