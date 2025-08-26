#!/usr/bin/env python3
"""
Front Matter Generator with Detailed Preface
Scans markdown files, extracts headings, generates detailed front matter with Claude API
Creates JSON response and PDF with quote, letter to readers, and detailed preface
"""

import os
import re
import sys
import subprocess
import tempfile
import shutil
import json
from pathlib import Path
from typing import List, Dict
import unicodedata

# Check for required libraries
try:
    import anthropic
    from dotenv import load_dotenv
except ImportError as e:
    print("Error: Required library not found!")
    missing_libs = []
    if "anthropic" in str(e):
        missing_libs.append("anthropic")
    if "dotenv" in str(e):
        missing_libs.append("python-dotenv")
    
    print(f"Install with: pip install {' '.join(missing_libs)}")
    sys.exit(1)

# Load environment variables from .env file
load_dotenv()

def natural_sort_key(s: str) -> List:
    """Sort strings containing numbers naturally."""
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split(r'(\d+)', s)]

def find_markdown_files(root_path: Path) -> List[Path]:
    """Find all markdown files in the directory."""
    markdown_files = []
    
    # Look for chapter folders with final_article.md first
    chapter_pattern = re.compile(r'^Chapter\s+\d+$', re.IGNORECASE)
    chapter_folders = []
    
    for item in root_path.iterdir():
        if item.is_dir() and chapter_pattern.match(item.name):
            final_article = item / "final_article.md"
            if final_article.exists():
                chapter_folders.append((item, final_article))
    
    if chapter_folders:
        chapter_folders.sort(key=lambda x: natural_sort_key(x[0].name))
        markdown_files = [md_file for _, md_file in chapter_folders]
        print(f"Found {len(markdown_files)} chapters with final_article.md")
    else:
        # Find any .md files
        for item in root_path.rglob("*.md"):
            if item.is_file():
                markdown_files.append(item)
        markdown_files.sort(key=lambda x: natural_sort_key(x.name))
        print(f"Found {len(markdown_files)} markdown files")
    
    return markdown_files

def clean_text_for_processing(text: str) -> str:
    """Clean text of problematic characters that break LaTeX."""
    # Normalize unicode
    text = unicodedata.normalize('NFKC', text)
    
    # Replace problematic characters
    replacements = {
        '"': '"', '"': '"', ''': "'", ''': "'",  # Smart quotes
        '—': '---', '–': '--',  # Dashes
        '…': '...', '′': "'", '″': '"',  # Symbols
        '\u200b': '', '\u200c': '', '\u200d': '', '\ufeff': '',  # Zero-width
        '\u00ad': '', '\xa0': ' ',  # Soft hyphen, non-breaking space
        '«': '"', '»': '"', '‹': "'", '›': "'",  # Angle quotes
        '°': ' degrees', '²': '^2', '³': '^3',  # Superscripts
        '©': '(C)', '®': '(R)', '™': '(TM)',  # Symbols
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def read_file_safely(file_path: Path) -> str:
    """Read file with encoding detection and cleaning."""
    encodings = ['utf-8', 'utf-8-sig', 'cp1252', 'latin-1', 'iso-8859-1']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding, errors='replace') as f:
                content = f.read()
            return clean_text_for_processing(content)
        except:
            continue
    
    # Last resort
    with open(file_path, 'rb') as f:
        raw = f.read()
    content = raw.decode('utf-8', errors='ignore')
    return clean_text_for_processing(content)

def extract_headings_from_markdown(content: str) -> List[Dict]:
    """Extract all headings from markdown content."""
    headings = []
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            heading_text = line[level:].strip()
            if heading_text:
                headings.append({
                    "level": level,
                    "text": heading_text
                })
    
    return headings

def analyze_book_structure(markdown_files: List[Path]) -> List[Dict]:
    """Analyze all markdown files and extract book structure."""
    chapters_data = []
    
    for i, md_file in enumerate(markdown_files, 1):
        print(f"Parsing: {md_file.name}")
        
        try:
            content = read_file_safely(md_file)
            headings = extract_headings_from_markdown(content)
            
            # Get chapter title from first heading or filename
            chapter_title = md_file.stem.replace('_', ' ').title()
            if headings and headings[0]['level'] == 1:
                chapter_title = headings[0]['text']
            
            chapter_data = {
                "chapter_number": i,
                "title": chapter_title,
                "headings": headings,
                "word_count": len(content.split())
            }
            
            chapters_data.append(chapter_data)
            print(f"   {chapter_title} ({len(headings)} headings, {chapter_data['word_count']} words)")
            
        except Exception as e:
            print(f"   Error reading {md_file}: {e}")
    
    return chapters_data

def get_user_input():
    """Get book title and author from user."""
    print("\n" + "="*50)
    print("FRONT MATTER GENERATOR")
    print("="*50)
    
    book_title = input("Enter book title: ").strip()
    if not book_title:
        print("Book title is required!")
        sys.exit(1)
    
    author_name = input("Enter author name: ").strip()
    if not author_name:
        print("Author name is required!")
        sys.exit(1)
    
    # Check for API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("\nError: ANTHROPIC_API_KEY not found in .env file")
        print("Create .env file with: ANTHROPIC_API_KEY=\"your-key\"")
        sys.exit(1)
    
    print("API key loaded from .env file")
    return book_title, author_name, api_key

def create_enhanced_claude_prompt(book_data: Dict) -> str:
    """Create enhanced prompt for detailed front matter generation."""
    
    # Extract chapter titles for better context
    chapter_titles = [ch['title'] for ch in book_data['chapters']]
    chapter_list = "\n".join([f"Chapter {ch['chapter_number']}: {ch['title']}" for ch in book_data['chapters']])
    
    return f"""You are a professional book editor creating front matter for "{book_data['book_title']}" by {book_data['author_name']}.

BOOK STRUCTURE:
{chapter_list}

DETAILED REQUIREMENTS:

1. QUOTE: Create an inspiring 1-2 sentence quote that captures the essence of this book about India's role in global affairs.

2. LETTER TO READERS: Write 250-300 words explaining:
   - What this book offers readers
   - Why it's relevant in today's world  
   - What readers will learn
   - Who should read this book

3. DETAILED PREFACE: Write 400-500 words that includes:
   - Author's motivation for writing this book
   - Why this topic matters now
   - Brief overview of what readers can expect from specific chapters
   - Mention 3-4 key chapters by name and what they cover
   - The book's unique approach or perspective
   - How the book fits into current discussions about India's global role

FORMATTING REQUIREMENTS:
- Use only basic markdown: **bold** and *italic*
- Use simple ASCII punctuation only
- No smart quotes, em-dashes, or special characters
- Write clear, engaging prose
- Make content specific to India's foreign policy and global significance

Respond with ONLY this JSON structure:

{{
  "quote": {{
    "text": "Your inspiring quote about India's global significance",
    "author": null
  }},
  "letter_to_readers": {{
    "title": "Dear Readers",
    "content": "Detailed letter explaining the book's value and relevance..."
  }},
  "preface": {{
    "title": "Preface",
    "content": "Detailed preface mentioning specific chapters, author motivation, and book's unique contribution..."
  }}
}}

Start with {{ and end with }}. No additional text."""

def generate_front_matter(book_data: Dict, api_key: str) -> Dict:
    """Generate detailed front matter using Claude API."""
    print("\nGenerating detailed front matter with Claude API...")
    
    try:
        client = anthropic.Anthropic(api_key=api_key)
        prompt = create_enhanced_claude_prompt(book_data)
        
        print("Sending request to Claude...")
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,  # Increased for detailed preface
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )
        
        response_text = message.content[0].text.strip()
        print("Received response from Claude")
        
        # Parse JSON
        front_matter = json.loads(response_text)
        print("JSON parsed successfully")
        
        # Validate structure
        required = ['quote', 'letter_to_readers', 'preface']
        for field in required:
            if field not in front_matter:
                raise ValueError(f"Missing field: {field}")
        
        return front_matter
        
    except json.JSONDecodeError as e:
        print(f"JSON parsing failed: {e}")
        print(f"Response: {response_text[:200]}...")
        raise
    except Exception as e:
        print(f"Claude API error: {e}")
        raise

def save_json_response(front_matter: Dict, output_dir: Path, book_title: str):
    """Save JSON response to file."""
    safe_title = re.sub(r'[^\w\s-]', '', book_title.lower())
    safe_title = re.sub(r'[-\s]+', '_', safe_title)
    
    json_file = output_dir / f"{safe_title}_front_matter.json"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(front_matter, f, indent=2, ensure_ascii=False)
    
    print(f"JSON saved: {json_file}")
    return json_file

def escape_for_latex(text: str) -> str:
    """Escape text for LaTeX compilation."""
    if not text:
        return ""
    
    # Clean problematic characters first
    text = clean_text_for_processing(text)
    
    # Escape LaTeX special characters
    escapes = {
        '\\': r'\textbackslash{}',
        '{': r'\{', '}': r'\}',
        '$': r'\$', '&': r'\&', 
        '%': r'\%', '#': r'\#',
        '^': r'\^{}', '_': r'\_', 
        '~': r'\textasciitilde{}'
    }
    
    for char, escape in escapes.items():
        text = text.replace(char, escape)
    
    return text

def convert_markdown_to_latex(text: str) -> str:
    """Convert markdown to LaTeX - FIXED VERSION."""
    if not text:
        return ""
    
    # Clean text first
    text = clean_text_for_processing(text)
    
    # Handle markdown with safe placeholders
    text = re.sub(r'\*\*\*([^*]+?)\*\*\*', r'XBOLDITALICX\1XBOLDITALICENDX', text)
    text = re.sub(r'\*\*([^*]+?)\*\*', r'XBOLDX\1XBOLDENDX', text)
    text = re.sub(r'\*([^*]+?)\*', r'XITALICX\1XITALICENDX', text)
    
    # Escape LaTeX characters
    text = escape_for_latex(text)
    
    # Convert to LaTeX commands
    text = text.replace('XBOLDITALICX', r'\textbf{\textit{')
    text = text.replace('XBOLDITALICENDX', '}}')
    text = text.replace('XBOLDX', r'\textbf{')
    text = text.replace('XBOLDENDX', '}')
    text = text.replace('XITALICX', r'\textit{')
    text = text.replace('XITALICENDX', '}')
    
    # Handle line breaks and paragraphs
    text = re.sub(r'\n\s*\n\s*\n+', r'\n\n\\vspace{0.4em}\n\n', text)
    text = re.sub(r'\n\n', r'\n\n\\vspace{0.2em}\n', text)
    
    return text

def create_front_matter_pdf(front_matter: Dict, book_title: str, author_name: str, output_dir: Path):
    """Create PDF with just the front matter content."""
    safe_title = re.sub(r'[^\w\s-]', '', book_title.lower())
    safe_title = re.sub(r'[-\s]+', '_', safe_title)
    
    # Convert all content to LaTeX
    quote_text = convert_markdown_to_latex(front_matter['quote']['text'])
    letter_title = convert_markdown_to_latex(front_matter['letter_to_readers']['title'])
    letter_content = convert_markdown_to_latex(front_matter['letter_to_readers']['content'])
    preface_title = convert_markdown_to_latex(front_matter['preface']['title'])
    preface_content = convert_markdown_to_latex(front_matter['preface']['content'])
    
    clean_title = escape_for_latex(book_title)
    clean_author = escape_for_latex(author_name)
    
    latex_doc = f'''\\documentclass[12pt,a4paper]{{article}}
\\usepackage[T1]{{fontenc}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[english]{{babel}}
\\usepackage{{geometry}}
\\usepackage{{fancyhdr}}
\\usepackage{{titlesec}}
\\usepackage{{hyperref}}
\\usepackage{{parskip}}
\\usepackage{{lmodern}}
\\usepackage{{setspace}}

\\geometry{{
    top=3cm, bottom=3cm,
    left=3cm, right=3cm
}}

\\setstretch{{1.2}}
\\setlength{{\\parskip}}{{0.6em}}
\\setlength{{\\parindent}}{{0pt}}

\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyfoot[C]{{\\thepage}}
\\renewcommand{{\\headrulewidth}}{{0pt}}

\\titleformat{{\\section}}{{\\normalfont\\Large\\bfseries}}{{}}{{0em}}{{}}
\\titleformat{{\\subsection}}{{\\normalfont\\large\\bfseries}}{{}}{{0em}}{{}}

\\hypersetup{{
    colorlinks=true,
    linkcolor=black,
    urlcolor=blue,
    pdftitle={{{clean_title} - Front Matter}},
    pdfauthor={{{clean_author}}}
}}

\\begin{{document}}

% Quote Page
\\begin{{titlepage}}
    \\centering
    \\vspace*{{\\fill}}
    \\begin{{minipage}}{{0.85\\textwidth}}
        \\centering
        \\Large\\textit{{"{quote_text}"}}
        \\vspace{{1cm}}
        
        \\normalsize\\textbf{{From: {clean_title}}}\\\\
        \\normalsize\\textit{{by {clean_author}}}
    \\end{{minipage}}
    \\vspace*{{\\fill}}
\\end{{titlepage}}
\\newpage

% Letter to Readers
\\section*{{{letter_title}}}
{letter_content}

\\newpage

% Detailed Preface  
\\section*{{{preface_title}}}
{preface_content}

\\end{{document}}'''

    # Save and compile
    tex_file = output_dir / f"{safe_title}_front_matter.tex"
    pdf_file = output_dir / f"{safe_title}_front_matter.pdf"
    
    with open(tex_file, 'w', encoding='utf-8', errors='replace') as f:
        f.write(latex_doc)
    
    print(f"LaTeX source saved: {tex_file}")
    
    # Compile to PDF
    return compile_to_pdf(latex_doc, pdf_file), tex_file, pdf_file

def compile_to_pdf(latex_content: str, output_pdf: Path) -> bool:
    """Compile LaTeX to PDF."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        tex_file = temp_path / "front_matter.tex"
        
        with open(tex_file, 'w', encoding='utf-8', errors='replace') as f:
            f.write(latex_content)
        
        try:
            print("Compiling to PDF...")
            
            # Two passes for references
            for i in range(2):
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-output-directory', temp_dir, str(tex_file)],
                    capture_output=True, text=True, cwd=temp_dir
                )
                
                if result.returncode != 0 and i == 1:  # Only show errors on final pass
                    print("LaTeX compilation warnings/errors:")
                    print(result.stdout[-800:])
            
            pdf_file = temp_path / "front_matter.pdf"
            if pdf_file.exists():
                shutil.copy(pdf_file, output_pdf)
                print(f"PDF created: {output_pdf}")
                return True
            else:
                print("PDF generation failed")
                return False
                
        except FileNotFoundError:
            print("pdflatex not found. Install LaTeX: sudo apt-get install texlive-full")
            return False
        except Exception as e:
            print(f"Compilation error: {e}")
            return False

def main():
    """Main function - generates only front matter."""
    print("FRONT MATTER GENERATOR WITH DETAILED PREFACE")
    print("="*60)
    print("Generates: Quote + Letter to Readers + Detailed Preface")
    print("Output: JSON file + PDF with front matter only")
    
    # Get folder path
    if len(sys.argv) > 1:
        folder_path = Path(sys.argv[1])
    else:
        folder_path = Path(input("Enter path to markdown folder: ").strip())
    
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Error: '{folder_path}' is not a valid directory")
        return
    
    # Find markdown files
    print(f"\nScanning: {folder_path}")
    markdown_files = find_markdown_files(folder_path)
    
    if not markdown_files:
        print("No markdown files found!")
        return
    
    # Analyze book structure
    print(f"\nAnalyzing {len(markdown_files)} files...")
    chapters_data = analyze_book_structure(markdown_files)
    
    if not chapters_data:
        print("No valid content found!")
        return
    
    # Show summary
    total_words = sum(ch['word_count'] for ch in chapters_data)
    total_headings = sum(len(ch['headings']) for ch in chapters_data)
    print(f"\nBook Analysis:")
    print(f"   Chapters: {len(chapters_data)}")
    print(f"   Total Words: {total_words:,}")
    print(f"   Total Headings: {total_headings}")
    
    # Get user input
    book_title, author_name, api_key = get_user_input()
    
    # Prepare data for Claude
    book_data = {
        "book_title": book_title,
        "author_name": author_name,
        "total_chapters": len(chapters_data),
        "total_words": total_words,
        "chapters": chapters_data
    }
    
    # Generate front matter with Claude
    try:
        front_matter = generate_front_matter(book_data, api_key)
        
        print("\nFront matter generated!")
        print(f"   Quote: {front_matter['quote']['text'][:60]}...")
        print(f"   Letter: {len(front_matter['letter_to_readers']['content'].split())} words")
        print(f"   Preface: {len(front_matter['preface']['content'].split())} words")
        
    except Exception as e:
        print(f"Failed to generate front matter: {e}")
        return
    
    # Save JSON response
    json_file = save_json_response(front_matter, folder_path, book_title)
    
    # Create PDF with front matter only
    print(f"\nCreating front matter PDF...")
    success, tex_file, pdf_file = create_front_matter_pdf(front_matter, book_title, author_name, folder_path)
    
    if success:
        file_size_kb = pdf_file.stat().st_size / 1024
        
        print(f"\nSUCCESS! Front matter generated.")
        print(f"\nFiles created:")
        print(f"   JSON Response: {json_file}")
        print(f"   PDF (3 pages): {pdf_file} ({file_size_kb:.0f} KB)")
        print(f"   LaTeX Source: {tex_file}")
        
        print(f"\nPDF Contents:")
        print(f"   Page 1: Quote")
        print(f"   Page 2: Letter to Readers")
        print(f"   Page 3: Detailed Preface (with chapter mentions)")
        
        print(f"\nGenerated Quote:")
        print(f'   "{front_matter["quote"]["text"]}"')
        
        print(f"\nPreface Length: {len(front_matter['preface']['content'].split())} words")
    else:
        print("Failed to create PDF")

if __name__ == "__main__":
    # Check for .env file
    if not Path(".env").exists():
        print("Error: .env file not found")
        print("Create .env file with: ANTHROPIC_API_KEY=\"your-key\"")
        sys.exit(1)
    
    main()