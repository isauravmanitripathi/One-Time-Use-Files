#!/usr/bin/env python3
"""
MCQ Question Extractor
Extracts questions from the cluster MCQ generator output and creates clean test files
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any

class MCQExtractor:
    """Extract and format MCQ questions from generator output"""
    
    def __init__(self):
        self.extracted_questions = []
        self.total_questions = 0
    
    def load_mcq_file(self, file_path: str) -> Dict:
        """Load the MCQ generator output file"""
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
    
    def extract_questions_from_data(self, data: Dict) -> List[Dict]:
        """Extract all questions from the MCQ generator data structure"""
        questions = []
        question_number = 1
        
        # Handle both master question bank and individual file formats
        sections = data.get('sections', [])
        
        for section in sections:
            chapter_name = section.get('chapter_name', 'Unknown Chapter')
            section_name = section.get('section_name', 'Unknown Section')
            bullet_points = section.get('bullet_points', [])
            
            print(f"  📖 Processing: {chapter_name} - {section_name}")
            
            for bullet_point in bullet_points:
                bp_questions = bullet_point.get('questions', [])
                
                for question_data in bp_questions:
                    # Validate question structure
                    if self.validate_question(question_data):
                        # Extract and format question
                        formatted_question = {
                            "question_number": question_number,
                            "question": question_data.get('question', '').strip(),
                            "options": question_data.get('options', []),
                            "correct": question_data.get('correct', 0),
                            "explanations": question_data.get('explanations', {}),
                            "source_info": {
                                "chapter": chapter_name,
                                "section": section_name,
                                "bullet_point_index": bullet_point.get('bullet_point_index', -1)
                            }
                        }
                        questions.append(formatted_question)
                        question_number += 1
        
        return questions
    
    def validate_question(self, question_data: Dict) -> bool:
        """Validate that a question has all required fields"""
        required_fields = ['question', 'options', 'correct', 'explanations']
        
        # Check if all required fields exist
        if not all(field in question_data for field in required_fields):
            return False
        
        # Check question is not empty
        if not question_data['question'].strip():
            return False
        
        # Check options structure
        options = question_data['options']
        if not isinstance(options, list) or len(options) != 4:
            return False
        
        # Check all options are non-empty
        if any(not str(opt).strip() for opt in options):
            return False
        
        # Check correct answer index
        correct = question_data['correct']
        if not isinstance(correct, int) or not (0 <= correct <= 3):
            return False
        
        # Check explanations structure
        explanations = question_data['explanations']
        if not isinstance(explanations, dict) or len(explanations) != 4:
            return False
        
        # Check all explanation keys exist
        if not all(str(i) in explanations for i in range(4)):
            return False
        
        return True
    
    def create_test_file(self, questions: List[Dict], timer: int, instructions: str, output_path: str) -> bool:
        """Create the final test file in the required format"""
        
        # Remove source_info from questions for the final output
        clean_questions = []
        for q in questions:
            clean_question = {
                "question": q["question"],
                "options": q["options"],
                "correct": q["correct"],
                "explanations": q["explanations"]
            }
            clean_questions.append(clean_question)
        
        # Create the test structure
        test_data = {
            "timer": timer,
            "instructions": instructions,
            "questions": clean_questions
        }
        
        try:
            # Ensure output directory exists
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Write the test file
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(test_data, f, indent=2, ensure_ascii=False)
            
            return True
            
        except Exception as e:
            print(f"❌ Error saving test file: {e}")
            return False
    
    def get_user_input(self) -> tuple:
        """Get timer, instructions, and output path from user"""
        print("\n" + "="*60)
        print("📝 MCQ Test Configuration")
        print("="*60)
        
        # Get timer
        while True:
            try:
                timer_input = input("⏱️  Enter test timer (minutes): ").strip()
                timer_minutes = int(timer_input)
                if timer_minutes > 0:
                    timer_seconds = timer_minutes * 60
                    break
                else:
                    print("❌ Please enter a positive number")
            except ValueError:
                print("❌ Please enter a valid number")
        
        # Get instructions
        print("\n📋 Enter test instructions:")
        print("   (Press Enter twice when done)")
        instructions_lines = []
        while True:
            line = input()
            if line.strip() == "" and instructions_lines:
                break
            if line.strip() != "":
                instructions_lines.append(line)
        
        instructions = " ".join(instructions_lines) if instructions_lines else "Complete all questions within the time limit."
        
        # Get output file path
        while True:
            output_path = input("\n💾 Enter output file path (e.g., /path/to/test.json): ").strip()
            if output_path:
                # Add .json extension if not present
                if not output_path.lower().endswith('.json'):
                    output_path += '.json'
                break
            else:
                print("❌ Please enter a valid output path")
        
        return timer_seconds, instructions, output_path
    
    def show_extraction_summary(self, questions: List[Dict]):
        """Show summary of extracted questions"""
        print("\n" + "="*60)
        print("📊 EXTRACTION SUMMARY")
        print("="*60)
        print(f"Total Questions Extracted: {len(questions)}")
        
        # Group by source chapter
        chapter_counts = {}
        for q in questions:
            chapter = q.get('source_info', {}).get('chapter', 'Unknown')
            chapter_counts[chapter] = chapter_counts.get(chapter, 0) + 1
        
        print("\n📚 Questions by Chapter:")
        for chapter, count in sorted(chapter_counts.items()):
            print(f"  • {chapter}: {count} questions")
        
        print("="*60)
    
    def run_extraction(self):
        """Main method to run the extraction process"""
        print("="*60)
        print("🚀 MCQ Question Extractor")
        print("="*60)
        print("This tool extracts questions from MCQ generator output files")
        print("and creates clean test files for UPSC preparation.")
        print("="*60)
        
        # Get input file path
        while True:
            file_path = input("\n📁 Enter path to MCQ file (questions_*.json or master_question_bank.json): ").strip()
            
            if not file_path:
                print("❌ Please enter a file path")
                continue
            
            if not os.path.exists(file_path):
                print(f"❌ File not found: {file_path}")
                continue
            
            break
        
        # Load and validate file
        print(f"\n🔍 Loading file: {file_path}")
        data = self.load_mcq_file(file_path)
        
        if data is None:
            print("❌ Failed to load MCQ file")
            return False
        
        # Extract questions
        print("🔄 Extracting questions...")
        questions = self.extract_questions_from_data(data)
        
        if not questions:
            print("❌ No valid questions found in the file")
            return False
        
        # Show summary
        self.show_extraction_summary(questions)
        
        # Get user configuration
        timer, instructions, output_path = self.get_user_input()
        
        # Create test file
        print(f"\n💾 Creating test file: {output_path}")
        success = self.create_test_file(questions, timer, instructions, output_path)
        
        if success:
            print("\n" + "="*60)
            print("✅ SUCCESS!")
            print("="*60)
            print(f"📁 Test file created: {output_path}")
            print(f"⏱️  Timer: {timer//60} minutes ({timer} seconds)")
            print(f"📝 Questions: {len(questions)}")
            print(f"📋 Instructions: {instructions[:50]}{'...' if len(instructions) > 50 else ''}")
            print("="*60)
            print("🎯 Your UPSC test file is ready!")
            return True
        else:
            print("❌ Failed to create test file")
            return False

def main():
    """Main entry point"""
    try:
        extractor = MCQExtractor()
        success = extractor.run_extraction()
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()