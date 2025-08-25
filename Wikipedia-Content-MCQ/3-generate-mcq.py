#!/usr/bin/env python3
"""
Per-File Dynamic Cluster MCQ Generator - Improved Strategy
Calculates cluster size per file based on total bullet points, then clusters section-by-section
Enhanced logging and progress tracking for the new cluster strategy
"""

import json
import os
import sys
import time
import logging
import random
import concurrent.futures
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime
import argparse
from dataclasses import dataclass, asdict
from openai import OpenAI
from dotenv import load_dotenv
import threading

# Rich library for better console output (optional)
try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
    from rich.table import Table
    from rich.panel import Panel
    from rich.logging import RichHandler
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    class SimpleConsole:
        def print(self, text, **kwargs):
            print(text)
    console = SimpleConsole()
    RICH_AVAILABLE = False

@dataclass
class FileAnalysis:
    """Analysis of a single file's bullet point distribution"""
    file_path: Path
    total_bullet_points: int
    sections_count: int
    cluster_size: int
    estimated_clusters: int
    estimated_questions: int
    sections_info: List[Dict] = None

    def __post_init__(self):
        if self.sections_info is None:
            self.sections_info = []

@dataclass
class SectionCompletion:
    """Track completion status of a specific chapter-section"""
    chapter_name: str
    section_number: str
    section_name: str
    total_bullets: int
    completed_bullets: List[int]
    missing_bullets: List[int]
    completion_percentage: float

    def is_complete(self) -> bool:
        return len(self.missing_bullets) == 0

@dataclass
class ProcessingStats:
    """Enhanced statistics for tracking MCQ generation progress"""
    total_files: int = 0
    completed_files: int = 0
    total_sections: int = 0
    completed_sections: int = 0
    total_bullet_points: int = 0
    completed_bullet_points: int = 0
    remaining_bullet_points: int = 0
    failed_bullet_points: int = 0
    total_clusters_processed: int = 0
    total_questions_generated: int = 0
    start_time: Optional[str] = None
    api_keys_used: int = 0
    cluster_size_distribution: Dict[int, int] = None

    def __post_init__(self):
        if self.cluster_size_distribution is None:
            self.cluster_size_distribution = {}

@dataclass
class BulletPointClusterTask:
    """Represents a cluster of bullet points to process together"""
    file_path: Path
    chapter_name: str
    section_number: str
    section_name: str
    section_index: int
    bullet_point_cluster: List[Tuple[int, str]]  # [(index, text), (index, text), ...]
    cluster_size: int
    cluster_id: str = ""

    def __post_init__(self):
        indices = [str(bp[0]) for bp in self.bullet_point_cluster]
        self.cluster_id = f"{self.chapter_name}_{self.section_number}_cluster_{'_'.join(indices)}"

    @property
    def actual_cluster_size(self) -> int:
        return len(self.bullet_point_cluster)

class EnhancedAPIKeyManager:
    """Enhanced API key manager with better load balancing and monitoring"""
    
    def __init__(self, model_name: str = "gpt-5-mini"):
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

class PerFileClusterMCQGenerator:
    """
    Per-file dynamic cluster MCQ generator with enhanced logging
    Calculates cluster size based on total bullet points per file, clusters section-by-section
    """
    
    def __init__(self, folder_path: str, model_name: str = "gpt-5-mini", max_workers: int = None):
        self.folder_path = Path(folder_path)
        self.model_name = model_name
        
        # Initialize enhanced API manager
        try:
            self.api_manager = EnhancedAPIKeyManager(model_name)
            self.max_workers = max_workers or min(len(self.api_manager.api_keys) * 2, 8)
        except Exception as e:
            console.print(f"[red]✗ API Initialization Failed: {e}[/red]")
            sys.exit(1)
        
        # Setup directories
        self.output_dir = self.folder_path.parent / "question_bank"
        self.logs_dir = self.output_dir / "logs"
        self.backups_dir = self.output_dir / "backups"
        
        for dir_path in [self.output_dir, self.logs_dir, self.backups_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)
        
        # Setup enhanced logging
        self.setup_enhanced_logging()
        
        # Initialize statistics
        self.stats = ProcessingStats()
        self.stats.api_keys_used = len(self.api_manager.api_keys)
        self.stats.start_time = datetime.now().isoformat()
        
        # Thread-safe data structures
        self.data_lock = threading.Lock()
        
    def setup_enhanced_logging(self):
        """Setup enhanced logging with detailed file and cluster tracking"""
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        self.logger = logging.getLogger('PerFileClusterMCQGen')
        self.logger.setLevel(logging.INFO)
        self.logger.handlers.clear()
        
        # Detailed file handler
        file_handler = logging.FileHandler(self.logs_dir / 'per_file_cluster_generation.log')
        file_handler.setFormatter(logging.Formatter(log_format))
        file_handler.setLevel(logging.DEBUG)
        
        # Cluster analysis handler
        cluster_handler = logging.FileHandler(self.logs_dir / 'cluster_analysis.log')
        cluster_handler.setFormatter(logging.Formatter(log_format))
        cluster_handler.setLevel(logging.INFO)
        
        # Console handler for errors only
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
        console_handler.setLevel(logging.ERROR)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(cluster_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.info("Enhanced per-file cluster logging system initialized")
    
    def calculate_cluster_size_for_file(self, total_bullet_points: int) -> int:
        """Calculate optimal cluster size based on total bullet points in file"""
        if total_bullet_points < 40:
            return 3
        elif total_bullet_points <= 100:
            return 5
        else:
            return 7
    
    def analyze_file_structure(self, file_path: Path) -> Optional[FileAnalysis]:
        """Analyze file structure and determine optimal cluster strategy"""
        try:
            data = self.load_json_file(file_path)
            if not data:
                return None
            
            total_bullets = 0
            sections_info = []
            
            for section_index, section in enumerate(data):
                chapter_name = section.get('chapter_name', 'Unknown Chapter')
                section_number = section.get('section_number', f'section_{section_index}')
                section_name = section.get('section_name', 'Untitled Section')
                bullet_points = section.get('bullet_points', [])
                
                section_bullets = len(bullet_points)
                total_bullets += section_bullets
                
                sections_info.append({
                    'index': section_index,
                    'chapter_name': chapter_name,
                    'section_number': section_number,
                    'section_name': section_name,
                    'bullet_count': section_bullets
                })
            
            # Calculate cluster size for this file
            cluster_size = self.calculate_cluster_size_for_file(total_bullets)
            estimated_clusters = (total_bullets + cluster_size - 1) // cluster_size  # Ceiling division
            estimated_questions = estimated_clusters * 5
            
            analysis = FileAnalysis(
                file_path=file_path,
                total_bullet_points=total_bullets,
                sections_count=len(data),
                cluster_size=cluster_size,
                estimated_clusters=estimated_clusters,
                estimated_questions=estimated_questions,
                sections_info=sections_info
            )
            
            # Log detailed analysis
            self.logger.info(f"FILE ANALYSIS: {file_path.name}")
            self.logger.info(f"  Total bullets: {total_bullets}")
            self.logger.info(f"  Sections: {len(data)}")
            self.logger.info(f"  Calculated cluster size: {cluster_size}")
            self.logger.info(f"  Estimated clusters: {estimated_clusters}")
            self.logger.info(f"  Estimated questions: {estimated_questions}")
            
            return analysis
            
        except Exception as e:
            self.logger.error(f"Failed to analyze file structure for {file_path}: {e}")
            return None
    
    def validate_questions(self, questions: List[Dict]) -> bool:
        """Validate that questions are complete and properly formatted"""
        if not questions or len(questions) == 0:
            return False
        
        for question in questions:
            # Check required fields exist
            required_fields = ['question', 'options', 'correct', 'explanations']
            if not all(field in question for field in required_fields):
                return False
            
            # Check options count
            if not isinstance(question['options'], list) or len(question['options']) != 4:
                return False
            
            # Check correct index is valid
            if not isinstance(question['correct'], int) or not (0 <= question['correct'] <= 3):
                return False
            
            # Check explanations exist for all options
            if not isinstance(question['explanations'], dict) or len(question['explanations']) != 4:
                return False
            
            # Check no empty strings
            if not question['question'].strip():
                return False
            
            if any(not str(opt).strip() for opt in question['options']):
                return False
            
            # Check all explanation keys exist
            if not all(str(i) in question['explanations'] for i in range(4)):
                return False
        
        return True
    
    def create_section_clusters(self, missing_bullets: List[int], bullet_points: List[str], cluster_size: int) -> List[List[Tuple[int, str]]]:
        """
        Group missing bullet points into clusters using the file's determined cluster size
        """
        clusters = []
        
        for i in range(0, len(missing_bullets), cluster_size):
            cluster_indices = missing_bullets[i:i + cluster_size]
            cluster_content = []
            
            for idx in cluster_indices:
                if idx < len(bullet_points) and isinstance(bullet_points[idx], str):
                    bullet_text = bullet_points[idx].strip()
                    # Clean up bullet point text - remove leading bullet symbols
                    if bullet_text.startswith('• '):
                        bullet_text = bullet_text[2:].strip()
                    elif bullet_text.startswith('- '):
                        bullet_text = bullet_text[2:].strip()
                    elif bullet_text.startswith('* '):
                        bullet_text = bullet_text[2:].strip()
                    
                    if len(bullet_text) >= 20:  # Only include substantial bullet points
                        cluster_content.append((idx, bullet_text))
            
            if cluster_content:  # Only add non-empty clusters
                clusters.append(cluster_content)
        
        return clusters
    
    def analyze_section_completion(self, original_data: List[Dict], question_file_path: Path) -> Dict[str, SectionCompletion]:
        """
        Analyze completion status for each chapter-section combination
        """
        completion_map = {}
        
        # Scan original file to establish baseline
        for section_index, section in enumerate(original_data):
            chapter_name = section.get('chapter_name', 'Unknown Chapter')
            section_number = section.get('section_number', f'section_{section_index}')
            section_name = section.get('section_name', 'Untitled Section')
            bullet_points = section.get('bullet_points', [])
            
            # Create unique key for this chapter-section
            section_key = f"{chapter_name}_{section_number}"
            total_bullets = len(bullet_points)
            
            completion_map[section_key] = SectionCompletion(
                chapter_name=chapter_name,
                section_number=section_number,
                section_name=section_name,
                total_bullets=total_bullets,
                completed_bullets=[],
                missing_bullets=list(range(total_bullets)),
                completion_percentage=0.0
            )
        
        # Scan existing question file (if exists)
        if question_file_path.exists():
            try:
                with open(question_file_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                
                existing_sections = existing_data.get('sections', [])
                for section in existing_sections:
                    chapter_name = section.get('chapter_name', 'Unknown Chapter')
                    section_number = section.get('section_number', 'unknown')
                    section_key = f"{chapter_name}_{section_number}"
                    
                    if section_key in completion_map:
                        # Check which bullet points have valid questions
                        bullet_points = section.get('bullet_points', [])
                        for bp in bullet_points:
                            bp_index = bp.get('bullet_point_index', -1)
                            questions = bp.get('questions', [])
                            
                            # Validate questions are complete and valid
                            if bp_index >= 0 and self.validate_questions(questions):
                                if bp_index in completion_map[section_key].missing_bullets:
                                    completion_map[section_key].completed_bullets.append(bp_index)
                                    completion_map[section_key].missing_bullets.remove(bp_index)
                        
                        # Update completion percentage
                        total = completion_map[section_key].total_bullets
                        completed = len(completion_map[section_key].completed_bullets)
                        completion_map[section_key].completion_percentage = (completed / total * 100) if total > 0 else 0
                
            except Exception as e:
                self.logger.error(f"Failed to analyze existing question file {question_file_path}: {e}")
        
        return completion_map
    
    def create_cluster_tasks_for_file(self, file_analysis: FileAnalysis, completion_map: Dict[str, SectionCompletion]) -> List[BulletPointClusterTask]:
        """Create cluster tasks for a file using per-file cluster size, section-by-section"""
        tasks = []
        
        # Load file data
        original_data = self.load_json_file(file_analysis.file_path)
        if not original_data:
            return tasks
        
        # Use the file's determined cluster size for ALL sections in this file
        cluster_size = file_analysis.cluster_size
        
        self.logger.info(f"CREATING CLUSTERS for {file_analysis.file_path.name}: cluster_size={cluster_size}")
        
        # Process each section with the file's cluster size
        for section_index, section in enumerate(original_data):
            chapter_name = section.get('chapter_name', 'Unknown Chapter')
            section_number = section.get('section_number', f'section_{section_index}')
            section_name = section.get('section_name', 'Untitled Section')
            section_key = f"{chapter_name}_{section_number}"
            
            if section_key in completion_map:
                missing_bullets = completion_map[section_key].missing_bullets
                bullet_points = section.get('bullet_points', [])
                
                if missing_bullets:
                    # Create clusters from missing bullet points using file's cluster size
                    clusters = self.create_section_clusters(missing_bullets, bullet_points, cluster_size)
                    
                    self.logger.info(f"  SECTION {section_key}: {len(missing_bullets)} missing bullets → {len(clusters)} clusters")
                    
                    for cluster_idx, cluster in enumerate(clusters):
                        if cluster:  # Only create task if cluster has content
                            task = BulletPointClusterTask(
                                file_path=file_analysis.file_path,
                                chapter_name=chapter_name,
                                section_number=section_number,
                                section_name=section_name,
                                section_index=section_index,
                                bullet_point_cluster=cluster,
                                cluster_size=cluster_size
                            )
                            tasks.append(task)
                            
                            self.logger.debug(f"    Cluster {cluster_idx + 1}: {len(cluster)} bullets, IDs: {[bp[0] for bp in cluster]}")
        
        return tasks
    
    def discover_json_files(self) -> List[Path]:
        """Discover JSON files with bullet points in the input folder"""
        try:
            json_files = []
            for json_file in self.folder_path.glob("*.json"):
                # Quick check if file contains bullet_points structure
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Check if it's a list with sections containing bullet_points
                    if isinstance(data, list) and len(data) > 0:
                        sample_section = data[0]
                        if isinstance(sample_section, dict) and 'bullet_points' in sample_section:
                            json_files.append(json_file)
                except:
                    continue  # Skip files that can't be parsed
            
            self.stats.total_files = len(json_files)
            return sorted(json_files)
        except Exception as e:
            self.logger.error(f"Failed to discover JSON files: {e}")
            return []
    
    def load_json_file(self, file_path: Path) -> Optional[List[Dict]]:
        """Load and validate JSON file structure"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Expect direct list structure from first code
            if isinstance(data, list):
                return data
            else:
                self.logger.error(f"Invalid JSON structure in {file_path}: expected list")
                return None
                
        except Exception as e:
            self.logger.error(f"Error reading {file_path}: {e}")
            return None
    
    def show_file_analyses(self, file_analyses: List[FileAnalysis]):
        """Display detailed file analysis with cluster size distribution"""
        if not file_analyses:
            return
        
        # Calculate distribution
        cluster_size_counts = {}
        total_bullets = 0
        total_estimated_questions = 0
        
        for analysis in file_analyses:
            size = analysis.cluster_size
            cluster_size_counts[size] = cluster_size_counts.get(size, 0) + 1
            total_bullets += analysis.total_bullet_points
            total_estimated_questions += analysis.estimated_questions
            
            # Update stats
            self.stats.cluster_size_distribution[size] = self.stats.cluster_size_distribution.get(size, 0) + 1
        
        if RICH_AVAILABLE:
            # Create detailed table
            table = Table(title="Per-File Cluster Size Analysis")
            table.add_column("File", style="cyan")
            table.add_column("Bullets", style="green", justify="right")
            table.add_column("Sections", style="blue", justify="right")
            table.add_column("Cluster Size", style="magenta", justify="center")
            table.add_column("Est. Clusters", style="yellow", justify="right")
            table.add_column("Est. Questions", style="red", justify="right")
            
            for analysis in file_analyses:
                table.add_row(
                    analysis.file_path.name[:30] + ("..." if len(analysis.file_path.name) > 30 else ""),
                    str(analysis.total_bullet_points),
                    str(analysis.sections_count),
                    str(analysis.cluster_size),
                    str(analysis.estimated_clusters),
                    str(analysis.estimated_questions)
                )
            
            console.print(table)
            
            # Summary panel
            summary_panel = Panel.fit(
                f"[bold]Per-File Dynamic Cluster Analysis[/bold]\n\n"
                f"[green]Total Files:[/green] {len(file_analyses)}\n"
                f"[green]Total Bullet Points:[/green] {total_bullets}\n"
                f"[yellow]Cluster Size Distribution:[/yellow]\n"
                + "\n".join([f"  Size {size}: {count} files" for size, count in sorted(cluster_size_counts.items())]) +
                f"\n\n[cyan]Estimated Total Questions:[/cyan] {total_estimated_questions}",
                title="Strategy Overview",
                border_style="blue"
            )
            console.print(summary_panel)
        else:
            print("\n" + "="*80)
            print("Per-File Cluster Size Analysis")
            print("="*80)
            print(f"{'File':<35} {'Bullets':<8} {'Sections':<8} {'Size':<6} {'Clusters':<9} {'Questions'}")
            print("-"*80)
            
            for analysis in file_analyses:
                print(f"{analysis.file_path.name[:34]:<35} {analysis.total_bullet_points:<8} "
                      f"{analysis.sections_count:<8} {analysis.cluster_size:<6} "
                      f"{analysis.estimated_clusters:<9} {analysis.estimated_questions}")
            
            print(f"\nTotal Files: {len(file_analyses)}")
            print(f"Total Bullet Points: {total_bullets}")
            print("Cluster Size Distribution:")
            for size, count in sorted(cluster_size_counts.items()):
                print(f"  Size {size}: {count} files")
            print(f"Estimated Total Questions: {total_estimated_questions}")
            print("="*80)
    
    def randomize_question_options(self, question_data: Dict) -> Dict:
        """Randomly shuffle options and update correct index and explanations"""
        try:
            options = question_data['options'].copy()
            explanations = question_data['explanations'].copy()
            correct_index = question_data['correct']
            
            # Create shuffled indices
            indices = list(range(4))
            random.shuffle(indices)
            
            # Rearrange options and explanations
            new_options = [options[i] for i in indices]
            new_explanations = {}
            for new_pos, old_pos in enumerate(indices):
                new_explanations[str(new_pos)] = explanations[str(old_pos)]
            
            # Find new position of correct answer
            new_correct_index = indices.index(correct_index)
            
            return {
                'question': question_data['question'],
                'options': new_options,
                'correct': new_correct_index,
                'explanations': new_explanations
            }
            
        except Exception as e:
            return question_data
    
    def format_bullet_cluster(self, cluster: List[Tuple[int, str]]) -> str:
        """Format bullet point cluster for the API prompt"""
        formatted_points = []
        for i, (bp_index, bp_text) in enumerate(cluster, 1):
            formatted_points.append(f"BULLET POINT {i} (Index {bp_index}): {bp_text}")
        
        return "\n\n".join(formatted_points)
    
    def call_openai_api(self, task: BulletPointClusterTask) -> Tuple[Optional[List[Dict]], str]:
        """Call OpenAI API to generate UPSC-style MCQ questions for a cluster"""
        
        system_message = """You are an expert question setter for UPSC Civil Services Examination and other prestigious government competitive exams in India. You specialize in creating analytical, application-based multiple-choice questions that test deep understanding and critical thinking across related topics."""
        
        actual_cluster_size = len(task.bullet_point_cluster)
        
        user_prompt = f"""Context Information:
CHAPTER: {task.chapter_name}
SECTION: {task.section_name} (Section {task.section_number})

BULLET POINTS CLUSTER:
{self.format_bullet_cluster(task.bullet_point_cluster)}

Create exactly 5 high-quality UPSC-style multiple-choice questions based on the {actual_cluster_size} bullet points above.

CRITICAL REQUIREMENTS:

1. CLUSTER PROCESSING:
   - Generate exactly 5 questions total for the entire cluster
   - Draw insights from ALL bullet points in the cluster
   - Create questions that synthesize information across bullet points
   - Ensure questions complement each other and cover different aspects

2. QUESTION DISTRIBUTION:
   - Questions should cover the breadth of topics in the cluster
   - Each question can focus on one bullet point OR combine multiple bullet points
   - Prioritize analytical and application-based questions over factual recall

3. UPSC EXAMINATION PATTERN:
   - Test analytical ability, logical reasoning, and application of concepts
   - Create scenario-based questions requiring synthesis of the knowledge
   - Avoid direct factual recall questions

4. QUESTION TYPES (vary across the 5 questions), any questions can be of anytype, up to you. 
   - Analytical reasoning and cause-effect relationships
   - Application scenarios and policy implications  
   - Comparative analysis across the bullet points
   - Conceptual understanding and synthesis
   - Critical evaluation of concepts or policies

5. OPTION QUALITY:
   - All 4 options must be plausible and well-researched
   - Distractors based on common misconceptions or closely related concepts
   - Options should require careful analysis to distinguish correct from incorrect
   - Avoid obviously wrong options

6. EXPLANATION QUALITY:
   - Comprehensive explanations for ALL options
   - Connect explanations back to the original bullet points
   - Include additional context that enhances learning
   - Reference specific bullet points when relevant

Return ONLY a JSON structure with this exact format:
{{
  "questions": [
    {{
      "question": "question text here",
      "options": ["option A", "option B", "option C", "option D"],
      "correct": 0,
      "explanations": {{
        "0": "explanation for why option A is correct",
        "1": "explanation for why option B is incorrect",
        "2": "explanation for why option C is incorrect", 
        "3": "explanation for why option D is incorrect"
      }},
      "source_bullet_points": [0, 1]
    }}
  ]
}}

Return ONLY the JSON, no other text:"""

        # Get next available client
        client, key_name, key_index = self.api_manager.get_next_client()
        
        try:
            response = client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_prompt}
                ]
            )
            
            if response.choices and response.choices[0].message:
                content_response = response.choices[0].message.content.strip()
                
                # Parse JSON response
                try:
                    if content_response.startswith('```json'):
                        content_response = content_response.replace('```json', '').replace('```', '').strip()
                    
                    questions_data = json.loads(content_response)
                    
                    if 'questions' in questions_data and isinstance(questions_data['questions'], list):
                        questions = questions_data['questions']
                        
                        # Validate each question and ensure we have exactly 5
                        valid_questions = []
                        for q in questions[:5]:  # Take only first 5 questions
                            if (isinstance(q, dict) and 
                                'question' in q and 'options' in q and 'correct' in q and 'explanations' in q and
                                isinstance(q['options'], list) and len(q['options']) == 4 and
                                isinstance(q['correct'], int) and 0 <= q['correct'] <= 3 and
                                isinstance(q['explanations'], dict) and len(q['explanations']) == 4):
                                valid_questions.append(q)
                        
                        if len(valid_questions) == 5:  # Must have exactly 5 valid questions
                            self.api_manager.release_client(key_name, success=True)
                            return valid_questions, key_name
                    
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name
                    
                except json.JSONDecodeError:
                    self.api_manager.release_client(key_name, success=False)
                    return None, key_name
            
        except Exception as e:
            self.api_manager.release_client(key_name, success=False)
            self.logger.error(f"OpenAI API error with {key_name}: {e}")
            return None, key_name
    
    def process_cluster_task(self, task: BulletPointClusterTask) -> Tuple[bool, List[Dict], str]:
        """Process a cluster task to generate 5 questions for the cluster"""
        
        self.logger.info(f"PROCESSING CLUSTER: {task.cluster_id} - {len(task.bullet_point_cluster)} bullets, target size: {task.cluster_size}")
        
        # Call OpenAI API with retries
        questions = None
        api_key_used = "none"
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                questions, api_key_used = self.call_openai_api(task)
                if questions and len(questions) == 5:
                    break
                else:
                    self.logger.warning(f"Attempt {attempt + 1}/{max_retries}: Invalid response for {task.cluster_id}")
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
            except Exception as e:
                self.logger.warning(f"Attempt {attempt + 1}/{max_retries} failed for {task.cluster_id}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
        
        if not questions or len(questions) != 5:
            self.logger.error(f"FAILED: {task.cluster_id} - Could not generate 5 valid questions")
            self.stats.failed_bullet_points += len(task.bullet_point_cluster)
            return False, [], api_key_used
        
        # Randomize each question's options
        randomized_questions = []
        for question in questions:
            randomized_question = self.randomize_question_options(question)
            randomized_questions.append(randomized_question)
        
        # Create results for each bullet point in the cluster
        cluster_results = []
        questions_per_bullet = 5 / len(task.bullet_point_cluster)  # Distribute questions
        
        # Assign questions to bullet points (simple distribution)
        question_index = 0
        for i, (bp_index, bp_text) in enumerate(task.bullet_point_cluster):
            # Calculate how many questions this bullet point should get
            if i == len(task.bullet_point_cluster) - 1:
                # Last bullet point gets remaining questions
                bullet_questions = randomized_questions[question_index:]
            else:
                # Other bullet points get proportional share
                num_questions = max(1, int(questions_per_bullet * (i + 1)) - question_index)
                bullet_questions = randomized_questions[question_index:question_index + num_questions]
                question_index += num_questions
            
            if bullet_questions:  # Only create result if there are questions
                result = {
                    'bullet_point_index': bp_index,
                    'bullet_point_text': bp_text,
                    'questions': bullet_questions,
                    'generation_metadata': {
                        'generated_timestamp': datetime.now().isoformat(),
                        'openai_model': self.model_name,
                        'questions_count': len(bullet_questions),
                        'bullet_point_length': len(bp_text),
                        'options_randomized': True,
                        'api_key_used': api_key_used,
                        'cluster_id': task.cluster_id,
                        'file_cluster_size': task.cluster_size,
                        'actual_cluster_size': len(task.bullet_point_cluster),
                        'chapter_name': task.chapter_name,
                        'section_number': task.section_number,
                        'processing_method': 'per_file_cluster'
                    }
                }
                cluster_results.append(result)

        # Update stats
        self.stats.completed_bullet_points += len(task.bullet_point_cluster)
        self.stats.total_questions_generated += 5  # Always 5 questions per cluster
        self.stats.total_clusters_processed += 1
        
        self.logger.info(f"SUCCESS: {task.cluster_id} - Generated 5 questions for {len(task.bullet_point_cluster)} bullets")
        
        return True, cluster_results, api_key_used
    
    def create_enhanced_progress_display(self, current: int, total: int, task: BulletPointClusterTask, api_key: str, status: str):
        """Create enhanced progress display showing file cluster strategy"""
        progress_pct = (current / total * 100) if total > 0 else 0
        
        # Truncate long names
        file_short = task.file_path.stem[:20] + "..." if len(task.file_path.stem) > 23 else task.file_path.stem
        chapter_short = task.chapter_name[:15] + "..." if len(task.chapter_name) > 18 else task.chapter_name
        section_short = f"S{task.section_number}"
        cluster_info = f"[{task.actual_cluster_size}/{task.cluster_size}]"  # actual/target
        
        if RICH_AVAILABLE:
            status_color = {
                'success': 'green',
                'failed': 'red',
                'processing': 'blue'
            }.get(status, 'white')
            
            console.print(f"[{status_color}]{status.upper():<9}[/{status_color}] "
                         f"[cyan]{current:3d}/{total:<3d}[/cyan] "
                         f"[magenta]{progress_pct:5.1f}%[/magenta] "
                         f"[white]{file_short:<23}[/white] "
                         f"[blue]{chapter_short:<18}[/blue] "
                         f"[green]{section_short:<8}[/green] "
                         f"[yellow]{cluster_info:<8}[/yellow] "
                         f"[cyan]{api_key}[/cyan]")
        else:
            print(f"{status.upper():<9} {current:3d}/{total:<3d} {progress_pct:5.1f}% "
                  f"{file_short:<23} {chapter_short:<18} {section_short:<8} {cluster_info:<8} {api_key}")
    
    def save_updated_file(self, file_path: Path, new_results: List[Dict], file_analysis: FileAnalysis):
        """Save or update the question file with new cluster results"""
        try:
            output_file = self.output_dir / f"questions_{file_path.stem}.json"
            
            # Load existing data if file exists
            existing_data = {}
            all_sections = []
            
            if output_file.exists():
                with open(output_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                all_sections = existing_data.get('sections', [])
            
            # Organize new results by chapter-section
            new_results_by_section = {}
            for result in new_results:
                metadata = result.get('generation_metadata', {})
                chapter_name = metadata.get('chapter_name', 'Unknown')
                section_number = metadata.get('section_number', 'unknown')
                section_key = f"{chapter_name}_{section_number}"
                
                if section_key not in new_results_by_section:
                    new_results_by_section[section_key] = []
                new_results_by_section[section_key].append(result)
            
            # Update or add sections
            for section_key, new_bullet_points in new_results_by_section.items():
                # Find existing section
                existing_section_index = None
                for i, section in enumerate(all_sections):
                    existing_key = f"{section.get('chapter_name', '')}_{section.get('section_number', '')}"
                    if existing_key == section_key:
                        existing_section_index = i
                        break
                
                if existing_section_index is not None:
                    # Merge bullet points into existing section
                    existing_bullets = all_sections[existing_section_index].get('bullet_points', [])
                    
                    # Add only new bullet points (avoid duplicates)
                    for new_bp in new_bullet_points:
                        bp_index = new_bp.get('bullet_point_index')
                        # Check if already exists
                        exists = any(bp.get('bullet_point_index') == bp_index for bp in existing_bullets)
                        if not exists:
                            existing_bullets.append(new_bp)
                    
                    # Sort by bullet point index
                    existing_bullets.sort(key=lambda x: x.get('bullet_point_index', 0))
                    all_sections[existing_section_index]['bullet_points'] = existing_bullets
                    all_sections[existing_section_index]['total_bullet_points'] = len(existing_bullets)
                else:
                    # Create new section
                    if new_bullet_points:
                        first_bp = new_bullet_points[0]
                        metadata = first_bp.get('generation_metadata', {})
                        
                        new_section = {
                            'chapter_name': metadata.get('chapter_name', 'Unknown Chapter'),
                            'section_name': 'Generated Section',
                            'section_number': metadata.get('section_number', 'unknown'),
                            'source_file': file_path.name,
                            'original_index': len(all_sections),
                            'total_bullet_points': len(new_bullet_points),
                            'bullet_points': sorted(new_bullet_points, key=lambda x: x.get('bullet_point_index', 0))
                        }
                        all_sections.append(new_section)
            
            # Calculate final statistics
            total_sections = len(all_sections)
            total_bullet_points = sum(len(s.get('bullet_points', [])) for s in all_sections)
            total_questions = sum(len(bp.get('questions', [])) for s in all_sections for bp in s.get('bullet_points', []))
            
            # Create completion status
            completion_status = {}
            for section in all_sections:
                chapter_name = section.get('chapter_name', 'Unknown')
                section_number = section.get('section_number', 'unknown')
                section_key = f"{chapter_name}_{section_number}"
                
                bullet_points = section.get('bullet_points', [])
                completed_bullets = [bp.get('bullet_point_index', -1) for bp in bullet_points if bp.get('bullet_point_index', -1) >= 0]
                
                completion_status[section_key] = {
                    'total_bullets': section.get('total_bullet_points', len(bullet_points)),
                    'completed_bullets': sorted(completed_bullets),
                    'completion_percentage': (len(completed_bullets) / max(section.get('total_bullet_points', 1), 1) * 100)
                }
            
            # Create final structure with enhanced metadata
            final_data = {
                'generation_info': {
                    'source_file': file_path.name,
                    'generation_timestamp': datetime.now().isoformat(),
                    'openai_model': self.model_name,
                    'processing_method': 'per_file_cluster',
                    'file_analysis': {
                        'total_bullet_points': file_analysis.total_bullet_points,
                        'calculated_cluster_size': file_analysis.cluster_size,
                        'sections_count': file_analysis.sections_count,
                        'estimated_clusters': file_analysis.estimated_clusters,
                        'estimated_questions': file_analysis.estimated_questions
                    },
                    'questions_per_cluster': 5,
                    'total_sections': total_sections,
                    'total_bullet_points': total_bullet_points,
                    'total_questions_generated': total_questions,
                    'completion_status': completion_status
                },
                'sections': all_sections
            }
            
            # Write atomically using temporary file
            temp_file = output_file.with_suffix('.tmp')
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(final_data, f, indent=2, ensure_ascii=False)
            
            # Atomic rename
            temp_file.rename(output_file)
            
            self.logger.info(f"SAVED: {output_file.name} - {total_questions} questions from {len(new_results)} bullet points")
            
        except Exception as e:
            self.logger.error(f"Failed to save updated file: {e}")
    
    def process_file_with_enhanced_strategy(self, file_analysis: FileAnalysis) -> bool:
        """Process a file using the enhanced per-file cluster strategy"""
        
        self.logger.info(f"PROCESSING FILE: {file_analysis.file_path.name}")
        self.logger.info(f"  Strategy: {file_analysis.total_bullet_points} bullets → cluster size {file_analysis.cluster_size}")
        
        # Load original file
        original_data = self.load_json_file(file_analysis.file_path)
        if original_data is None:
            return False
        
        # Analyze completion status
        question_file_path = self.output_dir / f"questions_{file_analysis.file_path.stem}.json"
        completion_map = self.analyze_section_completion(original_data, question_file_path)
        
        # Create cluster tasks using the enhanced strategy
        cluster_tasks = self.create_cluster_tasks_for_file(file_analysis, completion_map)
        
        if not cluster_tasks:
            if RICH_AVAILABLE:
                console.print(f"[green]✓ {file_analysis.file_path.name}: All bullet points already completed[/green]")
            else:
                print(f"✓ {file_analysis.file_path.name}: All bullet points already completed")
            self.stats.completed_files += 1
            return True
        
        # Calculate total bullet points in clusters
        total_cluster_bullets = sum(len(task.bullet_point_cluster) for task in cluster_tasks)
        
        # Show file processing header
        if RICH_AVAILABLE:
            console.print(f"\n[bold blue]Processing: {file_analysis.file_path.name}[/bold blue]")
            console.print(f"[cyan]Strategy: {file_analysis.total_bullet_points} bullets → cluster size {file_analysis.cluster_size}[/cyan]")
            console.print(f"[yellow]Found {len(cluster_tasks)} clusters with {total_cluster_bullets} bullet points[/yellow]")
            console.print(f"[magenta]Each cluster generates exactly 5 questions[/magenta]")
            console.print("-" * 105)
            console.print(f"{'STATUS':<9} {'PROGRESS':<7} {'%':<6} {'FILE':<23} {'CHAPTER':<18} {'SECT':<8} {'CLSTR':<8} {'API'}")
            console.print("-" * 105)
        else:
            print(f"\nProcessing: {file_analysis.file_path.name}")
            print(f"Strategy: {file_analysis.total_bullet_points} bullets → cluster size {file_analysis.cluster_size}")
            print(f"Found {len(cluster_tasks)} clusters with {total_cluster_bullets} bullet points")
            print(f"Each cluster generates exactly 5 questions")
            print("-" * 105)
            print(f"{'STATUS':<9} {'PROGRESS':<7} {'%':<6} {'FILE':<23} {'CHAPTER':<18} {'SECT':<8} {'CLSTR':<8} {'API'}")
            print("-" * 105)
        
        # Process cluster tasks in parallel
        processed_count = 0
        total_tasks = len(cluster_tasks)
        all_completed_results = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all cluster tasks
            future_to_task = {executor.submit(self.process_cluster_task, task): task for task in cluster_tasks}
            
            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_task):
                task = future_to_task[future]
                try:
                    success, cluster_results, api_key = future.result()
                    processed_count += 1
                    
                    if success:
                        all_completed_results.extend(cluster_results)
                        self.create_enhanced_progress_display(
                            processed_count, total_tasks, task, api_key, 'success'
                        )
                    else:
                        self.create_enhanced_progress_display(
                            processed_count, total_tasks, task, api_key, 'failed'
                        )
                        
                except Exception as e:
                    processed_count += 1
                    self.create_enhanced_progress_display(
                        processed_count, total_tasks, task, 'error', 'failed'
                    )
                    self.logger.error(f"Cluster task failed: {e}")
                
                # Save progress periodically (every 10 clusters)
                if len(all_completed_results) > 0 and processed_count % 10 == 0:
                    self.save_updated_file(file_analysis.file_path, all_completed_results, file_analysis)
        
        # Final save with all results
        if all_completed_results:
            self.save_updated_file(file_analysis.file_path, all_completed_results, file_analysis)
        
        self.stats.completed_files += 1
        return True
    
    def create_master_question_bank(self, processed_files: List[FileAnalysis]):
        """Create master question bank with all questions and enhanced metadata"""
        all_sections = []
        total_questions = 0
        total_clusters = 0
        cluster_size_stats = {}
        
        for file_analysis in processed_files:
            question_file = self.output_dir / f"questions_{file_analysis.file_path.stem}.json"
            if question_file.exists():
                try:
                    with open(question_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    sections = data.get('sections', [])
                    all_sections.extend(sections)
                    
                    # Count questions and track cluster sizes
                    file_questions = 0
                    file_clusters = 0
                    for section in sections:
                        for bp in section.get('bullet_points', []):
                            questions = bp.get('questions', [])
                            file_questions += len(questions)
                            if len(questions) > 0:
                                file_clusters += 1
                    
                    total_questions += file_questions
                    total_clusters += file_clusters
                    
                    # Track cluster size distribution
                    cluster_size = file_analysis.cluster_size
                    cluster_size_stats[cluster_size] = cluster_size_stats.get(cluster_size, 0) + 1
                    
                except Exception as e:
                    self.logger.error(f"Error reading question file {question_file}: {e}")
        
        if all_sections:
            master_data = {
                'master_question_bank_info': {
                    'creation_timestamp': datetime.now().isoformat(),
                    'total_sections': len(all_sections),
                    'total_questions': total_questions,
                    'total_clusters_processed': total_clusters,
                    'processing_method': 'per_file_cluster',
                    'cluster_strategy': {
                        'description': 'Dynamic cluster sizing per file',
                        'rules': {
                            'small_files': '< 40 bullets → cluster size 3',
                            'medium_files': '40-100 bullets → cluster size 5',
                            'large_files': '> 100 bullets → cluster size 7'
                        },
                        'cluster_size_distribution': cluster_size_stats
                    },
                    'questions_per_cluster': 5,
                    'source_folder': str(self.folder_path),
                    'openai_model': self.model_name
                },
                'sections': all_sections
            }
            
            master_file = self.output_dir / "master_question_bank.json"
            with open(master_file, 'w', encoding='utf-8') as f:
                json.dump(master_data, f, indent=2, ensure_ascii=False)
            
            if RICH_AVAILABLE:
                console.print(f"[green]✓ Master question bank created: {total_questions} questions from {total_clusters} clusters[/green]")
            else:
                print(f"✓ Master question bank created: {total_questions} questions from {total_clusters} clusters")
    
    def show_api_usage_summary(self):
        """Display enhanced API usage summary"""
        usage_summary = self.api_manager.get_usage_summary()
        
        if RICH_AVAILABLE:
            console.print("\n" + "="*80)
            console.print("[bold]Enhanced API Usage Summary[/bold]")
            console.print("="*80)
            
            table = Table()
            table.add_column("API Key", style="cyan")
            table.add_column("Clusters", style="green", justify="right")
            table.add_column("Errors", style="red", justify="right")
            table.add_column("Success Rate", style="yellow", justify="right")
            table.add_column("Questions", style="magenta", justify="right")
            
            for i, (key_name, requests) in enumerate(usage_summary['usage_stats'].items()):
                errors = usage_summary['error_counts'][key_name]
                success_rate = ((requests - errors) / requests * 100) if requests > 0 else 0
                est_questions = (requests - errors) * 5
                
                table.add_row(
                    key_name,
                    str(requests),
                    str(errors),
                    f"{success_rate:.1f}%",
                    str(est_questions)
                )
            
            console.print(table)
            
            # Show cluster size distribution
            if self.stats.cluster_size_distribution:
                console.print(f"\n[bold]Cluster Size Distribution:[/bold]")
                for size, count in sorted(self.stats.cluster_size_distribution.items()):
                    console.print(f"  Size {size}: {count} files")
            
            console.print(f"\n[bold]Total Cluster API Calls:[/bold] {usage_summary['total_requests']}")
            console.print(f"[bold]Total Errors:[/bold] {usage_summary['total_errors']}")
            console.print(f"[bold]Total Questions Generated:[/bold] {self.stats.total_questions_generated}")
            console.print("="*80)
        else:
            print("\n" + "="*80)
            print("Enhanced API Usage Summary")
            print("="*80)
            for key_name, requests in usage_summary['usage_stats'].items():
                errors = usage_summary['error_counts'][key_name]
                success_rate = ((requests - errors) / requests * 100) if requests > 0 else 0
                est_questions = (requests - errors) * 5
                print(f"{key_name}: {requests} clusters, {errors} errors, {success_rate:.1f}% success, ~{est_questions} questions")
            
            if self.stats.cluster_size_distribution:
                print("\nCluster Size Distribution:")
                for size, count in sorted(self.stats.cluster_size_distribution.items()):
                    print(f"  Size {size}: {count} files")
            
            print(f"Total Cluster API Calls: {usage_summary['total_requests']}")
            print(f"Total Errors: {usage_summary['total_errors']}")
            print(f"Total Questions Generated: {self.stats.total_questions_generated}")
            print("="*80)
    
    def run_generation(self) -> bool:
        """Main method to run the enhanced per-file cluster MCQ generation process"""
        
        # Show startup info
        if RICH_AVAILABLE:
            startup_panel = Panel.fit(
                f"[bold]Per-File Dynamic Cluster UPSC MCQ Generator[/bold]\n"
                f"Model: [cyan]{self.model_name}[/cyan]\n"
                f"API Keys: [green]{len(self.api_manager.api_keys)}[/green]\n"
                f"Workers: [yellow]{self.max_workers}[/yellow]\n"
                f"Strategy: [magenta]Dynamic cluster sizing per file[/magenta]\n"
                f"Rules: [blue]<40→size 3, 40-100→size 5, >100→size 7[/blue]\n"
                f"Questions per Cluster: [red]5 questions[/red]",
                title="Enhanced Configuration",
                border_style="blue"
            )
            console.print(startup_panel)
        else:
            print("="*70)
            print("Per-File Dynamic Cluster UPSC MCQ Generator")
            print(f"Model: {self.model_name}")
            print(f"API Keys: {len(self.api_manager.api_keys)}")
            print(f"Workers: {self.max_workers}")
            print("Strategy: Dynamic cluster sizing per file")
            print("Rules: <40→size 3, 40-100→size 5, >100→size 7")
            print("Questions per Cluster: 5 questions")
            print("="*70)
        
        # Discover files
        json_files = self.discover_json_files()
        if not json_files:
            if RICH_AVAILABLE:
                console.print("[red]✗ No JSON files with bullet_points found to process[/red]")
            else:
                print("✗ No JSON files with bullet_points found to process")
            return False
        
        # Analyze all files first
        file_analyses = []
        for file_path in json_files:
            analysis = self.analyze_file_structure(file_path)
            if analysis:
                file_analyses.append(analysis)
        
        if not file_analyses:
            if RICH_AVAILABLE:
                console.print("[red]✗ Failed to analyze any files[/red]")
            else:
                print("✗ Failed to analyze any files")
            return False
        
        # Show detailed file analyses
        self.show_file_analyses(file_analyses)
        
        # Process files using enhanced strategy
        processed_files = []
        for file_analysis in file_analyses:
            try:
                if self.process_file_with_enhanced_strategy(file_analysis):
                    processed_files.append(file_analysis)
            except KeyboardInterrupt:
                if RICH_AVAILABLE:
                    console.print("\n[yellow]⚠ Process interrupted. All progress saved automatically.[/yellow]")
                else:
                    print("\n⚠ Process interrupted. All progress saved automatically.")
                return False
            except Exception as e:
                self.logger.error(f"Critical error processing {file_analysis.file_path}: {e}")
                continue
        
        # Create master question bank
        if processed_files:
            if RICH_AVAILABLE:
                console.print("\n[blue]Creating enhanced master question bank...[/blue]")
            else:
                print("\nCreating enhanced master question bank...")
            self.create_master_question_bank(processed_files)
        
        # Show final summaries
        self.show_api_usage_summary()
        self.print_final_summary()
        
        return True
    
    def print_final_summary(self):
        """Print comprehensive final summary with enhanced metrics"""
        if RICH_AVAILABLE:
            summary_panel = Panel.fit(
                f"[bold green]✓ Per-File Dynamic Cluster MCQ Generation Complete[/bold green]\n\n"
                f"[bold]Files Processed:[/bold] {self.stats.completed_files}\n"
                f"[bold]Total Bullet Points:[/bold] {self.stats.completed_bullet_points}\n"
                f"[bold]Clusters Processed:[/bold] {self.stats.total_clusters_processed}\n"
                f"[bold]Questions Generated:[/bold] {self.stats.total_questions_generated}\n"
                f"[bold]Failed Bullet Points:[/bold] {self.stats.failed_bullet_points}\n\n"
                f"[bold]Strategy Efficiency:[/bold]\n"
                f"• Average questions per cluster: 5.0\n"
                f"• Questions per API call: ~5.0\n"
                f"• Adaptive cluster sizing: ✓\n\n"
                f"[bold]Output Location:[/bold] {self.output_dir}",
                title="Final Enhanced Summary",
                border_style="green"
            )
            console.print(summary_panel)
        else:
            print("\n" + "="*70)
            print("✓ Per-File Dynamic Cluster MCQ Generation Complete")
            print("="*70)
            print(f"Files Processed: {self.stats.completed_files}")
            print(f"Total Bullet Points: {self.stats.completed_bullet_points}")
            print(f"Clusters Processed: {self.stats.total_clusters_processed}")
            print(f"Questions Generated: {self.stats.total_questions_generated}")
            print(f"Failed Bullet Points: {self.stats.failed_bullet_points}")
            print("\nStrategy Efficiency:")
            print("• Average questions per cluster: 5.0")
            print("• Questions per API call: ~5.0")
            print("• Adaptive cluster sizing: ✓")
            print(f"\nOutput Location: {self.output_dir}")
            print("="*70)

def main():
    """Main entry point with enhanced argument parsing"""
    load_dotenv()
    
    parser = argparse.ArgumentParser(
        description='Per-File Dynamic Cluster UPSC MCQ Question Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
ENHANCED CLUSTERING STRATEGY:
  The system now uses per-file dynamic cluster sizing based on total bullet points:
  
  Small files  (< 40 bullets):   cluster size 3 → efficient for small datasets
  Medium files (40-100 bullets): cluster size 5 → balanced approach
  Large files  (> 100 bullets):  cluster size 7 → maximum efficiency
  
  Each cluster generates exactly 5 UPSC-style questions.

EXAMPLES:
  # Basic usage - automatic cluster sizing
  python3 enhanced_cluster_mcq.py /path/to/bullet_points/folder
  
  # With custom model
  python3 enhanced_cluster_mcq.py /path/to/folder --model gpt-5-mini
  
  # With custom worker count
  python3 enhanced_cluster_mcq.py /path/to/folder --workers 12

ENVIRONMENT VARIABLES:
  OPENAI_API_KEY      - Primary API key  
  OPENAI_API_KEY_1    - Additional API key 1
  OPENAI_API_KEY_2    - Additional API key 2
  ... and so on (unlimited)

ENHANCED FEATURES:
  ✓ Per-file dynamic cluster sizing (3/5/7 bullets per cluster)
  ✓ Section-by-section clustering within each file
  ✓ Enhanced logging with detailed cluster analysis
  ✓ Improved progress tracking and resume capability
  ✓ 5 questions per cluster for better coverage
  ✓ Smart load balancing across multiple API keys
  ✓ Comprehensive metadata and statistics

PROCESSING FLOW:
  1. Analyze each file → count total bullet points
  2. Calculate optimal cluster size for that file
  3. Process sections within file using calculated cluster size
  4. Generate 5 questions per cluster
  5. Save results with enhanced metadata

OUTPUT STRUCTURE:
  question_bank/
  ├── questions_filename1.json    # Individual file outputs
  ├── questions_filename2.json
  ├── master_question_bank.json   # Combined question bank
  └── logs/
      ├── per_file_cluster_generation.log  # Detailed processing logs
      └── cluster_analysis.log             # Cluster strategy logs
        """
    )
    
    parser.add_argument(
        'folder_path', 
        help='Path to folder containing JSON files with bullet_points structure'
    )
    
    parser.add_argument(
        '--model', 
        default='gpt-5-mini', 
        help='OpenAI model to use (default: gpt-5-mini)'
    )
    
    parser.add_argument(
        '--workers', 
        type=int, 
        help='Maximum number of parallel workers (default: API keys × 2, max 8)'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate folder path
    folder_path = Path(args.folder_path)
    if not folder_path.exists():
        console.print(f"[red]❌ Error: Folder not found: {folder_path}[/red]")
        sys.exit(1)
    
    if not folder_path.is_dir():
        console.print(f"[red]❌ Error: Path is not a directory: {folder_path}[/red]")
        sys.exit(1)
    
    # Check for JSON files with bullet_points structure
    json_files = []
    for json_file in folder_path.glob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                sample_section = data[0]
                if isinstance(sample_section, dict) and 'bullet_points' in sample_section:
                    json_files.append(json_file)
        except:
            continue
    
    if not json_files:
        console.print(f"[red]❌ Error: No JSON files with bullet_points found in {folder_path}[/red]")
        console.print("[yellow]Expected: JSON files containing sections with bullet_points field[/yellow]")
        console.print("[blue]Tip: Run the bullet point generator first to create compatible files[/blue]")
        sys.exit(1)
    
    # Show initial file discovery
    if RICH_AVAILABLE:
        console.print(f"[green]✓ Found {len(json_files)} compatible JSON files[/green]")
    else:
        print(f"✓ Found {len(json_files)} compatible JSON files")
    
    # Initialize generator and run
    try:
        generator = PerFileClusterMCQGenerator(
            folder_path=str(folder_path),
            model_name=args.model,
            max_workers=args.workers
        )
        
        success = generator.run_generation()
        
        if success:
            if RICH_AVAILABLE:
                console.print("\n[bold green]🎉 Enhanced cluster MCQ generation completed successfully![/bold green]")
            else:
                print("\n🎉 Enhanced cluster MCQ generation completed successfully!")
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️ Process interrupted by user. All progress has been saved.[/yellow]")
        console.print("[blue]💡 Resume by running the same command again.[/blue]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]❌ Critical error: {e}[/red]")
        console.print("[blue]💡 Check the logs in question_bank/logs/ for detailed error information.[/blue]")
        sys.exit(1)

if __name__ == "__main__":
    main()