# -*- coding: utf-8 -*-
"""
Combined Script: Stage 1 (Outline Generation) & Stage 2 (Content Generation) V9
- OpenAI ONLY VERSION - ADAPTED FOR CENTRAL SECRETARIAT JSON INPUT

Processes a flattened, structured JSON file where each item is a section.
Stage 1: Generates detailed outlines (JSON) using OpenAI API
Stage 2: Generates detailed article prose (Markdown) based on outlines
Uses SQLite for robust stage/item status tracking.
"""
import json
import os
import argparse
import time
import random
import gc
from typing import Dict, List, Any, Optional
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
import sys
import traceback
import re
import sqlite3
import copy

from openai import OpenAI

# --- Rich library integration (optional) ---
try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
    rich_available = True
except ImportError:
    rich_available = False
    class SimpleConsole:
        def print(self, message, **kwargs):
            message = re.sub(r'\x1b\[[0-9;]*[mK]', '', str(message))
            message = re.sub(r'\[(bold|italic|cyan|green|yellow|red|grey).*?\]', '', message)
            message = re.sub(r'\[/.*?\]', '', message)
            print(message)
        def status(self, message):
            class DummyContext:
                def __enter__(self): 
                    print(f"... {message}")
                def __exit__(self, exc_type, exc_val, exc_tb): 
                    pass
            return DummyContext()
    
    class SimpleProgress:
        def __init__(self, console=None, transient=True):
            self.console = console or SimpleConsole()
            self.task_counter = 0
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def add_task(self, description, total=100, completed=0):
            self.task_counter += 1
            self.console.print(f"Starting: {description} (Total: {total}, Completed: {completed})")
            return self.task_counter
        def update(self, task_id, advance=1, description=None):
            if description:
                self.console.print(f"Progress: {description}")

console = Console() if rich_available else SimpleConsole()
Progress = Progress if rich_available else SimpleProgress

# === NEW HELPER: Extracts a topic from filename ===
def extract_topic_from_filename(filename: Path) -> str:
    """Cleans a filename to extract a human-readable topic."""
    stem = filename.stem.lower()
    # Remove common prefixes and suffixes
    stem = stem.replace('economy_of_', '').replace('economy of ', '')
    stem = stem.replace('report_on_', '').replace('report on ', '')
    stem = stem.replace('chapter_', '').replace('chapter-', '')
    # Replace separators with spaces and capitalize
    topic = stem.replace('_', ' ').replace('-', ' ').strip()
    return topic.title()

# === Database Helper Functions ===
def init_db(db_path: Path) -> sqlite3.Connection:
    """Initializes the SQLite database and creates tables if they don't exist."""
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Files (
            file_id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_input_path TEXT UNIQUE NOT NULL,
            stage1_output_json_path TEXT NOT NULL,
            stage2_output_json_path TEXT NOT NULL,
            final_article_path TEXT NOT NULL,
            total_processable_units_stage1 INTEGER,
            total_processable_units_stage2 INTEGER,
            added_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Stages (
            stage_id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id INTEGER NOT NULL,
            stage_name TEXT NOT NULL CHECK(stage_name IN ('outline', 'content')),
            status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'running', 'completed', 'failed')),
            last_run_timestamp TIMESTAMP,
            run_details TEXT,
            FOREIGN KEY (file_id) REFERENCES Files (file_id),
            UNIQUE (file_id, stage_name)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ProcessedItems (
            item_log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_id INTEGER NOT NULL,
            stage_name TEXT NOT NULL CHECK(stage_name IN ('outline', 'content')),
            item_key TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('processed', 'failed', 'skipped_empty')),
            processed_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (file_id) REFERENCES Files (file_id),
            UNIQUE (file_id, stage_name, item_key)
        )
    ''')
    conn.commit()
    return conn

def get_or_create_file_record(conn: sqlite3.Connection, original_path: str, stage1_path: str, stage2_path: str, final_path: str) -> int:
    """Gets the file_id for the original path, creating records if needed."""
    cursor = conn.cursor()
    cursor.execute("SELECT file_id FROM Files WHERE original_input_path = ?", (original_path,))
    result = cursor.fetchone()
    if result:
        return result["file_id"]
    else:
        cursor.execute("""
            INSERT INTO Files (original_input_path, stage1_output_json_path, stage2_output_json_path, final_article_path)
            VALUES (?, ?, ?, ?)
        """, (original_path, stage1_path, stage2_path, final_path))
        file_id = cursor.lastrowid
        cursor.execute("INSERT OR IGNORE INTO Stages (file_id, stage_name, status) VALUES (?, ?, ?)", (file_id, 'outline', 'pending'))
        cursor.execute("INSERT OR IGNORE INTO Stages (file_id, stage_name, status) VALUES (?, ?, ?)", (file_id, 'content', 'pending'))
        conn.commit()
        console.print(f"DB: Added new file record for: {Path(original_path).name} (ID: {file_id})")
        return file_id

def update_total_processable_units(conn: sqlite3.Connection, file_id: int, stage_name: str, total_units: int):
    """Updates the total processable unit count for a file and stage if not already set."""
    cursor = conn.cursor()
    column_name = "total_processable_units_stage1" if stage_name == "outline" else "total_processable_units_stage2"
    cursor.execute(f"UPDATE Files SET {column_name} = ? WHERE file_id = ? AND {column_name} IS NULL", (total_units, file_id))
    if cursor.rowcount > 0:
        console.print(f"DB: Set total {stage_name} units to {total_units} for file ID {file_id}")
        conn.commit()

def get_stage_status(conn: sqlite3.Connection, file_id: int, stage_name: str) -> str:
    """Gets the current status of a specific stage for a file."""
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM Stages WHERE file_id = ? AND stage_name = ?", (file_id, stage_name))
    result = cursor.fetchone()
    return result["status"] if result else 'pending'

def update_stage_status(conn: sqlite3.Connection, file_id: int, stage_name: str, status: str, details: Optional[str] = None):
    """Updates the status and timestamp of a specific stage for a file."""
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    cursor.execute("""
        UPDATE Stages
        SET status = ?, last_run_timestamp = ?, run_details = ?
        WHERE file_id = ? AND stage_name = ?
    """, (status, timestamp, details, file_id, stage_name))
    conn.commit()

def get_processed_items(conn: sqlite3.Connection, file_id: int, stage_name: str) -> set:
    """Gets the set of item_keys that have been successfully processed or skipped for a stage."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT item_key FROM ProcessedItems
        WHERE file_id = ? AND stage_name = ? AND status IN ('processed', 'skipped_empty')
    """, (file_id, stage_name))
    return {row["item_key"] for row in cursor.fetchall()}

def log_processed_item(conn: sqlite3.Connection, file_id: int, stage_name: str, item_key: str, status: str):
    """Logs the status of a processed item (INSERT OR REPLACE)."""
    cursor = conn.cursor()
    timestamp = datetime.now().isoformat()
    cursor.execute("""
        INSERT OR REPLACE INTO ProcessedItems (file_id, stage_name, item_key, status, processed_timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (file_id, stage_name, item_key, status, timestamp))
    conn.commit()

def get_file_paths(conn: sqlite3.Connection, file_id: int) -> Optional[Dict]:
    """Retrieves paths associated with a file_id."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT original_input_path, stage1_output_json_path, stage2_output_json_path, final_article_path,
               total_processable_units_stage1, total_processable_units_stage2
        FROM Files WHERE file_id = ?
        """, (file_id,))
    result = cursor.fetchone()
    return dict(result) if result else None

# === Utility Functions ===
def load_json_file(file_path: str) -> Optional[List[Dict]]:
    """Load and parse JSON file, expecting a list of dictionaries."""
    if not Path(file_path).is_file():
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                console.print(f"Error: Input file {file_path} is not a JSON list of objects.")
                return None
            return data
    except json.JSONDecodeError as e:
        console.print(f"Error: Invalid JSON in file: {file_path}\n{e}")
    except Exception as e:
        console.print(f"Error: Could not load JSON file: {file_path}\n{e}")
        console.print(traceback.format_exc())
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
        console.print(f"Error: Could not save JSON file: {file_path}\n{e}")

def save_text_file(content: str, file_path: str):
    """Save text content to a file with error handling."""
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        temp_file_path = Path(file_path).with_suffix(f"{Path(file_path).suffix}.tmp")
        with open(temp_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        os.replace(temp_file_path, file_path)
    except Exception as e:
        console.print(f"Error: Could not save text file: {file_path}\n{e}")

def fix_json_string(json_str: str) -> str:
    """Attempts to fix common issues in JSON strings from LLM outputs."""
    if not json_str or not json_str.strip():
        return '{}'
    json_str = re.sub(r'^```(?:json)?\s*\n?', '', json_str, flags=re.MULTILINE)
    json_str = re.sub(r'\n?```\s*$', '', json_str, flags=re.MULTILINE)
    json_str = json_str.strip()
    start_brace = json_str.find('{')
    end_brace = json_str.rfind('}')
    if start_brace != -1 and end_brace != -1 and start_brace < end_brace:
        json_str = json_str[start_brace : end_brace + 1]
    json_str = re.sub(r',\s*([\}\]])', r'\1', json_str)
    return json_str.strip()

# === OpenAI API Functions ===
def call_openai_api_for_json(prompt: str, api_key: str, model_name: str, retry_count: int, temperature: float) -> Optional[Dict]:
    """Call OpenAI API and return parsed JSON response."""
    client = OpenAI(api_key=api_key)
    
    for attempt in range(retry_count + 1):
        try:
            # Handle gpt-5-mini specific requirements
            if "gpt-5" in model_name:
                completion_params = {
                    "model": model_name,
                    "messages": [
                        {"role": "developer", "content": "You are an expert analyst. Always respond with valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    # gpt-5-mini only supports temperature=1.0 (default)
                }
            else:
                completion_params = {
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": "You are an expert analyst. Always respond with valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": temperature,
                    "max_completion_tokens": 8192
                }
            
            response = client.chat.completions.create(**completion_params)
            
            if response.choices[0].message.content:
                fixed_json = fix_json_string(response.choices[0].message.content)
                return json.loads(fixed_json)
            else:
                console.print(f"Warning: Empty response from OpenAI (attempt {attempt + 1})")
                
        except json.JSONDecodeError as e:
            console.print(f"JSON parsing error (attempt {attempt + 1}): {e}")
            if attempt == retry_count:
                return {"error": f"JSON parsing failed after {retry_count + 1} attempts"}
                
        except Exception as e:
            console.print(f"OpenAI API error (attempt {attempt + 1}): {e}")
            if attempt == retry_count:
                return {"error": f"API call failed: {str(e)}"}
                
        if attempt < retry_count:
            time.sleep(random.uniform(1, 3))
    
    return {"error": "Failed after all retry attempts"}

def call_openai_api_for_text(prompt: str, api_key: str, model_name: str, retry_count: int, temperature: float) -> str:
    """Call OpenAI API and return text response."""
    client = OpenAI(api_key=api_key)
    
    for attempt in range(retry_count + 1):
        try:
            # Handle gpt-5-mini specific requirements
            if "gpt-5" in model_name:
                completion_params = {
                    "model": model_name,
                    "messages": [
                        {"role": "developer", "content": "You are an expert writer and analyst."},
                        {"role": "user", "content": prompt}
                    ],
                    # gpt-5-mini only supports temperature=1.0 (default)
                }
            else:
                completion_params = {
                    "model": model_name,
                    "messages": [
                        {"role": "system", "content": "You are an expert writer and analyst."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": temperature,
                    "max_completion_tokens": 8192
                }
            
            response = client.chat.completions.create(**completion_params)
            
            if response.choices[0].message.content:
                return response.choices[0].message.content.strip()
            else:
                console.print(f"Warning: Empty response from OpenAI (attempt {attempt + 1})")
                
        except Exception as e:
            console.print(f"OpenAI API error (attempt {attempt + 1}): {e}")
            if attempt == retry_count:
                return f"[ERROR: OpenAI API failed after {retry_count + 1} attempts: {str(e)}]"
                
        if attempt < retry_count:
            time.sleep(random.uniform(1, 3))
    
    return "[ERROR: Failed after all retry attempts]"

# === Prompt Generators ===
def generate_outline_prompt(
    topic: str,
    chapter_name: str,
    current_section_name: str,
    section_content_for_prompt: str,
    previous_outlines_summary: str
) -> str:
    """Generates prompt for STAGE 1 with comprehensive analysis for administrative topics."""
    summary_prefix = ""
    if previous_outlines_summary:
        summary_prefix = f"Context from Previously Analyzed Sections:\n{previous_outlines_summary}\n"

    prompt = f"""
# Expert Persona

You are a distinguished expert on Public Administration and Government Systems, specializing in {topic}. You have decades of experience analyzing administrative structures, government processes, and bureaucratic systems from both theoretical and practical perspectives.

# Your Analytical Framework

As an expert in Public Administration, you understand that:
- Administrative systems are built on hierarchical structures and defined processes
- Government organizations operate through formal rules, procedures, and protocols
- Administrative efficiency depends on clear roles, responsibilities, and accountability
- Historical development shapes current administrative practices
- Analysis should identify both structural elements and functional relationships

# Current Analysis Task

Document Subject: {topic}
Current Chapter: {chapter_name}
Section Being Analyzed: {current_section_name}

{summary_prefix}

# Content for Deep Administrative Analysis

--- START OF TEXT TO ANALYZE ---
{section_content_for_prompt}
--- END OF TEXT TO ANALYZE ---

# Your Expert Analysis Task

Breakdown the text comprehensively. Tell me what it is discussing, the key concepts behind the text, what administrative elements are being talked about, and what insights are being conveyed. Focus on:

- Administrative structures and hierarchies described
- Government processes and procedures outlined
- Historical development and evolution mentioned
- Key roles, responsibilities, and functions
- Organizational relationships and reporting structures
- Policy implications and administrative significance
- Tables, charts, and structured data interpretation

Provide a detailed analysis that captures all aspects of the administrative content.

```json
{{
  "section_analysis": {{
    "section_title": "Descriptive title for this section",
    "main_themes": ["Theme 1", "Theme 2", "Theme 3"],
    "key_concepts": ["Concept A", "Concept B"],
    "administrative_focus": "Primary administrative aspect covered",
    "scope": "What this section covers"
  }},
  "content_breakdown": {{
    "key_points": [
      {{
        "point": "Main argument or fact",
        "supporting_details": "Supporting information",
        "significance": "Why this matters administratively"
      }}
    ],
    "structures_and_hierarchies": {{
      "organizational_elements": "Any organizational structures described",
      "hierarchy_details": "Hierarchy information if present",
      "roles_and_responsibilities": "Key roles and responsibilities mentioned"
    }},
    "processes_and_procedures": {{
      "administrative_processes": "Key processes described",
      "procedural_requirements": "Important procedures outlined",
      "operational_mechanisms": "How things work in practice"
    }},
    "data_interpretation": {{
      "tables_charts_analysis": "Interpretation of any tables or structured data",
      "quantitative_insights": "Key numbers and their administrative meaning",
      "patterns_trends": "Observable patterns in the administrative information"
    }}
  }},
  "contextual_connections": {{
    "historical_context": "Historical background or administrative development",
    "broader_significance": "Role in the larger administrative system",
    "practical_implications": "Real-world applications and administrative importance"
  }},
  "professor_summary": "Concise academic summary for continuity with next sections"
}}
```
"""
    return prompt.strip()

def generate_writing_prompt(
    topic: str,
    chapter_name: str,
    section_name: str,
    section_outline_json: Dict,
    previous_content_summary: str,
    original_section_content: str
) -> str:
    """Generates prompt for STAGE 2 focused on writing based on the detailed outline."""
    try:
        outline_json_str = json.dumps(section_outline_json, indent=2, ensure_ascii=False)
    except Exception as e:
        console.print(f"Warning: Could not serialize outline for writing prompt: {e}")
        outline_json_str = '{"error": "Outline data could not be serialized for prompt."}'

    summary_prefix_content = ""
    if previous_content_summary:
        summary_prefix_content = f"Context from Previously Written Sections:\n{previous_content_summary}\n"

    prompt = f"""
# Expert Author Persona

You are a distinguished expert and author specializing in Public Administration and Government Systems, particularly in {topic}. You are writing a comprehensive academic book that analyzes administrative structures, government processes, and bureaucratic systems. Your writing style is scholarly yet accessible, combining deep analytical insight with clear exposition suitable for students, practitioners, and researchers.

# Your Writing Approach

Your expertise allows you to:
- Analyze administrative systems through both theoretical and practical lenses
- Connect historical development to contemporary administrative practices
- Examine the interplay between organizational structure and functional efficiency
- Identify patterns of administrative evolution and reform
- Contextualize administrative decisions within broader governance frameworks
- Explain complex bureaucratic processes in clear, understandable terms

# Current Writing Context

Document Subject: {topic}
Current Chapter: {chapter_name}
Current Section: {section_name}

{summary_prefix_content}

# Your Expert Analysis (Outline) to Transform into Content

{outline_json_str}

# Your Writing Task

Transform the above outline into detailed, well-structured Markdown content that forms part of an academic book on Public Administration. Your task is to:

1. **Expand comprehensively**: Convert every aspect of the outline into detailed prose
2. **Maintain academic rigor**: Use scholarly language while keeping it accessible
3. **Structure logically**: Organize information in a clear, logical flow
4. **Provide context**: Explain the significance of administrative elements
5. **Include examples**: Where appropriate, illustrate concepts with practical examples
6. **Connect ideas**: Show relationships between different administrative elements

Write the content as a complete section of a book, without introduction or conclusion paragraphs (as this is part of a larger work). Focus on:
- Clear explanations of administrative structures and hierarchies
- Detailed coverage of processes and procedures
- Historical context and development
- Practical implications and real-world applications
- Proper interpretation of any data or organizational charts

The writing should be suitable for an academic audience studying Public Administration and Government Systems.

"""
    return prompt.strip()

# === Memory Trail Formatters ===
def format_outline_memory_trail(previous_sections_context: List[Dict]) -> str:
    """This function creates a summary of previously processed outlines to give context."""
    if not previous_sections_context: 
        return ""
    summary_lines = ["Previously Outlined Sections & Summaries:"]
    for outline in previous_sections_context[-5:]:
        title = outline.get("section_analysis", {}).get("section_title", "Untitled")
        summary = outline.get("professor_summary", "No summary.")
        summary_lines.append(f"- Title: {title}\n  Summary: {summary[:150]}...")
    return "\n".join(summary_lines)

def format_content_memory_trail(previous_content_summary_trail: List[Dict]) -> str:
    """This function creates a summary of previously written content to give context."""
    if not previous_content_summary_trail: 
        return ""
    summary_lines = []
    for item_data in previous_content_summary_trail[-3:]:
        title = item_data.get('section_analysis', {}).get('section_title', "Untitled")
        summary = item_data.get('professor_summary', 'N/A')
        summary_lines.append(f"- Preceding Section Title: {title}\n  Summary: {summary[:150]}...")
    return "\n".join(summary_lines)

# === Stage Functions ===
def run_outline_generation_stage(
    db_connection: sqlite3.Connection,
    file_id: int,
    topic: str,
    api_key: str,
    model_name: str,
    retries: int
) -> bool:
    stage_name = "outline"
    console.print(f"\n{'='*10} Starting Stage 1: Outline Generation (File ID: {file_id}) {'='*10}")
    update_stage_status(db_connection, file_id, stage_name, 'running')

    file_paths = get_file_paths(db_connection, file_id)
    if not file_paths:
        console.print(f"Error: Could not retrieve file paths for file ID {file_id}.")
        update_stage_status(db_connection, file_id, stage_name, 'failed', 'DB path retrieval failed')
        return False

    stage1_output_path = file_paths["stage1_output_json_path"]
    in_memory_data = load_json_file(stage1_output_path) or load_json_file(file_paths['original_input_path'])

    if not in_memory_data:
        console.print("Exiting Stage 1: Failed to load original or intermediate input JSON.")
        update_stage_status(db_connection, file_id, stage_name, 'failed', 'Input load failed')
        return False

    sections_to_process = [s for s in in_memory_data if s.get("text", "").strip()]
    total_sections_eligible = len(sections_to_process)
    console.print(f"Found {total_sections_eligible} sections with content to process.")
    update_total_processable_units(db_connection, file_id, stage_name, total_sections_eligible)

    processed_section_keys = get_processed_items(db_connection, file_id, stage_name)
    console.print(f"Found {len(processed_section_keys)} sections already outlined in DB.")

    # Chapter tracking logic for Central Secretariat structure
    current_chapter_name_tracker = None
    current_chapter_accumulated_content = []
    previous_outlines_for_memory = []

    try:
        with Progress(console=console, transient=True) as progress:
            task = progress.add_task("Stage 1: Outlining...", total=total_sections_eligible, completed=len(processed_section_keys))
            for section_obj in in_memory_data:
                item_key = section_obj.get("section_number")
                if not item_key or not section_obj.get("text", "").strip():
                    continue

                if item_key in processed_section_keys:
                    if 'section_outline_response' in section_obj:
                        previous_outlines_for_memory.append(section_obj['section_outline_response'])
                    continue

                progress.update(task, description=f"Outlining Section: {item_key} ('{section_obj.get('section_name', '')[:30]}...')")

                # Chapter tracking for Central Secretariat structure
                current_chapter_name = section_obj.get("chapter_name")
                if current_chapter_name != current_chapter_name_tracker:
                    console.print(f"\nSwitching to Chapter '{current_chapter_name}'. Resetting chapter context.")
                    current_chapter_accumulated_content = []
                    current_chapter_name_tracker = current_chapter_name

                prompt_input_content = section_obj.get("text", "")
                if current_chapter_accumulated_content:
                    previous_sections_str = "\n\n".join(current_chapter_accumulated_content)
                    prompt_input_content = f"{previous_sections_str}\n\n--- START OF CURRENT SECTION TO ANALYZE ---\n\n{prompt_input_content}"

                outline_memory_trail = format_outline_memory_trail(previous_outlines_for_memory)

                prompt = generate_outline_prompt(
                    topic,
                    section_obj.get("chapter_name", ""),
                    section_obj.get("section_name", ""),
                    prompt_input_content,
                    outline_memory_trail
                )

                outline_response = call_openai_api_for_json(prompt, api_key, model_name, retries, 0.5)

                section_obj['section_outline_response'] = outline_response
                status_for_db = 'processed' if not (isinstance(outline_response, dict) and outline_response.get("error")) else 'failed'
                log_processed_item(db_connection, file_id, stage_name, item_key, status_for_db)

                if status_for_db == 'processed':
                    previous_outlines_for_memory.append(outline_response)
                    current_chapter_accumulated_content.append(section_obj.get("text", ""))

                save_json_file(in_memory_data, stage1_output_path)
                progress.update(task, advance=1)
                time.sleep(random.uniform(0.5, 1.0))
                gc.collect()

    except Exception as e:
        console.print(f"\nUNHANDLED Error in Stage 1: {e}")
        traceback.print_exc()
        update_stage_status(db_connection, file_id, stage_name, 'failed', str(e))
        return False
    finally:
        save_json_file(in_memory_data, stage1_output_path)
        final_processed_count = len(get_processed_items(db_connection, file_id, stage_name))
        is_complete = final_processed_count >= total_sections_eligible
        update_stage_status(db_connection, file_id, stage_name, 'completed' if is_complete else 'failed')
        console.print(f"Stage 1 Finished {'Successfully' if is_complete else 'with Errors/Incomplete'}!")
    return is_complete

def run_content_generation_stage(
    db_connection: sqlite3.Connection,
    file_id: int,
    topic: str,
    api_key: str,
    model_name: str,
    retries: int
) -> bool:
    stage_name = "content"
    console.print(f"\n{'='*10} Starting Stage 2: Content Generation (File ID: {file_id}) {'='*10}")
    update_stage_status(db_connection, file_id, stage_name, 'running')

    file_paths = get_file_paths(db_connection, file_id)
    if not file_paths:
        console.print(f"Error: Could not retrieve file paths for file ID {file_id}.")
        update_stage_status(db_connection, file_id, stage_name, 'failed', 'DB path retrieval failed')
        return False

    stage1_input_path = file_paths["stage1_output_json_path"]
    stage2_output_path = file_paths["stage2_output_json_path"]
    final_article_path = file_paths["final_article_path"]

    outlined_data = load_json_file(stage1_input_path)
    if not outlined_data:
        console.print("Exiting Stage 2: Failed to load Stage 1 output JSON.")
        update_stage_status(db_connection, file_id, stage_name, 'failed', 'Stage 1 output not found')
        return False

    in_memory_data = load_json_file(stage2_output_path) or copy.deepcopy(outlined_data)

    sections_to_process = [s for s in in_memory_data if s.get("section_outline_response") and not s.get("section_outline_response", {}).get("error")]
    total_sections_eligible = len(sections_to_process)
    console.print(f"Found {total_sections_eligible} sections with valid outlines.")
    update_total_processable_units(db_connection, file_id, stage_name, total_sections_eligible)

    processed_content_keys = get_processed_items(db_connection, file_id, stage_name)
    console.print(f"Found {len(processed_content_keys)} sections with generated content in DB.")

    previous_outlines_for_memory = []

    try:
        with Progress(console=console, transient=True) as progress:
            task = progress.add_task("Stage 2: Writing...", total=total_sections_eligible, completed=len(processed_content_keys))
            for section_obj in in_memory_data:
                item_key = section_obj.get("section_number")
                outline = section_obj.get("section_outline_response")

                if not item_key or item_key in processed_content_keys or not outline or outline.get("error"):
                    if outline and not outline.get("error"):
                        previous_outlines_for_memory.append(outline)
                    continue

                progress.update(task, description=f"Writing Content for: {item_key} ('{section_obj.get('section_name', '')[:30]}...')")

                content_memory_trail = format_content_memory_trail(previous_outlines_for_memory)

                prompt = generate_writing_prompt(
                    topic,
                    section_obj.get("chapter_name", ""),
                    section_obj.get("section_name", ""),
                    outline,
                    content_memory_trail,
                    section_obj.get("text", "")
                )

                generated_prose = call_openai_api_for_text(prompt, api_key, model_name, retries, 0.7)

                section_obj['generated_section_content_md'] = generated_prose
                status_for_db = 'processed' if "[ERROR:" not in generated_prose else 'failed'
                log_processed_item(db_connection, file_id, stage_name, item_key, status_for_db)

                if status_for_db == 'processed':
                    previous_outlines_for_memory.append(outline)

                save_json_file(in_memory_data, stage2_output_path)
                progress.update(task, advance=1)
                time.sleep(random.uniform(0.6, 1.2))
                gc.collect()

    except Exception as e:
        console.print(f"\nUNHANDLED Error in Stage 2: {e}")
        traceback.print_exc()
        update_stage_status(db_connection, file_id, stage_name, 'failed', str(e))
        return False
    finally:
        save_json_file(in_memory_data, stage2_output_path)
        console.print("Assembling final Markdown article...")
        final_article_pieces = [s.get('generated_section_content_md', '') for s in in_memory_data if s.get('generated_section_content_md')]
        final_md = "\n\n---\n\n".join(final_article_pieces)
        save_text_file(final_md, final_article_path)
        console.print(f"Final article assembled and saved to: {final_article_path}")

        final_processed_count = len(get_processed_items(db_connection, file_id, stage_name))
        is_complete = final_processed_count >= total_sections_eligible
        update_stage_status(db_connection, file_id, stage_name, 'completed' if is_complete else 'failed')
        console.print(f"Stage 2 Finished {'Successfully' if is_complete else 'with Errors/Incomplete'}!")
    return is_complete

# === Main Execution ===
def main():
    start_time = time.monotonic()
    console.print("="*40)
    console.print("=== OpenAI Content Generation Pipeline (Central Secretariat) ===")
    load_dotenv()

    parser = argparse.ArgumentParser(description='Generate outlines and content using OpenAI API for Central Secretariat JSON structure.')
    parser.add_argument('--input_file', type=str, required=True, help='Path to the Central Secretariat JSON file.')
    parser.add_argument('--output_dir', type=str, default='results_openai_central_secretariat', help='Directory for all outputs.')
    parser.add_argument('--final_article_filename', type=str, default='final_central_secretariat_guide.md', help='Filename for the final Markdown article.')
    parser.add_argument('--stage', type=str, default='all', choices=['all', 'outline', 'content'], help='Specify which stage(s) to run.')
    parser.add_argument('--force_rerun_content', action='store_true', help='Force Stage 2 to run even if completed.')
    parser.add_argument('--api_key', type=str, default=os.environ.get('OPENAI_API_KEY'), help='OpenAI API Key.')
    parser.add_argument('--outline_model', type=str, default='gpt-4o-mini', help='Model for outlining.')
    parser.add_argument('--content_model', type=str, default='gpt-4o-mini', help='Model for content generation.')
    parser.add_argument('--outline_retries', type=int, default=5, help='Retries for outline API calls.')
    parser.add_argument('--content_retries', type=int, default=3, help='Retries for content API calls.')
    args = parser.parse_args()

    # Validate API key
    if not args.api_key:
        console.print("Fatal Error: OpenAI API Key missing.")
        sys.exit(1)

    # Extract topic from filename
    input_file_path = Path(args.input_file)
    topic = extract_topic_from_filename(input_file_path)
    console.print(f"Detected topic: {topic}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    db_path = output_dir / "pipeline_status_openai.db"
    db_conn = None

    try:
        db_conn = init_db(db_path)

        original_input_abs_path = str(input_file_path.resolve())
        original_stem = input_file_path.stem

        stage1_path = str((output_dir / f"outlined_{original_stem}.json").resolve())
        stage2_path = str((output_dir / f"content_{original_stem}.json").resolve())
        final_path = str((output_dir / args.final_article_filename).resolve())

        file_id = get_or_create_file_record(db_conn, original_input_abs_path, stage1_path, stage2_path, final_path)

        outline_status = get_stage_status(db_conn, file_id, 'outline')
        content_status = get_stage_status(db_conn, file_id, 'content')

        console.print(f"DB Status: Outline='{outline_status}', Content='{content_status}' for File ID {file_id}")

        run_stage1 = (args.stage in ['all', 'outline']) and (outline_status != 'completed')
        run_stage2 = (args.stage in ['all', 'content'])

        if run_stage1:
            stage1_success = run_outline_generation_stage(db_conn, file_id, topic, args.api_key, args.outline_model, args.outline_retries)
            if not stage1_success:
                console.print("Stage 1 failed. Halting process.")
                sys.exit(1)
            # Re-fetch outline status after potential completion of Stage 1
            outline_status = get_stage_status(db_conn, file_id, 'outline')

        if run_stage2:
            if outline_status != 'completed':
                console.print("Cannot run Stage 2 because Stage 1 is not complete.")
            elif content_status == 'completed' and not args.force_rerun_content:
                console.print("Content stage is already complete. Use --force_rerun_content to override.")
            else:
                run_content_generation_stage(db_conn, file_id, topic, args.api_key, args.content_model, args.content_retries)

    except Exception as e:
        console.print(f"\nA fatal error occurred in the main execution block:")
        console.print(traceback.format_exc())
    finally:
        if db_conn:
            db_conn.close()
        console.print(f"\nTotal execution time: {time.monotonic() - start_time:.2f} seconds.")
        console.print("="*40)

if __name__ == "__main__":
    main()