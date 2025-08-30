#!/usr/bin/env python3
"""
MCQ Test LaTeX PDF Generator - Manual Layout Control
Manually calculates and controls question distribution across pages and columns
"""

import json
import os
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Tuple
import tempfile
import math

class ManualLayoutPDFGenerator:
    """Generate question bank PDF with manual layout control"""
    
    def __init__(self):
        self.temp_dir = None
        self.tex_file = None
        
        # Layout parameters (estimated)
        self.lines_per_column = 35  # Approximately 35 lines per column
        self.avg_question_lines = 6  # Question + 4 options ≈ 6 lines
        self.questions_per_column = 5  # Safe estimate: 5 questions per column
        self.questions_per_page = 10  # 2 columns × 5 questions
    
    def check_latex_installation(self) -> bool:
        """Check if LaTeX is installed and accessible"""
        try:
            result = subprocess.run(['pdflatex', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print("✅ LaTeX installation found")
                return True
            else:
                print("❌ LaTeX not accessible")
                return False
        except (subprocess.TimeoutExpired, FileNotFoundError):
            print("❌ LaTeX (pdflatex) not found in PATH")
            print("💡 Make sure MacTeX is installed and in your PATH")
            return False
    
    def load_test_file(self, file_path: str) -> Dict:
        """Load the test JSON file"""
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
    
    def validate_test_data(self, data: Dict) -> bool:
        """Validate the test data structure"""
        required_fields = ['timer', 'instructions', 'questions']
        
        if not all(field in data for field in required_fields):
            print("❌ Error: Missing required fields in test data")
            return False
        
        questions = data.get('questions', [])
        if not questions:
            print("❌ Error: No questions found in test data")
            return False
        
        return True
    
    def format_timer(self, seconds: int) -> str:
        """Convert seconds to readable format"""
        if seconds >= 3600:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{hours}h {minutes}m"
        elif seconds >= 60:
            minutes = seconds // 60
            return f"{minutes} minutes"
        else:
            return f"{seconds} seconds"
    
    def escape_latex(self, text: str) -> str:
        """Escape special LaTeX characters - simplified and safe"""
        if not text:
            return ""
        
        # Handle most common problematic characters
        replacements = [
            ('\\', r'\textbackslash '),
            ('&', r'\&'),
            ('%', r'\%'),
            ('$', r'\$'),
            ('#', r'\#'),
            ('^', r'\textasciicircum '),
            ('_', r'\_'),
            ('{', r'\{'),
            ('}', r'\}'),
            ('~', r'\textasciitilde '),
            ('"', "''"),
            (''', "'"),
            (''', "'"),
            ('"', "''"),
            ('"', "''"),
            ('…', '...'),
        ]
        
        result = text
        for old, new in replacements:
            result = result.replace(old, new)
        
        return result
    
    def estimate_question_lines(self, question_data: Dict) -> int:
        """Estimate how many lines a question will take"""
        question_text = question_data['question']
        options = question_data['options']
        
        # Estimate lines for question (roughly 50 chars per line)
        question_lines = max(1, len(question_text) // 50)
        
        # 4 options, each roughly 1 line
        option_lines = 4
        
        # Add spacing
        spacing_lines = 2
        
        return question_lines + option_lines + spacing_lines
    
    def distribute_questions_to_pages(self, questions: List[Dict]) -> List[List[List[Dict]]]:
        """
        Distribute questions to pages and columns
        Returns: List of pages, each page has [left_column, right_column]
        """
        pages = []
        current_page_left = []
        current_page_right = []
        left_column_lines = 0
        right_column_lines = 0
        
        print(f"📊 Distributing {len(questions)} questions across pages...")
        
        for i, question in enumerate(questions):
            question_lines = self.estimate_question_lines(question)
            
            # Try to fit in left column first
            if left_column_lines + question_lines <= self.lines_per_column:
                current_page_left.append(question)
                left_column_lines += question_lines
            
            # Try right column
            elif right_column_lines + question_lines <= self.lines_per_column:
                current_page_right.append(question)
                right_column_lines += question_lines
            
            # Need new page
            else:
                # Save current page if it has content
                if current_page_left or current_page_right:
                    pages.append([current_page_left, current_page_right])
                
                # Start new page
                current_page_left = [question]
                current_page_right = []
                left_column_lines = question_lines
                right_column_lines = 0
        
        # Add the last page if it has content
        if current_page_left or current_page_right:
            pages.append([current_page_left, current_page_right])
        
        print(f"📄 Questions distributed across {len(pages)} pages")
        return pages
    
    def create_latex_document(self, data: Dict) -> str:
        """Create the complete LaTeX document with manual layout"""
        questions = data['questions']
        question_count = len(questions)
        timer_str = self.format_timer(data['timer'])
        instructions = self.escape_latex(data['instructions'])
        
        # Distribute questions to pages
        question_pages = self.distribute_questions_to_pages(questions)
        
        # LaTeX document header
        latex_content = r"""
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{multicol}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

% Page setup
\geometry{
    a4paper,
    left=20mm,
    right=20mm,
    top=25mm,
    bottom=25mm
}

% Colors
\definecolor{darkblue}{RGB}{0,51,102}
\definecolor{darkgreen}{RGB}{0,100,0}
\definecolor{darkred}{RGB}{139,0,0}

% Header and footer
\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\textcolor{darkblue}{\textbf{MCQ Question Bank}}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.5pt}

% Custom commands
\newcommand{\questionnum}[1]{\textbf{Q#1.}}

% Title formatting
\titleformat{\section}
{\normalfont\Large\bfseries\color{darkblue}}
{\thesection}{1em}{}

% List formatting
\setlist[enumerate]{nosep, leftmargin=15pt}
\setlist[itemize]{nosep, leftmargin=15pt}

\begin{document}

% Title page
\begin{center}
{\Huge \textcolor{darkblue}{\textbf{MCQ Question Bank}}}\\[20pt]
{\Large Test Preparation Material}\\[30pt]

\begin{tabular}{ll}
\textbf{Total Questions:} & """ + str(question_count) + r""" \\[5pt]
\textbf{Time Limit:} & """ + timer_str + r""" \\[5pt]
\textbf{Generated:} & """ + datetime.now().strftime("%B %d, %Y") + r""" \\
\end{tabular}\\[30pt]

\textbf{\large Instructions:}\\[10pt]
\begin{minipage}{0.8\textwidth}
""" + instructions + r"""
\end{minipage}\\[20pt]

\textbf{\large How to use this question bank:}\\[10pt]
\begin{minipage}{0.8\textwidth}
• Questions are arranged in two columns per page\\
• Answer all questions before checking the answer key\\
• Answer key with detailed explanations starts after all questions\\
• Each explanation covers why the correct answer is right and why others are wrong
\end{minipage}\\[40pt]

\rule{\textwidth}{0.5pt}
\end{center}

\newpage

\section*{\centering QUESTIONS}

"""
        
        # Add questions page by page with manual column control
        question_counter = 1
        
        for page_num, (left_column, right_column) in enumerate(question_pages):
            print(f"   📄 Processing page {page_num + 1}: {len(left_column)} + {len(right_column)} questions")
            
            # Start two-column layout for this page
            latex_content += r"\begin{multicols}{2}" + "\n"
            
            # Left column questions
            for question_data in left_column:
                latex_content += self.format_single_question(question_counter, question_data)
                question_counter += 1
            
            # Column break
            latex_content += r"\columnbreak" + "\n"
            
            # Right column questions  
            for question_data in right_column:
                latex_content += self.format_single_question(question_counter, question_data)
                question_counter += 1
            
            # End two-column layout
            latex_content += r"\end{multicols}" + "\n"
            
            # Page break if not the last page
            if page_num < len(question_pages) - 1:
                latex_content += r"\newpage" + "\n"
        
        # Start answer key section
        latex_content += r"""
\newpage
\section*{\centering ANSWER KEY \& EXPLANATIONS}

"""
        
        # Add answer key
        for i, question_data in enumerate(questions, 1):
            latex_content += self.format_answer_key(i, question_data)
        
        # Document end
        latex_content += r"\end{document}"
        
        return latex_content
    
    def format_single_question(self, question_num: int, question_data: Dict) -> str:
        """Format a single question for column display"""
        question_text = self.escape_latex(question_data['question'])
        options = [self.escape_latex(opt) for opt in question_data['options']]
        
        return f"""
\\questionnum{{{question_num}}} {question_text}

\\begin{{enumerate}}[label=\\Alph*., nosep]
\\item {options[0]}
\\item {options[1]}
\\item {options[2]}
\\item {options[3]}
\\end{{enumerate}}

\\vspace{{8pt}}

"""
    
    def format_answer_key(self, question_num: int, question_data: Dict) -> str:
        """Format answer key entry"""
        question_text = self.escape_latex(question_data['question'])
        options = [self.escape_latex(opt) for opt in question_data['options']]
        correct_index = question_data['correct']
        correct_letter = chr(65 + correct_index)  # A, B, C, D
        explanations = question_data['explanations']
        
        # Question reference (truncated if too long)
        if len(question_text) > 80:
            question_ref = question_text[:80] + "..."
        else:
            question_ref = question_text
        
        answer_content = f"""\\textbf{{Q{question_num}.}} {question_ref}

\\textcolor{{darkgreen}}{{\\textbf{{Correct Answer: {correct_letter}}}}} -- {options[correct_index]}

\\textcolor{{darkgreen}}{{\\textbf{{Why {correct_letter} is correct:}}}} {self.escape_latex(explanations.get(str(correct_index), "No explanation provided"))}

"""
        
        # Add wrong explanations
        for opt_idx in range(4):
            if opt_idx != correct_index:
                wrong_letter = chr(65 + opt_idx)
                wrong_explanation = explanations.get(str(opt_idx), "No explanation provided")
                escaped_explanation = self.escape_latex(wrong_explanation)
                answer_content += f"""\\textcolor{{darkred}}{{\\textbf{{Why {wrong_letter} is wrong:}}}} {escaped_explanation}

"""
        
        answer_content += "\\vspace{12pt}\n\n"
        return answer_content
    
    def compile_latex(self, tex_content: str, output_path: str) -> bool:
        """Compile LaTeX to PDF"""
        try:
            # Create temporary directory
            self.temp_dir = tempfile.mkdtemp()
            tex_file = Path(self.temp_dir) / "question_bank.tex"
            
            # Write LaTeX content
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.write(tex_content)
            
            print("🔄 Compiling LaTeX document...")
            
            # Run pdflatex twice for proper formatting
            for run in [1, 2]:
                print(f"   📄 LaTeX compilation run {run}/2...")
                result = subprocess.run([
                    'pdflatex',
                    '-interaction=nonstopmode',
                    '-output-directory', str(self.temp_dir),
                    str(tex_file)
                ], capture_output=True, text=True, cwd=self.temp_dir)
                
                if result.returncode != 0:
                    print(f"❌ LaTeX compilation failed on run {run}")
                    print("LaTeX Error Output:")
                    print(result.stdout[-1500:])  # Last 1500 chars
                    
                    # Also save the .tex file for debugging
                    debug_file = Path(output_path).parent / "debug_question_bank.tex"
                    shutil.copy2(tex_file, debug_file)
                    print(f"🐛 Debug: LaTeX source saved to {debug_file}")
                    return False
            
            # Copy PDF to output location
            pdf_file = Path(self.temp_dir) / "question_bank.pdf"
            if pdf_file.exists():
                shutil.copy2(pdf_file, output_path)
                print(f"✅ PDF successfully generated: {output_path}")
                return True
            else:
                print("❌ PDF file was not generated")
                return False
                
        except Exception as e:
            print(f"❌ Error during LaTeX compilation: {e}")
            return False
        finally:
            # Clean up temporary directory
            if self.temp_dir and Path(self.temp_dir).exists():
                try:
                    shutil.rmtree(self.temp_dir)
                except:
                    pass  # Ignore cleanup errors
    
    def get_output_path(self, input_path: str) -> str:
        """Get output PDF path from user"""
        input_file = Path(input_path)
        default_name = input_file.stem + "_question_bank.pdf"
        default_path = input_file.parent / default_name
        
        print(f"\n💾 Default output: {default_path}")
        custom_path = input("   Enter custom PDF path (or press Enter for default): ").strip()
        
        if custom_path:
            if not custom_path.lower().endswith('.pdf'):
                custom_path += '.pdf'
            return custom_path
        else:
            return str(default_path)
    
    def show_generation_summary(self, data: Dict, output_path: str):
        """Show summary of PDF generation"""
        print("\n" + "="*60)
        print("📊 QUESTION BANK GENERATION SUMMARY")
        print("="*60)
        print(f"📁 Output File: {output_path}")
        print(f"📝 Questions: {len(data['questions'])}")
        print(f"⏱️  Timer: {self.format_timer(data['timer'])}")
        print(f"📖 Layout: Manual page/column distribution")
        print(f"🛠️  Generated using: LaTeX with manual layout control")
        
        # File size
        try:
            file_size = os.path.getsize(output_path)
            if file_size > 1024 * 1024:
                size_str = f"{file_size / (1024 * 1024):.1f} MB"
            elif file_size > 1024:
                size_str = f"{file_size / 1024:.1f} KB"
            else:
                size_str = f"{file_size} bytes"
            print(f"📦 File Size: {size_str}")
        except:
            pass
        
        print("="*60)
        print("🎯 Your manually-laid-out question bank is ready!")
        print("📖 Perfect spacing and controlled layout!")
    
    def run_generation(self):
        """Main method to run the PDF generation process"""
        print("="*60)
        print("🚀 Manual Layout MCQ Question Bank Generator")
        print("="*60)
        print("Features:")
        print("• Manual page and column distribution")
        print("• Controlled question spacing")
        print("• No overflow errors")
        print("• Predictable layout")
        print("="*60)
        
        # Check LaTeX installation
        if not self.check_latex_installation():
            print("\n💡 To install LaTeX on macOS:")
            print("   brew install --cask mactex")
            print("   # OR download from: https://tug.org/mactex/")
            return False
        
        # Get input file path
        while True:
            file_path = input("\n📁 Enter path to test JSON file: ").strip()
            
            if not file_path:
                print("❌ Please enter a file path")
                continue
            
            if not os.path.exists(file_path):
                print(f"❌ File not found: {file_path}")
                continue
            
            if not file_path.lower().endswith('.json'):
                print("❌ Please provide a JSON file")
                continue
            
            break
        
        # Load and validate file
        print(f"\n🔍 Loading test file: {file_path}")
        data = self.load_test_file(file_path)
        
        if data is None:
            return False
        
        if not self.validate_test_data(data):
            return False
        
        print(f"✅ Loaded {len(data['questions'])} questions")
        
        # Get output path
        output_path = self.get_output_path(file_path)
        
        # Generate LaTeX content
        print("\n📝 Generating LaTeX document with manual layout...")
        latex_content = self.create_latex_document(data)
        
        # Compile to PDF
        success = self.compile_latex(latex_content, output_path)
        
        if success:
            print("\n✅ SUCCESS!")
            self.show_generation_summary(data, output_path)
            return True
        else:
            print("❌ Failed to generate PDF")
            return False

def main():
    """Main entry point"""
    try:
        generator = ManualLayoutPDFGenerator()
        success = generator.run_generation()
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()