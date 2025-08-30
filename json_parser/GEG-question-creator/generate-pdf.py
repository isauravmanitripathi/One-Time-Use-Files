#!/usr/bin/env python3
"""
MCQ Test LaTeX PDF Generator - Question Bank Book Style
Creates a two-column question layout with separate answer key using LaTeX
"""

import json
import os
import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import tempfile

class LaTeXQuestionBankGenerator:
    """Generate question bank style PDF using LaTeX"""
    
    def __init__(self):
        self.temp_dir = None
        self.tex_file = None
    
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
        """Escape special LaTeX characters"""
        if not text:
            return ""
        
        result = text.replace('\\', r'\textbackslash{}')
        
        latex_special = {
            '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '^': r'\textasciicircum{}',
            '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
        }
        
        for char, escape in latex_special.items():
            result = result.replace(char, escape)
        
        result = result.replace('…', '...')
        result = result.replace('‘', '`').replace('’', "'")
        result = result.replace('“', '``').replace('”', "''")
        result = result.replace('"', "''")
        
        return result
    
    def create_latex_document(self, data: Dict) -> str:
        """Create the complete LaTeX document"""
        questions = data['questions']
        question_count = len(questions)
        timer_str = self.format_timer(data['timer'])
        instructions = self.escape_latex(data['instructions'])
        
        # FINAL FIX: The entire LaTeX structure is rebuilt for stability.
        # 1. Start in 'onecolumn' mode.
        # 2. Create the title page normally.
        # 3. Explicitly switch to 'twocolumn' for questions.
        # This resolves the underlying layout conflict that caused all previous errors.
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

\geometry{a4paper, left=20mm, right=20mm, top=25mm, bottom=25mm, columnsep=8mm}

\definecolor{darkblue}{RGB}{0,51,102}
\definecolor{darkgreen}{RGB}{0,100,0}
\definecolor{darkred}{RGB}{139,0,0}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[C]{\textcolor{darkblue}{\textbf{MCQ Question Bank}}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.5pt}
\renewcommand{\footrulewidth}{0.5pt}

\newcommand{\questionnum}[1]{\textbf{Q#1.}}
\newcommand{\correctans}[1]{\textcolor{darkgreen}{\textbf{#1}}}

\titleformat{\section}{\normalfont\Large\bfseries\color{darkblue}}{\thesection}{1em}{}

\setlist[enumerate]{nosep, leftmargin=*}
\setlist[itemize]{nosep, leftmargin=*}

\begin{document}

% Title page (now in standard one-column mode)
\begin{center}
{\Huge \textcolor{darkblue}{\textbf{MCQ Question Bank}}}\\[20pt]
{\Large Test Preparation Material}\\[30pt]

\begin{tabular}{ll}
\textbf{Total Questions:} & """ + str(question_count) + r""" \\[5pt]
\textbf{Time Limit:} & """ + timer_str + r""" \\[5pt]
\textbf{Generated:} & """ + datetime.now().strftime("%B %d, %Y") + r""" \\
\end{tabular}\\[30pt]

\parbox{0.8\textwidth}{
\textbf{\large Instructions:}\\[10pt]
""" + instructions + r"""
}\\[20pt]

\parbox{0.8\textwidth}{
\textbf{\large How to use this question bank:}\\[10pt]
• Questions are arranged in two columns per page\\
• Answer all questions before checking the answer key\\
• Answer key with detailed explanations starts after all questions\\
• Each explanation covers why the correct answer is right and why others are wrong
}\\[40pt]

\rule{\textwidth}{0.5pt}
\end{center}

\newpage
% Explicitly switch to two-column mode for the questions section
\twocolumn 

\section*{\centering QUESTIONS}
\addcontentsline{toc}{section}{Questions}
"""
        
        for i, question_data in enumerate(questions, 1):
            question_text = self.escape_latex(question_data['question'])
            options = [self.escape_latex(opt) for opt in question_data['options']]
            
            latex_content += f"""
\\questionnum{{{i}}} {question_text}
\\begin{{enumerate}}[label=\\Alph*., nosep, leftmargin=*]
\\item {options[0]}
\\item {options[1]}
\\item {options[2]}
\\item {options[3]}
\\end{{enumerate}}
\\vspace{{10pt}}
"""
        
        latex_content += r"""
\clearpage 
\onecolumn
\section*{\centering ANSWER KEY \& EXPLANATIONS}
\addcontentsline{toc}{section}{Answer Key \& Explanations}
"""
        
        for i, question_data in enumerate(questions, 1):
            question_text = self.escape_latex(question_data['question'])
            options = [self.escape_latex(opt) for opt in question_data['options']]
            correct_index = question_data['correct']
            correct_letter = chr(65 + correct_index)
            explanations = question_data['explanations']
            
            question_ref = question_text[:80] + "..." if len(question_text) > 80 else question_text
            
            latex_content += f"""\\par\\textbf{{Q{i}.}} {question_ref}
\\correctans{{Correct Answer: {correct_letter}}} -- {options[correct_index]}
\\par\\textcolor{{darkgreen}}{{\\textbf{{Why {correct_letter} is correct:}}}} {self.escape_latex(explanations.get(str(correct_index), "N/A"))}
"""
            
            for opt_idx in range(4):
                if opt_idx != correct_index:
                    wrong_letter = chr(65 + opt_idx)
                    wrong_explanation = explanations.get(str(opt_idx), "N/A")
                    escaped_explanation = self.escape_latex(wrong_explanation)
                    latex_content += f"""\\par\\textcolor{{darkred}}{{\\textbf{{Why {wrong_letter} is wrong:}}}} {escaped_explanation}"""
            
            latex_content += "\\vspace{15pt}\n"
        
        latex_content += r"\end{document}"
        return latex_content
    
    def compile_latex(self, tex_content: str, output_path: str) -> bool:
        """Compile LaTeX to PDF"""
        try:
            self.temp_dir = tempfile.mkdtemp()
            tex_file = Path(self.temp_dir) / "question_bank.tex"
            with open(tex_file, 'w', encoding='utf-8') as f: f.write(tex_content)
            
            print("🔄 Compiling LaTeX document...")
            for run in [1, 2]:
                print(f"    📄 LaTeX compilation run {run}/2...")
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-output-directory', str(self.temp_dir), str(tex_file)],
                    capture_output=True, text=True, cwd=self.temp_dir
                )
                if result.returncode != 0:
                    print(f"❌ LaTeX compilation failed on run {run}")
                    print("LaTeX Log Output (last 1000 chars):")
                    log_file = tex_file.with_suffix('.log')
                    if log_file.exists():
                        print(log_file.read_text()[-1000:])
                    else:
                        print(result.stdout[-1000:])
                    return False
            
            pdf_file = Path(self.temp_dir) / "question_bank.pdf"
            if pdf_file.exists():
                shutil.copy2(pdf_file, output_path)
                print(f"✅ PDF successfully generated: {output_path}")
                return True
            else:
                print("❌ PDF file was not generated after compilation.")
                return False
        except Exception as e:
            print(f"❌ An exception occurred during LaTeX compilation: {e}")
            return False
        finally:
            if self.temp_dir and Path(self.temp_dir).exists():
                shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def get_output_path(self, input_path: str) -> str:
        """Get output PDF path from user"""
        input_file = Path(input_path)
        default_name = input_file.stem + "_question_bank.pdf"
        default_path = input_file.parent / default_name
        
        print(f"\n💾 Default output: {default_path}")
        custom_path = input("    Enter custom PDF path (or press Enter for default): ").strip()
        
        if custom_path:
            if not custom_path.lower().endswith('.pdf'): custom_path += '.pdf'
            return custom_path
        return str(default_path)
    
    def show_generation_summary(self, data: Dict, output_path: str):
        """Show summary of PDF generation"""
        print("\n" + "="*60)
        print("📊 QUESTION BANK GENERATION SUMMARY")
        print("="*60)
        print(f"📁 Output File: {output_path}")
        print(f"📝 Questions: {len(data['questions'])}")
        print(f"⏱️  Timer: {self.format_timer(data['timer'])}")
        
        try:
            file_size = os.path.getsize(output_path)
            if file_size > 1024 * 1024: size_str = f"{file_size / (1024 * 1024):.1f} MB"
            elif file_size > 1024: size_str = f"{file_size / 1024:.1f} KB"
            else: size_str = f"{file_size} bytes"
            print(f"📦 File Size: {size_str}")
        except: pass
        
        print("="*60)
        print("🎯 Your professional question bank is ready!")
    
    def run_generation(self):
        """Main method to run the PDF generation process"""
        print("="*60)
        print("🚀 LaTeX MCQ Question Bank Generator")
        print("="*60)
        
        if not self.check_latex_installation():
            print("\n💡 To install LaTeX on macOS, run: brew install --cask mactex")
            return False
        
        while True:
            file_path = input("\n📁 Enter path to test JSON file: ").strip()
            if not file_path:
                print("❌ Please enter a file path.")
                continue
            if not os.path.exists(file_path):
                print(f"❌ File not found: {file_path}")
                continue
            if not file_path.lower().endswith('.json'):
                print("❌ Please provide a JSON file.")
                continue
            break
        
        print(f"\n🔍 Loading test file: {file_path}")
        data = self.load_test_file(file_path)
        if data is None or not self.validate_test_data(data):
            return False
        
        print(f"✅ Loaded {len(data['questions'])} questions.")
        
        output_path = self.get_output_path(file_path)
        
        print("\n📝 Generating LaTeX document...")
        latex_content = self.create_latex_document(data)
        
        if self.compile_latex(latex_content, output_path):
            print("\n✅ SUCCESS!")
            self.show_generation_summary(data, output_path)
            return True
        else:
            print("\n❌ Failed to generate PDF. Please check the LaTeX log output above for errors.")
            return False

def main():
    try:
        generator = LaTeXQuestionBankGenerator()
        success = generator.run_generation()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ A critical error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

