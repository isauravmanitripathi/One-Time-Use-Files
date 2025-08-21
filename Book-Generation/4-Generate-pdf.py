#!/usr/bin/env python3
"""
Markdown to PDF Book Generator - COMPLETE FIXED VERSION
Converts chapter markdown files to a professional PDF with LaTeX
Also exports clean text versions of all chapters
FIXES: Watermark visibility, text formatting, paragraph spacing, LaTeX compilation
"""

import os
import re
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import List, Tuple
import math

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

def calculate_watermark_positions(page_width: float, page_height: float, author_name: str):
    """
    Calculate optimal watermark positions with MAXIMUM coverage and visibility.
    """
    # More precise text width calculation
    text_width_cm = len(author_name) * 0.45  # Slightly tighter spacing
    text_height_cm = 0.35
    
    # Minimum gaps between watermarks (very tight but safe)
    min_horizontal_gap = 0.5
    min_vertical_gap = 0.4
    
    # Effective watermark space needed
    watermark_width = text_width_cm + min_horizontal_gap
    watermark_height = text_height_cm + min_vertical_gap
    
    # Smaller margins for maximum coverage
    margin = 0.8
    available_width = page_width - (2 * margin)
    available_height = page_height - (2 * margin)
    
    # Calculate maximum number of watermarks that fit
    horizontal_count = max(3, int(available_width / watermark_width))
    vertical_count = max(4, int(available_height / watermark_height))
    
    # Try to squeeze in more if possible
    if horizontal_count * watermark_width < available_width * 0.85:
        horizontal_count += 1
    if vertical_count * watermark_height < available_height * 0.85:
        vertical_count += 1
    
    # Calculate positions with even spacing
    h_spacing = available_width / (horizontal_count - 1) if horizontal_count > 1 else 0
    v_spacing = available_height / (vertical_count - 1) if vertical_count > 1 else 0
    
    # Generate main grid positions
    h_positions = []
    v_positions = []
    
    for i in range(horizontal_count):
        if horizontal_count == 1:
            h_positions.append(page_width / 2)
        else:
            h_positions.append(margin + i * h_spacing)
    
    for i in range(vertical_count):
        if vertical_count == 1:
            v_positions.append(page_height / 2)
        else:
            v_positions.append(margin + i * v_spacing)
    
    # Generate diagonal offset positions (between main grid)
    h_offset_positions = []
    v_offset_positions = []
    
    if horizontal_count > 1 and vertical_count > 1:
        # Create offset grid with half-spacing
        offset_h_spacing = h_spacing / 2
        offset_v_spacing = v_spacing / 2
        
        # Offset horizontal positions
        for i in range(horizontal_count - 1):
            offset_x = h_positions[i] + offset_h_spacing
            if offset_x + text_width_cm / 2 <= page_width - margin:
                h_offset_positions.append(offset_x)
        
        # Offset vertical positions
        for i in range(vertical_count - 1):
            offset_y = v_positions[i] + offset_v_spacing
            if offset_y + text_height_cm / 2 <= page_height - margin:
                v_offset_positions.append(offset_y)
    
    return h_positions, v_positions, h_offset_positions, v_offset_positions, watermark_width, watermark_height

def get_user_preferences():
    """
    Get user preferences for book generation.
    """
    print("\n" + "="*50)
    print("📚 BOOK GENERATION SETUP - FIXED VERSION")
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
    print("   • Watermarks will be HIGHLY VISIBLE across each page")
    print("   • Maximum coverage with dense grid pattern")
    print("   • Both horizontal and diagonal patterns")
    
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
    
    # Get page size preference
    print("\n📏 Choose the page size for your PDF:")
    print("   1. A4 Standard (21 x 29.7 cm) - Most common")
    print("   2. Publisher Format 1 (16 x 24 cm) - Small book format")
    print("   3. Publisher Format 2 (26 x 27 cm) - Large book format")
    print("   4. US Letter (21.6 x 27.9 cm) - US standard")
    print("   5. Crown Quarto (18.9 x 24.6 cm) - Classic book size")
    print("   6. Royal Octavo (15.6 x 23.4 cm) - Compact book")
    
    page_sizes = {
        '1': ('a4paper', 21, 29.7, 'A4 Standard'),
        '2': ('custom', 16, 24, 'Publisher Format 1'),
        '3': ('custom', 26, 27, 'Publisher Format 2'),
        '4': ('letterpaper', 21.6, 27.9, 'US Letter'),
        '5': ('custom', 18.9, 24.6, 'Crown Quarto'),
        '6': ('custom', 15.6, 23.4, 'Royal Octavo')
    }
    
    while True:
        size_choice = input("Select page size (1-6): ").strip()
        if size_choice in page_sizes:
            page_config = page_sizes[size_choice]
            break
        print("Please enter a number from 1 to 6.")
    
    # Show watermark preview if enabled
    if add_watermark:
        _, page_width, page_height, size_name = page_config
        h_pos, v_pos, h_off, v_off, w_width, w_height = calculate_watermark_positions(
            page_width, page_height, author_name
        )
        total_main = len(h_pos) * len(v_pos)
        total_offset = len(h_off) * len(v_off)
        total_watermarks = total_main + total_offset
        
        print(f"\n🔍 HIGH-DENSITY Watermark preview for {size_name}:")
        print(f"   • Author name: '{author_name}' (≈{len(author_name) * 0.45:.1f}cm wide)")
        print(f"   • Main grid: {len(h_pos)} watermarks per row × {len(v_pos)} rows = {total_main}")
        print(f"   • Diagonal grid: {len(h_off)} × {len(v_off)} = {total_offset} watermarks")
        print(f"   • 🎯 TOTAL WATERMARKS PER PAGE: {total_watermarks}")
        print(f"   • Coverage density: {total_watermarks / (page_width * page_height):.1f} watermarks/cm²")
        print(f"   • Visibility: HIGH (enhanced opacity and contrast)")
    
    print(f"\n✅ Configuration:")
    print(f"   📖 Title: {book_title}")
    print(f"   ✍️  Author: {author_name}")
    print(f"   💧 Watermark: {'YES - High Density' if add_watermark else 'No'}")
    print(f"   🔢 Numbering: {'Yes' if use_numbers else 'No'}")
    print(f"   📑 Subsections in TOC: {'Yes' if include_subsections else 'No'}")
    print(f"   📏 Page Size: {page_config[3]} ({page_config[1]} x {page_config[2]} cm)")
    print()
    
    return book_title, author_name, use_numbers, include_subsections, add_watermark, page_config

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
    Convert markdown formatting to LaTeX with FIXED paragraph handling.
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
    
    # FIXED: Better paragraph handling
    # Replace multiple newlines with proper paragraph breaks
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)  # Clean up excessive breaks
    content = re.sub(r'\n\n', '\n\n\\\\vspace{0.3em}\n', content)  # Add proper spacing
    
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

def create_latex_document(chapters_data: List[Tuple[str, str]], output_path: Path, book_title: str, author_name: str, use_numbers: bool, include_subsections: bool, add_watermark: bool, page_config: Tuple) -> str:
    """
    Create a complete LaTeX document with ENHANCED watermarks and FIXED formatting.
    """
    paper_size, page_width, page_height, size_name = page_config
    
    # LaTeX preamble with better formatting packages
    if paper_size == 'custom':
        latex_doc = f'''\\documentclass[12pt]{{book}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[english]{{babel}}
\\usepackage{{geometry}}
\\usepackage{{fancyhdr}}
\\usepackage{{titlesec}}
\\usepackage{{tocloft}}
\\usepackage{{hyperref}}
\\usepackage{{parskip}}
\\usepackage{{microtype}}
\\usepackage{{tikz}}
\\usepackage{{eso-pic}}
\\usepackage{{xcolor}}
\\usepackage{{setspace}}

% Use a nice font (Latin Modern)
\\usepackage{{lmodern}}

% Custom page geometry for {size_name}
\\geometry{{
    paperwidth={page_width}cm,
    paperheight={page_height}cm,
    top=1.8cm,
    bottom=1.8cm,
    left=2.2cm,
    right=1.8cm,
    headheight=28pt
}}

% Better text spacing
\\setstretch{{1.1}}
\\setlength{{\\parskip}}{{0.4em}}
\\setlength{{\\parindent}}{{0pt}}'''
    else:
        latex_doc = f'''\\documentclass[12pt,{paper_size}]{{book}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[english]{{babel}}
\\usepackage{{geometry}}
\\usepackage{{fancyhdr}}
\\usepackage{{titlesec}}
\\usepackage{{tocloft}}
\\usepackage{{hyperref}}
\\usepackage{{parskip}}
\\usepackage{{microtype}}
\\usepackage{{tikz}}
\\usepackage{{eso-pic}}
\\usepackage{{xcolor}}
\\usepackage{{setspace}}

% Use a nice font (Latin Modern)
\\usepackage{{lmodern}}

% Page geometry for {size_name}
\\geometry{{
    top=2.2cm,
    bottom=2.2cm,
    left=2.8cm,
    right=2.2cm,
    headheight=28pt
}}

% Better text spacing
\\setstretch{{1.1}}
\\setlength{{\\parskip}}{{0.4em}}
\\setlength{{\\parindent}}{{0pt}}'''

    latex_doc += '''

% Headers and footers
\\pagestyle{fancy}
\\fancyhf{}
\\fancyhead[LE,RO]{\\thepage}
\\fancyhead[LO]{\\rightmark}
\\fancyhead[RE]{\\leftmark}
\\renewcommand{\\headrulewidth}{0.4pt}

% Fix header to show chapter names instead of "CONTENTS"
\\renewcommand{\\chaptermark}[1]{\\markboth{\\MakeUppercase{\\chaptername\\ \\thechapter.\\ #1}}{}}
\\renewcommand{\\sectionmark}[1]{\\markright{\\thesection\\ #1}}
'''

    # Add ENHANCED watermark configuration if requested
    if add_watermark:
        # Calculate precise watermark positions
        h_positions, v_positions, h_offset_positions, v_offset_positions, w_width, w_height = calculate_watermark_positions(
            page_width, page_height, author_name
        )
        
        # Format positions for LaTeX
        h_pos_str = "{" + ", ".join([f"{pos:.2f}" for pos in h_positions]) + "}"
        v_pos_str = "{" + ", ".join([f"{pos:.2f}" for pos in v_positions]) + "}"
        
        total_main = len(h_positions) * len(v_positions)
        total_offset = len(h_offset_positions) * len(v_offset_positions)

        latex_doc += f'''

% ENHANCED HIGH-VISIBILITY Watermark configuration for {size_name} ({page_width}x{page_height}cm)
\\newcommand{{\\watermarktext}}{{{author_name}}}

% Create DENSE watermark grid with MAXIMUM visibility
\\AddToShipoutPictureBG{{%
    \\AtPageLowerLeft{{%
        \\begin{{tikzpicture}}[remember picture, overlay]
            % Define ENHANCED watermark style for maximum visibility
            \\tikzset{{
                watermark/.style={{
                    color=gray!40,  % INCREASED visibility (was 25)
                    font=\\fontsize{{9}}{{11}}\\selectfont\\bfseries,  % Optimized size
                    opacity=0.6,    % INCREASED opacity (was 0.4)
                    inner sep=0pt,
                    outer sep=0pt
                }}
            }}
            
            % PRIMARY GRID: {len(h_positions)} × {len(v_positions)} = {total_main} watermarks
            \\foreach \\x in {h_pos_str} {{
                \\foreach \\y in {v_pos_str} {{
                    \\node[watermark, rotate=0] at (\\x cm, \\y cm) {{\\watermarktext}};
                }}
            }}'''
        
        # Add offset positions if they exist
        if h_offset_positions and v_offset_positions:
            h_offset_str = "{" + ", ".join([f"{pos:.2f}" for pos in h_offset_positions]) + "}"
            v_offset_str = "{" + ", ".join([f"{pos:.2f}" for pos in v_offset_positions]) + "}"
            
            latex_doc += f'''
            
            % SECONDARY DIAGONAL GRID: {len(h_offset_positions)} × {len(v_offset_positions)} = {total_offset} watermarks
            \\foreach \\x in {h_offset_str} {{
                \\foreach \\y in {v_offset_str} {{
                    \\node[watermark, rotate=15] at (\\x cm, \\y cm) {{\\watermarktext}};
                }}
            }}'''
        
        latex_doc += f'''
        \\end{{tikzpicture}}
    }}
}}

% TOTAL WATERMARKS PER PAGE: {total_main + total_offset}
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
    Compile LaTeX content to PDF using pdflatex with enhanced error handling.
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
            print("   🔄 Running LaTeX compilation (pass 1/2)...")
            for i in range(2):
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-output-directory', temp_dir, str(tex_file)],
                    capture_output=True,
                    text=True,
                    cwd=temp_dir
                )
                
                if i == 0:
                    print("   🔄 Running LaTeX compilation (pass 2/2)...")
                
                # Check if compilation failed (return code != 0) and no PDF was produced
                pdf_file = temp_path / "document.pdf"
                if result.returncode != 0 and not pdf_file.exists():
                    print(f"❌ LaTeX compilation failed (pass {i+1}):")
                    print("Last 1500 characters of output:")
                    print("-" * 50)
                    print(result.stdout[-1500:])
                    if result.stderr:
                        print("Errors:")
                        print(result.stderr)
                    return False
            
            # Copy the generated PDF to the output location
            if pdf_file.exists():
                shutil.copy(pdf_file, output_pdf)
                print("   ✅ PDF compilation successful!")
                return True
            else:
                print("❌ PDF file was not generated")
                return False
                
        except FileNotFoundError:
            print("❌ Error: pdflatex not found. Please ensure LaTeX is installed.")
            print("   Install LaTeX: sudo apt-get install texlive-full (Ubuntu/Debian)")
            print("   or download from: https://www.latex-project.org/get/")
            return False
        except Exception as e:
            print(f"❌ Error during compilation: {e}")
            return False

def main():
    """
    Main function to orchestrate the PDF generation.
    """
    print("🚀 ENHANCED BOOK GENERATOR - FIXED VERSION")
    print("=" * 60)
    
    # Get user preferences
    book_title, author_name, use_numbers, include_subsections, add_watermark, page_config = get_user_preferences()
    
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
        print("   Make sure you have folders named 'Chapter 1', 'Chapter 2', etc.")
        print("   Each folder should contain a 'final_article.md' file")
        return
    
    print(f"📚 Found {len(chapter_folders)} chapters:")
    for folder in chapter_folders:
        print(f"  ✅ {folder.name}")
    
    # Read all markdown files
    print("\n📖 Reading markdown files...")
    chapters_data = []
    for chapter_folder in chapter_folders:
        title, content = read_markdown_file(chapter_folder, use_numbers)
        if content:
            chapters_data.append((title, content))
            word_count = len(content.split())
            print(f"  ✅ {title} ({word_count:,} words)")
        else:
            print(f"  ❌ Skipped {chapter_folder.name} (no content)")
    
    if not chapters_data:
        print("❌ No valid chapters found!")
        return
    
    total_words = sum(len(content.split()) for _, content in chapters_data)
    print(f"\n📊 Total content: {len(chapters_data)} chapters, {total_words:,} words")
    
    # Create LaTeX document
    print("\n🔧 Generating LaTeX document...")
    
    # Create filename based on book title
    safe_title = re.sub(r'[^\w\s-]', '', book_title.lower())
    safe_title = re.sub(r'[-\s]+', '_', safe_title)
    output_pdf = folder_path / f"{safe_title}.pdf"
    latex_file = folder_path / f"{safe_title}.tex"
    
    latex_content = create_latex_document(chapters_data, output_pdf, book_title, author_name, use_numbers, include_subsections, add_watermark, page_config)
    
    # Save LaTeX source (for debugging)
    with open(latex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    print(f"📄 LaTeX source saved to: {latex_file}")
    
    # Compile to PDF
    print("\n⚙️  Compiling to PDF...")
    if compile_latex_to_pdf(latex_content, output_pdf):
        print(f"\n🎉 SUCCESS! PDF generated successfully!")
        print("\n" + "=" * 60)
        print("📖 BOOK DETAILS:")
        print(f"   Title: {book_title}")
        print(f"   Author: {author_name}")
        print(f"   Chapters: {len(chapters_data)}")
        print(f"   Words: {total_words:,}")
        print(f"   Page Size: {page_config[3]} ({page_config[1]} x {page_config[2]} cm)")
        print(f"   Watermarks: {'ENABLED - High Density' if add_watermark else 'Disabled'}")
        print(f"   Numbering: {'Enabled' if use_numbers else 'Disabled'}")
        print(f"   Subsections in TOC: {'Enabled' if include_subsections else 'Disabled'}")
        
        # Show watermark stats if enabled
        if add_watermark:
            _, page_width, page_height, size_name = page_config
            h_pos, v_pos, h_off, v_off, _, _ = calculate_watermark_positions(
                page_width, page_height, author_name
            )
            total_watermarks = len(h_pos) * len(v_pos) + len(h_off) * len(v_off)
            print(f"   Watermarks per page: {total_watermarks}")
        
        # Save chapters as text files
        text_folder = save_chapters_as_text(chapters_data, folder_path, safe_title)
        
        print("\n" + "=" * 60)
        print("✨ FILES GENERATED:")
        print(f"   📕 PDF Book: {output_pdf}")
        print(f"   📄 LaTeX Source: {latex_file}")
        print(f"   📁 Text Chapters: {text_folder}")
        
        # Calculate file size
        try:
            pdf_size_mb = output_pdf.stat().st_size / (1024 * 1024)
            print(f"   📊 PDF Size: {pdf_size_mb:.1f} MB")
        except:
            pass
        
        print("\n🎯 Your book is ready! Check the PDF for:")
        if add_watermark:
            print("   ✅ High-density watermarks (both horizontal and diagonal)")
        print("   ✅ Professional formatting")
        print("   ✅ Clickable table of contents")
        print("   ✅ Proper headers and page numbers")
        print("   ✅ Clean text export for reference")
        
    else:
        print("\n❌ Failed to generate PDF.")
        print(f"📄 Check the LaTeX source file for issues: {latex_file}")
        print("💡 Common issues:")
        print("   • LaTeX not installed (install texlive)")
        print("   • Special characters in content")
        print("   • Missing fonts")

if __name__ == "__main__":
    main()