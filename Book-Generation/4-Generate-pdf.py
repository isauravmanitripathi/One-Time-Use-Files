#!/usr/bin/env python3
"""
Markdown to PDF Book Generator
Converts chapter markdown files to a professional PDF with LaTeX
Also exports clean text versions of all chapters
"""

import os
import re
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import List, Tuple

def natural_sort_key(s: str) -> List:
    """
    Sort strings containing numbers in a natural way.
    E.g., Chapter 1, Chapter 2, ..., Chapter 10 (not Chapter 1, Chapter 10, Chapter 2)
    """
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split(r'(\d+)', s)]

def get_chapter_folders(root_path: Path) -> List[Path]:
    """
    Find and sort all chapter folders in natural order.
    """
    chapter_folders = []
    pattern = re.compile(r'^Chapter\s+\d+$', re.IGNORECASE)
    
    for item in root_path.iterdir():
        if item.is_dir() and pattern.match(item.name):
            chapter_folders.append(item)
    
    # Sort chapters naturally (Chapter 1, 2, ..., 10, not 1, 10, 2)
    chapter_folders.sort(key=lambda x: natural_sort_key(x.name))
    return chapter_folders

def get_user_preferences():
    """
    Get user preferences for book generation.
    """
    print("\n" + "="*50)
    print("📚 BOOK GENERATION SETUP")
    print("="*50)
    
    # Get book title
    book_title = input("📖 Enter the book title: ").strip()
    if not book_title:
        book_title = "Generated Book"
    
    # Get author name
    author_name = input("✍️  Enter the author name: ").strip()
    if not author_name:
        author_name = "Unknown Author"
    
    # Get watermark preference
    print("\n💧 Do you want to add watermarks to the PDF?")
    print("   • Watermarks will display the author's name diagonally across each page")
    print("   • They will be light but OCR-detectable")
    print("   • Multiple watermarks per page for better protection")
    
    while True:
        watermark_choice = input("Add watermarks? (y/n): ").strip().lower()
        if watermark_choice in ['y', 'yes', 'n', 'no']:
            add_watermark = watermark_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    # Get numbering preference
    print("\n🔢 Do you want to include numbers in chapters and sections?")
    print("   • With numbers: 'Chapter 1', '1.1 Introduction', etc.")
    print("   • Without numbers: Just the title text, no numbering")
    
    while True:
        numbering_choice = input("Include numbering? (y/n): ").strip().lower()
        if numbering_choice in ['y', 'yes', 'n', 'no']:
            use_numbers = numbering_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    # Get table of contents subsection preference
    print("\n📑 Do you want to include subsections in the table of contents?")
    if use_numbers:
        print("   • With subsections: Shows '1.1 Introduction', '1.2 Overview', etc. in TOC")
        print("   • Without subsections: Shows only chapter titles in TOC")
    else:
        print("   • With subsections: Shows 'Introduction', 'Overview', etc. in TOC")
        print("   • Without subsections: Shows only chapter titles in TOC")
    
    while True:
        subsections_choice = input("Include subsections in table of contents? (y/n): ").strip().lower()
        if subsections_choice in ['y', 'yes', 'n', 'no']:
            include_subsections = subsections_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    print(f"\n✅ Configuration:")
    print(f"   📖 Title: {book_title}")
    print(f"   ✍️  Author: {author_name}")
    print(f"   💧 Watermark: {'Yes' if add_watermark else 'No'}")
    print(f"   🔢 Numbering: {'Yes' if use_numbers else 'No'}")
    print(f"   📑 Subsections in TOC: {'Yes' if include_subsections else 'No'}")
    print()
    
    return book_title, author_name, use_numbers, include_subsections, add_watermark

def read_markdown_file(chapter_path: Path, use_numbers: bool) -> Tuple[str, str]:
    """
    Read the markdown content from final_article.md in the chapter folder.
    Returns tuple of (chapter_title, content)
    """
    md_file = chapter_path / "final_article.md"
    if not md_file.exists():
        print(f"Warning: {md_file} not found, skipping chapter")
        return None, None
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract chapter title based on user preference
    if use_numbers:
        chapter_match = re.search(r'Chapter\s+(\d+)', chapter_path.name, re.IGNORECASE)
        if chapter_match:
            chapter_num = chapter_match.group(1)
            chapter_title = f"Chapter {chapter_num}"
        else:
            chapter_title = chapter_path.name
    else:
        # Extract just the text without "Chapter X" prefix
        # Look for the first heading in the markdown content
        lines = content.split('\n')
        chapter_title = "Untitled Chapter"
        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                # Remove markdown heading syntax and use as title
                chapter_title = re.sub(r'^#+\s*', '', line).strip()
                break
    
    return chapter_title, content

def escape_latex(text: str) -> str:
    """
    Escape special LaTeX characters in text.
    """
    # Dictionary of LaTeX special characters and their escaped versions
    special_chars = {
        '\\': r'\textbackslash{}',
        '{': r'\{',
        '}': r'\}',
        '$': r'\$',
        '&': r'\&',
        '#': r'\#',
        '^': r'\^{}',
        '_': r'\_',
        '~': r'\textasciitilde{}',
        '%': r'\%',
    }
    
    # First replace backslash, then others
    text = text.replace('\\', special_chars['\\'])
    for char, replacement in special_chars.items():
        if char != '\\':  # Skip backslash as we already handled it
            text = text.replace(char, replacement)
    
    return text

def markdown_to_latex(content: str, use_numbers: bool) -> str:
    """
    Convert markdown formatting to LaTeX.
    """
    # Handle code blocks first (to preserve their content)
    code_blocks = []
    
    # Store code blocks temporarily
    def store_code_block(match):
        code_blocks.append(match.group(0))
        return f"<<<CODEBLOCK_{len(code_blocks)-1}>>>"
    
    # Match fenced code blocks
    content = re.sub(r'```[\s\S]*?```', store_code_block, content)
    
    # Handle inline code before escaping
    content = re.sub(r'`([^`]+)`', r'\\texttt{\1}', content)
    
    # Now escape LaTeX special characters (but not in code blocks)
    lines = content.split('\n')
    processed_lines = []
    
    for line in lines:
        if not line.startswith('<<<CODEBLOCK_'):
            # Headers (before escaping to preserve the # symbol for processing)
            if use_numbers:
                # With numbers - use standard sectioning
                if line.startswith('######'):
                    line = re.sub(r'^######\s+(.+)$', r'\\subparagraph{\1}', line)
                elif line.startswith('#####'):
                    line = re.sub(r'^#####\s+(.+)$', r'\\paragraph{\1}', line)
                elif line.startswith('####'):
                    line = re.sub(r'^####\s+(.+)$', r'\\subsubsection{\1}', line)
                elif line.startswith('###'):
                    line = re.sub(r'^###\s+(.+)$', r'\\subsection{\1}', line)
                elif line.startswith('##'):
                    line = re.sub(r'^##\s+(.+)$', r'\\section{\1}', line)
                elif line.startswith('#'):
                    line = re.sub(r'^#\s+(.+)$', r'\\section{\1}', line)
            else:
                # Without numbers - use starred versions (no numbering)
                if line.startswith('######'):
                    line = re.sub(r'^######\s+(.+)$', r'\\subparagraph*{\1}', line)
                elif line.startswith('#####'):
                    line = re.sub(r'^#####\s+(.+)$', r'\\paragraph*{\1}', line)
                elif line.startswith('####'):
                    line = re.sub(r'^####\s+(.+)$', r'\\subsubsection*{\1}', line)
                elif line.startswith('###'):
                    line = re.sub(r'^###\s+(.+)$', r'\\subsection*{\1}', line)
                elif line.startswith('##'):
                    line = re.sub(r'^##\s+(.+)$', r'\\section*{\1}', line)
                elif line.startswith('#'):
                    line = re.sub(r'^#\s+(.+)$', r'\\section*{\1}', line)
            
            # Only escape if it's not a LaTeX command we just added
            if not line.startswith('\\'):
                line = escape_latex(line)
        
        processed_lines.append(line)
    
    content = '\n'.join(processed_lines)
    
    # Bold and italic (after escaping)
    content = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\textit{\1}}', content)
    content = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', content)
    content = re.sub(r'\*(.+?)\*', r'\\textit{\1}', content)
    
    # Lists
    content = re.sub(r'^\*\s+', r'\\item ', content, flags=re.MULTILINE)
    content = re.sub(r'^-\s+', r'\\item ', content, flags=re.MULTILINE)
    content = re.sub(r'^\d+\.\s+', r'\\item ', content, flags=re.MULTILINE)
    
    # Wrap list items in itemize environment
    lines = content.split('\n')
    in_list = False
    processed_lines = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('\\item'):
            if not in_list:
                processed_lines.append('\\begin{itemize}')
                in_list = True
            processed_lines.append(line)
        else:
            if in_list and line.strip() == '':
                # Check if next non-empty line is also a list item
                next_is_item = False
                for j in range(i+1, len(lines)):
                    if lines[j].strip():
                        if lines[j].strip().startswith('\\item'):
                            next_is_item = True
                        break
                
                if not next_is_item:
                    processed_lines.append('\\end{itemize}')
                    in_list = False
            processed_lines.append(line)
    
    if in_list:
        processed_lines.append('\\end{itemize}')
    
    content = '\n'.join(processed_lines)
    
    # Restore code blocks with proper formatting
    for i, code_block in enumerate(code_blocks):
        # Extract language and code
        match = re.match(r'```(\w*)\n([\s\S]*?)```', code_block)
        if match:
            lang = match.group(1) or 'text'
            code = match.group(2)
            # Use verbatim for code blocks
            latex_code = f"\\begin{{verbatim}}\n{code}\\end{{verbatim}}"
            content = content.replace(f"<<<CODEBLOCK_{i}>>>", latex_code)
    
    # Handle paragraphs (double newline = new paragraph) - FIXED
    # Use proper LaTeX paragraph spacing instead of problematic vspace
    content = re.sub(r'\n\n+', '\n\n\\\\par\n\\\\vspace{0.5em}\n', content)
    
    return content

def clean_markdown_to_text(content: str) -> str:
    """
    Convert markdown content to clean plain text by removing all markdown formatting.
    """
    # Remove code blocks first
    content = re.sub(r'```[\s\S]*?```', '', content)
    
    # Remove inline code
    content = re.sub(r'`([^`]+)`', r'\1', content)
    
    # Remove headers (keep the text, remove the # symbols)
    content = re.sub(r'^#+\s*(.+)$', r'\1', content, flags=re.MULTILINE)
    
    # Remove bold and italic formatting
    content = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', content)  # Bold italic
    content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)      # Bold
    content = re.sub(r'\*(.+?)\*', r'\1', content)          # Italic
    content = re.sub(r'__(.+?)__', r'\1', content)          # Alternative bold
    content = re.sub(r'_(.+?)_', r'\1', content)            # Alternative italic
    
    # Remove strikethrough
    content = re.sub(r'~~(.+?)~~', r'\1', content)
    
    # Remove links but keep the text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)  # [text](url)
    content = re.sub(r'<([^>]+)>', r'\1', content)               # <url>
    
    # Remove images
    content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', content)
    
    # Convert lists to simple text
    content = re.sub(r'^\s*[-*+]\s+', '• ', content, flags=re.MULTILINE)  # Bullet lists
    content = re.sub(r'^\s*\d+\.\s+', '• ', content, flags=re.MULTILINE)  # Numbered lists
    
    # Remove horizontal rules
    content = re.sub(r'^[-*_]{3,}$', '', content, flags=re.MULTILINE)
    
    # Remove blockquotes
    content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)
    
    # Remove tables (simple approach - remove table formatting)
    content = re.sub(r'\|', ' ', content)  # Remove pipe characters
    content = re.sub(r'^[-\s:]+$', '', content, flags=re.MULTILINE)  # Remove table separators
    
    # Clean up excessive whitespace
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)  # Multiple blank lines to double
    content = re.sub(r'[ \t]+', ' ', content)             # Multiple spaces to single
    content = re.sub(r'^\s+', '', content, flags=re.MULTILINE)  # Leading whitespace
    content = re.sub(r'\s+$', '', content, flags=re.MULTILINE)  # Trailing whitespace
    
    # Remove any remaining markdown artifacts
    content = re.sub(r'\\(.)', r'\1', content)  # Remove escaped characters
    
    return content.strip()

def save_chapters_as_text(chapters_data: List[Tuple[str, str]], base_path: Path, folder_name: str):
    """
    Save all chapters as clean text files in a separate folder.
    """
    # Create the text chapters folder
    text_folder = base_path / f"{folder_name}_chapters_text"
    text_folder.mkdir(exist_ok=True)
    
    print(f"\n📝 Saving chapters as text files in: {text_folder}")
    
    for i, (chapter_title, content) in enumerate(chapters_data, 1):
        if content:
            # Clean the markdown content to plain text
            clean_text = clean_markdown_to_text(content)
            
            # Create a safe filename
            safe_chapter_name = re.sub(r'[^\w\s-]', '', chapter_title.lower())
            safe_chapter_name = re.sub(r'[-\s]+', '_', safe_chapter_name)
            
            # Add chapter number for ordering
            text_filename = f"chapter_{i:02d}_{safe_chapter_name}.txt"
            text_file_path = text_folder / text_filename
            
            # Write the clean text to file
            with open(text_file_path, 'w', encoding='utf-8') as f:
                f.write(f"{chapter_title}\n")
                f.write("=" * len(chapter_title) + "\n\n")
                f.write(clean_text)
            
            print(f"  ✅ {text_filename}")
    
    print(f"📁 Text chapters saved to: {text_folder}")
    return text_folder

def create_latex_document(chapters_data: List[Tuple[str, str]], output_path: Path, book_title: str, author_name: str, use_numbers: bool, include_subsections: bool, add_watermark: bool) -> str:
    """
    Create a complete LaTeX document from chapters data.
    """
    # LaTeX preamble with nice formatting
    latex_doc = r'''\documentclass[12pt,a4paper]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{tocloft}
\usepackage{hyperref}
\usepackage{parskip}
\usepackage{microtype}
\usepackage{tikz}
\usepackage{eso-pic}
\usepackage{xcolor}

% Use a nice font (Latin Modern)
\usepackage{lmodern}

% Page geometry
\geometry{
    top=2.5cm,
    bottom=2.5cm,
    left=3cm,
    right=2.5cm,
    headheight=28pt
}

% Headers and footers
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\rightmark}
\fancyhead[RE]{\leftmark}
\renewcommand{\headrulewidth}{0.4pt}

% Fix header to show chapter names instead of "CONTENTS"
\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{\chaptername\ \thechapter.\ #1}}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}
'''

    # Add watermark configuration if requested - FIXED SPACING
    if add_watermark:
        latex_doc += f'''

% Watermark configuration
\\newcommand{{\\watermarktext}}{{{author_name}}}

% Create the watermark with proper spacing to avoid overlap
\\AddToShipoutPictureBG{{%
    \\AtPageLowerLeft{{%
        \\begin{{tikzpicture}}[remember picture, overlay]
            % Define watermark style
            \\tikzset{{
                watermark/.style={{
                    color=gray!30,
                    font=\\fontsize{{12}}{{14}}\\selectfont\\bfseries,
                    opacity=0.4
                }}
            }}
            
            % Calculate proper spacing based on text width
            % Each watermark needs about 4cm width minimum to avoid overlap
            % Page is about 21cm wide, so we can fit 4-5 watermarks horizontally
            % Page is about 29.7cm tall, so we can fit 7-8 watermarks vertically
            
            % Horizontal watermarks with proper spacing
            \\foreach \\x in {{2, 6.5, 11, 15.5}} {{
                \\foreach \\y in {{2, 4.5, 7, 9.5, 12, 14.5, 17, 19.5, 22, 24.5, 27}} {{
                    \\node[watermark, rotate=0] at (\\x cm, \\y cm) {{\\watermarktext}};
                }}
            }}
            
            % Add diagonal watermarks for better coverage (optional)
            % Offset pattern with diagonal rotation for additional protection
            \\foreach \\x in {{4.25, 8.75, 13.25}} {{
                \\foreach \\y in {{3.25, 5.75, 8.25, 10.75, 13.25, 15.75, 18.25, 20.75, 23.25, 25.75}} {{
                    \\node[watermark, rotate=15] at (\\x cm, \\y cm) {{\\watermarktext}};
                }}
            }}
        \\end{{tikzpicture}}
    }}
}}
'''

    latex_doc += '''
% Chapter formatting'''

    if use_numbers:
        latex_doc += r'''
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}
{\chaptertitlename\ \thechapter}
{20pt}
{\Huge}

% Section formatting
\titleformat{\section}
{\normalfont\Large\bfseries}
{\thesection}
{1em}
{}

\titleformat{\subsection}
{\normalfont\large\bfseries}
{\thesubsection}
{1em}
{}
'''
    else:
        latex_doc += r'''
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}
{}
{20pt}
{\Huge}

% Section formatting (without numbers)
\titleformat{\section}
{\normalfont\Large\bfseries}
{}
{1em}
{}

\titleformat{\subsection}
{\normalfont\large\bfseries}
{}
{1em}
{}

% Fix headers for unnumbered chapters
\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{#1}}{}}
\renewcommand{\sectionmark}[1]{\markright{#1}}
'''

    # Table of contents depth control
    if include_subsections:
        toc_depth = "2"  # Show chapters, sections, and subsections
    else:
        toc_depth = "0"  # Show only chapters

    latex_doc += f'''
% Table of contents formatting
\\setcounter{{tocdepth}}{{{toc_depth}}}
\\renewcommand{{\\cftchapfont}}{{\\bfseries}}
\\renewcommand{{\\cftsecfont}}{{\\normalfont}}
\\renewcommand{{\\cftsubsecfont}}{{\\normalfont}}

% Hyperref setup
\\hypersetup{{
    colorlinks=true,
    linkcolor=black,
    filecolor=black,
    urlcolor=blue,
    pdftitle={{{book_title}}},
    pdfauthor={{{author_name}}},
    bookmarks=true,
    bookmarksopen=true,
    bookmarksnumbered=true,
    pdfstartview={{FitH}},
    pdfpagemode={{UseOutlines}}
}}

% Start document
\\begin{{document}}

% Title page
\\begin{{titlepage}}
    \\centering
    \\vspace*{{5cm}}
    {{\\Huge\\bfseries {book_title}\\par}}
    \\vspace{{2cm}}
    {{\\Large by {author_name}\\par}}
    \\vfill
    {{\\large \\today\\par}}
\\end{{titlepage}}

% Table of contents
\\tableofcontents
\\clearpage

% Main content
'''

    # Add each chapter
    for chapter_title, content in chapters_data:
        if content:
            latex_content = markdown_to_latex(content, use_numbers)
            if use_numbers:
                latex_doc += f"\n\\chapter{{{chapter_title}}}\n"
            else:
                latex_doc += f"\n\\chapter*{{{chapter_title}}}\n"
                # Add to TOC manually for unnumbered chapters
                latex_doc += f"\\addcontentsline{{toc}}{{chapter}}{{{chapter_title}}}\n"
                # Mark the chapter for headers
                latex_doc += f"\\markboth{{\\MakeUppercase{{{chapter_title}}}}}{{\\MakeUppercase{{{chapter_title}}}}}\n"
            latex_doc += latex_content
            latex_doc += "\n\\clearpage\n"
    
    # End document
    latex_doc += r'''
\end{document}
'''
    
    return latex_doc

def compile_latex_to_pdf(latex_content: str, output_pdf: Path) -> bool:
    """
    Compile LaTeX content to PDF using pdflatex.
    """
    # Create a temporary directory for LaTeX compilation
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        tex_file = temp_path / "document.tex"
        
        # Write LaTeX content to file
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        # Run pdflatex twice to resolve references
        try:
            for i in range(2):
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-output-directory', temp_dir, str(tex_file)],
                    capture_output=True,
                    text=True,
                    cwd=temp_dir
                )
                
                # Check if compilation failed (return code != 0) and no PDF was produced
                pdf_file = temp_path / "document.pdf"
                if result.returncode != 0 and not pdf_file.exists():
                    print(f"LaTeX compilation failed (pass {i+1}):")
                    print(result.stdout[-2000:])  # Print last 2000 chars of output
                    print(result.stderr)
                    return False
            
            # Copy the generated PDF to the output location
            if pdf_file.exists():
                shutil.copy(pdf_file, output_pdf)
                return True
            else:
                print("PDF file was not generated")
                return False
                
        except FileNotFoundError:
            print("Error: pdflatex not found. Please ensure LaTeX is installed.")
            return False
        except Exception as e:
            print(f"Error during compilation: {e}")
            return False

def main():
    """
    Main function to orchestrate the PDF generation.
    """
    # Get user preferences
    book_title, author_name, use_numbers, include_subsections, add_watermark = get_user_preferences()
    
    # Get the folder path from user
    if len(sys.argv) > 1:
        folder_path = Path(sys.argv[1])
    else:
        folder_path = Path(input("📁 Enter the path to the folder containing chapters: ").strip())
    
    # Validate path
    if not folder_path.exists():
        print(f"❌ Error: Path '{folder_path}' does not exist")
        return
    
    if not folder_path.is_dir():
        print(f"❌ Error: '{folder_path}' is not a directory")
        return
    
    print(f"\n🔍 Processing chapters in: {folder_path}")
    
    # Get and sort chapter folders
    chapter_folders = get_chapter_folders(folder_path)
    
    if not chapter_folders:
        print("❌ No chapter folders found!")
        return
    
    print(f"📚 Found {len(chapter_folders)} chapters:")
    for folder in chapter_folders:
        print(f"  - {folder.name}")
    
    # Read all markdown files
    print("\n📖 Reading markdown files...")
    chapters_data = []
    for chapter_folder in chapter_folders:
        title, content = read_markdown_file(chapter_folder, use_numbers)
        if content:
            chapters_data.append((title, content))
            print(f"  ✅ {title}")
        else:
            print(f"  ❌ Skipped {chapter_folder.name} (no content)")
    
    if not chapters_data:
        print("❌ No valid chapters found!")
        return
    
    # Create LaTeX document
    print("\n🔧 Generating LaTeX document...")
    
    # Create filename based on book title
    safe_title = re.sub(r'[^\w\s-]', '', book_title.lower())
    safe_title = re.sub(r'[-\s]+', '_', safe_title)
    output_pdf = folder_path / f"{safe_title}.pdf"
    latex_file = folder_path / f"{safe_title}.tex"
    
    latex_content = create_latex_document(chapters_data, output_pdf, book_title, author_name, use_numbers, include_subsections, add_watermark)
    
    # Save LaTeX source (optional, for debugging)
    with open(latex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    print(f"📄 LaTeX source saved to: {latex_file}")
    
    # Compile to PDF
    print("\n⚙️  Compiling to PDF...")
    if compile_latex_to_pdf(latex_content, output_pdf):
        print(f"\n🎉 Success! PDF generated at: {output_pdf}")
        print(f"📖 Title: {book_title}")
        print(f"✍️  Author: {author_name}")
        print(f"💧 Watermark: {'Enabled' if add_watermark else 'Disabled'}")
        print(f"🔢 Numbering: {'Enabled' if use_numbers else 'Disabled'}")
        print(f"📑 Subsections in TOC: {'Enabled' if include_subsections else 'Disabled'}")
        
        # Save chapters as text files
        text_folder = save_chapters_as_text(chapters_data, folder_path, safe_title)
        
        print(f"\n✨ All files generated:")
        print(f"   📕 PDF: {output_pdf}")
        print(f"   📄 LaTeX: {latex_file}")
        print(f"   📁 Text chapters: {text_folder}")
        
    else:
        print("\n❌ Failed to generate PDF. Check the LaTeX source for errors.")
        print(f"📄 You can manually compile the LaTeX file: {latex_file}")

if __name__ == "__main__":
    main()