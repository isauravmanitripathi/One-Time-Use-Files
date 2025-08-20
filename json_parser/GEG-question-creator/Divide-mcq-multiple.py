#!/usr/bin/env python3
"""
MCQ File Divider
Takes an MCQ JSON file and divides it into multiple files with 100 questions each
while preserving the exact structure and calculating appropriate timers
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any
import math

class MCQDivider:
    """Divides MCQ files into chunks of 100 questions with proper timing"""
    
    def __init__(self):
        self.questions_per_file = 100
    
    def load_mcq_file(self, file_path: str) -> Dict:
        """Load the MCQ test file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"❌ Error: File not found: {file_path}")
            return None
        except json.JSONDecodeError:
            print(f"❌ Error: Invalid JSON file: {file_path}")
            return None
        except Exception as e:
            print(f"❌ Error reading file: {e}")
            return None
    
    def validate_mcq_structure(self, data: Dict) -> bool:
        """Validate that the file has the expected MCQ test structure"""
        required_fields = ['timer', 'instructions', 'questions']
        
        if not all(field in data for field in required_fields):
            print("❌ Error: File must contain 'timer', 'instructions', and 'questions' fields")
            return False
        
        if not isinstance(data['questions'], list):
            print("❌ Error: 'questions' must be a list")
            return False
        
        if len(data['questions']) == 0:
            print("❌ Error: No questions found in file")
            return False
        
        # Validate first question structure
        first_q = data['questions'][0]
        required_q_fields = ['question', 'options', 'correct', 'explanations']
        
        if not all(field in first_q for field in required_q_fields):
            print("❌ Error: Questions must have 'question', 'options', 'correct', and 'explanations' fields")
            return False
        
        return True
    
    def get_time_per_question(self) -> int:
        """Get time per question from user in seconds"""
        print("\n" + "="*60)
        print("⏱️  TIME CONFIGURATION")
        print("="*60)
        
        while True:
            try:
                time_input = input("Enter time per question (in seconds): ").strip()
                time_seconds = int(time_input)
                if time_seconds > 0:
                    print(f"✅ Time per question: {time_seconds} seconds")
                    return time_seconds
                else:
                    print("❌ Please enter a positive number")
            except ValueError:
                print("❌ Please enter a valid number")
    
    def create_instructions(self, time_per_question: int, original_instructions: str = "") -> str:
        """Create instructions with timing information"""
        base_instructions = f"You have {time_per_question} seconds per question. "
        base_instructions += "Read each question carefully and select the best answer. "
        base_instructions += "Do not refresh the page during the test. "
        base_instructions += "Complete all questions within the time limit."
        
        # Clean and validate original instructions
        if original_instructions:
            cleaned_original = original_instructions.strip()
            
            # Skip if it's empty, just the default message, or looks like random text
            skip_conditions = [
                not cleaned_original,
                cleaned_original == "Complete all questions within the time limit.",
                len(cleaned_original) < 10,  # Too short to be meaningful
                not any(c.isalpha() for c in cleaned_original),  # No letters
                cleaned_original.lower() in ['test', 'exam', 'quiz', 'edwe', 'abc', 'xyz']  # Common test text
            ]
            
            if not any(skip_conditions):
                base_instructions += f" {cleaned_original}"
        
        return base_instructions
    
    def divide_questions(self, questions: List[Dict]) -> List[List[Dict]]:
        """Divide questions into chunks of 100"""
        chunks = []
        total_questions = len(questions)
        
        for i in range(0, total_questions, self.questions_per_file):
            chunk = questions[i:i + self.questions_per_file]
            chunks.append(chunk)
        
        return chunks
    
    def create_divided_files(self, data: Dict, time_per_question: int, input_file_path: str) -> bool:
        """Create multiple JSON files with divided questions"""
        
        # Get file info for naming
        input_path = Path(input_file_path)
        base_name = input_path.stem  # filename without extension
        output_dir = input_path.parent
        
        # Get questions and divide them
        all_questions = data['questions']
        question_chunks = self.divide_questions(all_questions)
        
        # Create instructions
        new_instructions = self.create_instructions(time_per_question, data.get('instructions', ''))
        
        success_count = 0
        
        print(f"\n🔄 Creating {len(question_chunks)} divided files...")
        
        for i, chunk in enumerate(question_chunks, 1):
            # Calculate timer for this chunk
            chunk_timer = len(chunk) * time_per_question
            
            # Create new file data
            file_data = {
                "timer": chunk_timer,
                "instructions": new_instructions,
                "questions": chunk
            }
            
            # Create output filename
            output_filename = f"{base_name}-divided-{i}.json"
            output_path = output_dir / output_filename
            
            try:
                # Write the file
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(file_data, f, indent=2, ensure_ascii=False)
                
                print(f"  ✅ Created: {output_filename} ({len(chunk)} questions, {chunk_timer//60}:{chunk_timer%60:02d})")
                success_count += 1
                
            except Exception as e:
                print(f"  ❌ Failed to create {output_filename}: {e}")
        
        return success_count == len(question_chunks)
    
    def show_summary(self, total_questions: int, time_per_question: int, num_files: int):
        """Show final summary"""
        print("\n" + "="*60)
        print("📊 DIVISION SUMMARY")
        print("="*60)
        print(f"Total Questions: {total_questions}")
        print(f"Time per Question: {time_per_question} seconds")
        print(f"Questions per File: {self.questions_per_file}")
        print(f"Files Created: {num_files}")
        
        # Show file breakdown
        full_files = total_questions // self.questions_per_file
        remaining = total_questions % self.questions_per_file
        
        print(f"\n📂 File Breakdown:")
        if full_files > 0:
            total_time_full = self.questions_per_file * time_per_question
            print(f"  • {full_files} files with {self.questions_per_file} questions each ({total_time_full//60}:{total_time_full%60:02d})")
        
        if remaining > 0:
            total_time_remaining = remaining * time_per_question
            print(f"  • 1 file with {remaining} questions ({total_time_remaining//60}:{total_time_remaining%60:02d})")
        
        print("="*60)
        print("🎯 MCQ files are ready for UPSC practice!")
    
    def run(self):
        """Main method to run the division process"""
        print("="*60)
        print("📚 MCQ File Divider")
        print("="*60)
        print("This tool divides large MCQ test files into smaller chunks")
        print("of 100 questions each with proper timing calculations.")
        print("="*60)
        
        # Get input file
        while True:
            file_path = input("\n📁 Enter path to MCQ test file (.json): ").strip()
            
            if not file_path:
                print("❌ Please enter a file path")
                continue
            
            if not os.path.exists(file_path):
                print(f"❌ File not found: {file_path}")
                continue
            
            if not file_path.lower().endswith('.json'):
                print("❌ Please enter a JSON file")
                continue
            
            break
        
        # Load and validate file
        print(f"\n🔍 Loading file: {os.path.basename(file_path)}")
        data = self.load_mcq_file(file_path)
        
        if data is None:
            print("❌ Failed to load MCQ file")
            return False
        
        # Validate structure
        if not self.validate_mcq_structure(data):
            return False
        
        total_questions = len(data['questions'])
        print(f"✅ Found {total_questions} questions")
        
        # Get timing configuration
        time_per_question = self.get_time_per_question()
        
        # Calculate number of files needed
        num_files = math.ceil(total_questions / self.questions_per_file)
        
        print(f"\n📊 Will create {num_files} files:")
        full_files = total_questions // self.questions_per_file
        remaining = total_questions % self.questions_per_file
        
        if full_files > 0:
            print(f"  • {full_files} files with {self.questions_per_file} questions each")
        if remaining > 0:
            print(f"  • 1 file with {remaining} questions")
        
        # Confirm with user
        confirm = input(f"\n❓ Proceed with division? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("🛑 Operation cancelled")
            return False
        
        # Create divided files
        success = self.create_divided_files(data, time_per_question, file_path)
        
        if success:
            self.show_summary(total_questions, time_per_question, num_files)
            return True
        else:
            print("❌ Failed to create some files")
            return False

def main():
    """Main entry point"""
    try:
        divider = MCQDivider()
        success = divider.run()
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()