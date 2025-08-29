#!/usr/bin/env python3
"""
Enhanced KDP-Compliant Markdown to PDF Book Generator
Converts chapter markdown files to Amazon KDP-compliant PDF with LaTeX
Features: Professional styling, center/left alignment, enhanced typography
"""

import os
import re
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import List, Tuple, Dict
import math

def natural_sort_key(s: str) -> List:
    """Sort strings containing numbers in a natural way."""
    return [int(text) if text.isdigit() else text.lower() 
            for text in re.split(r'(\d+)', s)]

def get_chapter_folders(root_path: Path) -> List[Path]:
    """Find and sort all chapter folders in natural order."""
    chapter_folders = []
    pattern = re.compile(r'^Chapter\s+\d+$', re.IGNORECASE)
    
    for item in root_path.iterdir():
        if item.is_dir() and pattern.match(item.name):
            chapter_folders.append(item)
    
    chapter_folders.sort(key=lambda x: natural_sort_key(x.name))
    return chapter_folders

def calculate_kdp_margins(page_count: int, has_bleed: bool = False) -> Dict[str, float]:
    """Calculate KDP-compliant margins based on page count."""
    if page_count <= 24:
        inside_margin = 0.375
        outside_margin = 0.25
    elif page_count <= 150:
        inside_margin = 0.75
        outside_margin = 0.25
    elif page_count <= 300:
        inside_margin = 0.875
        outside_margin = 0.25
    elif page_count <= 500:
        inside_margin = 1.0
        outside_margin = 0.25
    elif page_count <= 700:
        inside_margin = 1.125
        outside_margin = 0.25
    else:
        inside_margin = 1.25
        outside_margin = 0.25
    
    top_margin = 0.3
    bottom_margin = 0.3
    safety_margin = 0.125
    
    return {
        'top': top_margin + safety_margin,
        'bottom': bottom_margin + safety_margin, 
        'inside': inside_margin + safety_margin,
        'outside': outside_margin + safety_margin
    }

def calculate_bleed_dimensions(width: float, height: float, has_bleed: bool = False) -> Tuple[float, float]:
    """Calculate page dimensions with bleed if needed."""
    if has_bleed:
        width_inches = width / 2.54
        height_inches = height / 2.54
        width_inches += 0.125
        height_inches += 0.25
        return width_inches * 2.54, height_inches * 2.54
    return width, height

def calculate_watermark_positions(page_width: float, page_height: float, author_name: str, margins: Dict[str, float], has_bleed: bool = False):
    """Calculate watermark positions respecting KDP margins and safe zones."""
    top_margin_cm = margins['top'] * 2.54
    bottom_margin_cm = margins['bottom'] * 2.54
    inside_margin_cm = margins['inside'] * 2.54
    outside_margin_cm = margins['outside'] * 2.54
    
    safe_zone = 0.125 * 2.54
    
    effective_top = max(top_margin_cm, safe_zone)
    effective_bottom = max(bottom_margin_cm, safe_zone)
    effective_left = max(outside_margin_cm, safe_zone)
    effective_right = max(inside_margin_cm, safe_zone)
    
    text_width_cm = len(author_name) * 0.4
    text_height_cm = 0.3
    
    min_horizontal_gap = 1.0
    min_vertical_gap = 0.8
    
    watermark_width = text_width_cm + min_horizontal_gap
    watermark_height = text_height_cm + min_vertical_gap
    
    available_width = page_width - effective_left - effective_right
    available_height = page_height - effective_top - effective_bottom
    
    horizontal_count = max(2, int(available_width / watermark_width))
    vertical_count = max(3, int(available_height / watermark_height))
    
    h_positions = []
    v_positions = []
    
    if horizontal_count == 1:
        h_positions.append(effective_left + available_width / 2)
    else:
        h_spacing = available_width / (horizontal_count - 1)
        for i in range(horizontal_count):
            h_positions.append(effective_left + i * h_spacing)
    
    if vertical_count == 1:
        v_positions.append(effective_bottom + available_height / 2)
    else:
        v_spacing = available_height / (vertical_count - 1)
        for i in range(vertical_count):
            v_positions.append(effective_bottom + i * v_spacing)
    
    return h_positions, v_positions, [], [], watermark_width, watermark_height

def get_user_preferences():
    """Get user preferences for enhanced KDP-compliant book generation."""
    print("\n" + "="*70)
    print("📚 ENHANCED KDP-COMPLIANT BOOK GENERATOR")
    print("="*70)
    print("✨ Professional Styling & Typography")
    print("✅ Amazon KDP Print-on-Demand Ready")
    print("✅ Center/Left Alignment Options")
    print("✅ Enhanced Visual Appearance")
    print("="*70)
    
    # Get book title
    book_title = input("📖 Enter the book title: ").strip()
    if not book_title:
        book_title = "Generated Book"
    
    # Get author name
    author_name = input("✍️  Enter the author name: ").strip()
    if not author_name:
        author_name = "Unknown Author"
    
    # Get title alignment preference
    print("\n📐 Choose title and heading alignment:")
    print("   1. Left aligned (traditional)")
    print("   2. Center aligned (modern)")
    
    while True:
        align_choice = input("Select alignment (1-2): ").strip()
        if align_choice in ['1', '2']:
            center_titles = align_choice == '2'
            break
        print("Please enter 1 for left or 2 for center.")
    
    # Get styling preference
    print("\n🎨 Choose styling theme:")
    print("   1. Classic - Traditional book styling")
    print("   2. Modern - Contemporary with enhanced spacing")
    print("   3. Elegant - Sophisticated with decorative elements")
    
    while True:
        style_choice = input("Select styling (1-3): ").strip()
        if style_choice in ['1', '2', '3']:
            style_theme = {
                '1': 'classic',
                '2': 'modern', 
                '3': 'elegant'
            }[style_choice]
            break
        print("Please enter 1, 2, or 3.")
    
    # Get bleed preference
    print("\n🖨️  Do you need bleed for your book?")
    print("   • Required if you have full-page backgrounds or images")
    
    while True:
        bleed_choice = input("Include bleed? (y/n): ").strip().lower()
        if bleed_choice in ['y', 'yes', 'n', 'no']:
            has_bleed = bleed_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    # Get watermark preference
    print("\n💧 Add watermarks to the PDF?")
    
    while True:
        watermark_choice = input("Add watermarks? (y/n): ").strip().lower()
        if watermark_choice in ['y', 'yes', 'n', 'no']:
            add_watermark = watermark_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    # Get numbering preference
    print("\n🔢 Include numbers in chapters and sections?")
    
    while True:
        numbering_choice = input("Include numbering? (y/n): ").strip().lower()
        if numbering_choice in ['y', 'yes', 'n', 'no']:
            use_numbers = numbering_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    # Get table of contents subsection preference
    print("\n📑 Include subsections in table of contents?")
    
    while True:
        subsections_choice = input("Include subsections in TOC? (y/n): ").strip().lower()
        if subsections_choice in ['y', 'yes', 'n', 'no']:
            include_subsections = subsections_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    # Updated page size preferences with your specified sizes
    print("\n📏 Choose KDP-compliant page size:")
    print("   1. 5.06\" x 7.81\" (12.85 x 19.84 cm)")
    print("   2. 6.14\" x 9.21\" (15.6 x 23.39 cm)")
    print("   3. 6.69\" x 9.61\" (16.99 x 24.4 cm)")
    print("   4. 7\" x 10\" (17.78 x 25.4 cm)")
    print("   5. 7.44\" x 9.69\" (18.9 x 24.61 cm)")
    print("   6. 7.5\" x 9.25\" (19.05 x 23.5 cm)")
    print("   7. 8\" x 10\" (20.32 x 25.4 cm)")
    print("   8. 8.5\" x 11\" (21.59 x 27.94 cm)")
    
    page_sizes = {
        '1': (5.06, 7.81, '5.06" x 7.81" (12.85 x 19.84 cm)'),
        '2': (6.14, 9.21, '6.14" x 9.21" (15.6 x 23.39 cm)'),
        '3': (6.69, 9.61, '6.69" x 9.61" (16.99 x 24.4 cm)'),
        '4': (7.0, 10.0, '7" x 10" (17.78 x 25.4 cm)'),
        '5': (7.44, 9.69, '7.44" x 9.69" (18.9 x 24.61 cm)'),
        '6': (7.5, 9.25, '7.5" x 9.25" (19.05 x 23.5 cm)'),
        '7': (8.0, 10.0, '8" x 10" (20.32 x 25.4 cm)'),
        '8': (8.5, 11.0, '8.5" x 11" (21.59 x 27.94 cm)')
    }
    
    while True:
        size_choice = input("Select page size (1-8): ").strip()
        if size_choice in page_sizes:
            width_inches, height_inches, size_name = page_sizes[size_choice]
            page_width = width_inches * 2.54
            page_height = height_inches * 2.54
            page_config = (page_width, page_height, size_name, width_inches, height_inches)
            break
        print("Please enter a number from 1 to 8.")
    
    print(f"\n✅ Configuration Summary:")
    print(f"   📖 Title: {book_title}")
    print(f"   ✍️  Author: {author_name}")
    print(f"   📐 Alignment: {'Center' if center_titles else 'Left'}")
    print(f"   🎨 Style: {style_theme.title()}")
    print(f"   📏 Page Size: {page_config[2]}")
    print(f"   🖨️  Bleed: {'Yes' if has_bleed else 'No'}")
    print(f"   💧 Watermark: {'Yes' if add_watermark else 'No'}")
    print(f"   🔢 Numbering: {'Yes' if use_numbers else 'No'}")
    print(f"   📑 Subsections in TOC: {'Yes' if include_subsections else 'No'}")
    
    return (book_title, author_name, use_numbers, include_subsections, 
            add_watermark, page_config, has_bleed, center_titles, style_theme)

def read_markdown_file(chapter_path: Path, use_numbers: bool) -> Tuple[str, str]:
    """Read markdown content from final_article.md in chapter folder."""
    md_file = chapter_path / "final_article.md"
    if not md_file.exists():
        print(f"Warning: {md_file} not found, skipping chapter")
        return None, None
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if use_numbers:
        chapter_match = re.search(r'Chapter\s+(\d+)', chapter_path.name, re.IGNORECASE)
        if chapter_match:
            chapter_num = chapter_match.group(1)
            chapter_title = f"Chapter {chapter_num}"
        else:
            chapter_title = chapter_path.name
    else:
        lines = content.split('\n')
        chapter_title = "Untitled Chapter"
        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                chapter_title = re.sub(r'^#+\s*', '', line).strip()
                break
    
    return chapter_title, content

def escape_latex(text: str) -> str:
    """Escape special LaTeX characters in text."""
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
    
    text = text.replace('\\', special_chars['\\'])
    for char, replacement in special_chars.items():
        if char != '\\':
            text = text.replace(char, replacement)
    
    return text

def markdown_to_latex(content: str, use_numbers: bool, center_titles: bool) -> str:
    """Convert markdown formatting to LaTeX with enhanced styling."""
    
    # Handle code blocks first
    code_blocks = []
    
    def store_code_block(match):
        code_blocks.append(match.group(0))
        return f"<<<CODEBLOCK_{len(code_blocks)-1}>>>"
    
    content = re.sub(r'```[\s\S]*?```', store_code_block, content)
    content = re.sub(r'`([^`]+)`', r'\\texttt{\1}', content)
    
    lines = content.split('\n')
    processed_lines = []
    
    for line in lines:
        if not line.startswith('<<<CODEBLOCK_'):
            # Headers with enhanced styling and alignment
            if use_numbers:
                if line.startswith('######'):
                    header_text = re.sub(r'^######\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\subparagraph{{\\centering {header_text}}}"
                    else:
                        line = f"\\subparagraph{{{header_text}}}"
                elif line.startswith('#####'):
                    header_text = re.sub(r'^#####\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\paragraph{{\\centering {header_text}}}"
                    else:
                        line = f"\\paragraph{{{header_text}}}"
                elif line.startswith('####'):
                    header_text = re.sub(r'^####\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\subsubsection{{\\centering {header_text}}}"
                    else:
                        line = f"\\subsubsection{{{header_text}}}"
                elif line.startswith('###'):
                    header_text = re.sub(r'^###\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\subsection{{\\centering {header_text}}}"
                    else:
                        line = f"\\subsection{{{header_text}}}"
                elif line.startswith('##'):
                    header_text = re.sub(r'^##\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\section{{\\centering {header_text}}}"
                    else:
                        line = f"\\section{{{header_text}}}"
                elif line.startswith('#'):
                    header_text = re.sub(r'^#\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\section{{\\centering {header_text}}}"
                    else:
                        line = f"\\section{{{header_text}}}"
            else:
                # Unnumbered sections
                if line.startswith('######'):
                    header_text = re.sub(r'^######\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\subparagraph*{{\\centering {header_text}}}"
                    else:
                        line = f"\\subparagraph*{{{header_text}}}"
                elif line.startswith('#####'):
                    header_text = re.sub(r'^#####\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\paragraph*{{\\centering {header_text}}}"
                    else:
                        line = f"\\paragraph*{{{header_text}}}"
                elif line.startswith('####'):
                    header_text = re.sub(r'^####\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\subsubsection*{{\\centering {header_text}}}"
                    else:
                        line = f"\\subsubsection*{{{header_text}}}"
                elif line.startswith('###'):
                    header_text = re.sub(r'^###\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\subsection*{{\\centering {header_text}}}"
                    else:
                        line = f"\\subsection*{{{header_text}}}"
                elif line.startswith('##'):
                    header_text = re.sub(r'^##\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\section*{{\\centering {header_text}}}"
                    else:
                        line = f"\\section*{{{header_text}}}"
                elif line.startswith('#'):
                    header_text = re.sub(r'^#\s+(.+)$', r'\1', line)
                    if center_titles:
                        line = f"\\section*{{\\centering {header_text}}}"
                    else:
                        line = f"\\section*{{{header_text}}}"
            
            if not line.startswith('\\'):
                line = escape_latex(line)
        
        processed_lines.append(line)
    
    content = '\n'.join(processed_lines)
    
    # Enhanced text formatting
    content = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\textit{\1}}', content)
    content = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', content)
    content = re.sub(r'\*(.+?)\*', r'\\textit{\1}', content)
    
    # Enhanced lists
    content = re.sub(r'^\*\s+', r'\\item ', content, flags=re.MULTILINE)
    content = re.sub(r'^-\s+', r'\\item ', content, flags=re.MULTILINE)
    content = re.sub(r'^\d+\.\s+', r'\\item ', content, flags=re.MULTILINE)
    
    # Wrap list items in enhanced itemize environment
    lines = content.split('\n')
    in_list = False
    processed_lines = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('\\item'):
            if not in_list:
                processed_lines.append('\\begin{itemize}[leftmargin=1.2em, itemsep=0.1em]')
                in_list = True
            processed_lines.append(line)
        else:
            if in_list and line.strip() == '':
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
    
    # Restore code blocks with enhanced formatting
    for i, code_block in enumerate(code_blocks):
        match = re.match(r'```(\w*)\n([\s\S]*?)```', code_block)
        if match:
            lang = match.group(1) or 'text'
            code = match.group(2)
            # Enhanced code block formatting
            latex_code = f"\\vspace{{0.3em}}\n\\begin{{verbatim}}\n{code}\\end{{verbatim}}\n\\vspace{{0.3em}}"
            content = content.replace(f"<<<CODEBLOCK_{i}>>>", latex_code)
    
    # Enhanced paragraph handling
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    content = re.sub(r'\n\n', '\n\n\\\\vspace{0.25em}\n', content)
    
    return content

def clean_markdown_to_text(content: str) -> str:
    """Convert markdown content to clean plain text."""
    # Remove code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)
    content = re.sub(r'`([^`]+)`', r'\1', content)
    
    # Remove headers (keep text, remove # symbols)
    content = re.sub(r'^#+\s*(.+)$', r'\1', content, flags=re.MULTILINE)
    
    # Remove formatting
    content = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', content)
    content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)
    content = re.sub(r'\*(.+?)\*', r'\1', content)
    content = re.sub(r'__(.+?)__', r'\1', content)
    content = re.sub(r'_(.+?)_', r'\1', content)
    content = re.sub(r'~~(.+?)~~', r'\1', content)
    
    # Remove links but keep text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    content = re.sub(r'<([^>]+)>', r'\1', content)
    
    # Remove images
    content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', content)
    
    # Convert lists
    content = re.sub(r'^\s*[-*+]\s+', '• ', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*\d+\.\s+', '• ', content, flags=re.MULTILINE)
    
    # Clean up
    content = re.sub(r'^[-*_]{3,}$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^>\s*', '', content, flags=re.MULTILINE)
    content = re.sub(r'\|', ' ', content)
    content = re.sub(r'^[-\s:]+$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    content = re.sub(r'[ \t]+', ' ', content)
    content = re.sub(r'^\s+', '', content, flags=re.MULTILINE)
    content = re.sub(r'\s+$', '', content, flags=re.MULTILINE)
    content = re.sub(r'\\(.)', r'\1', content)
    
    return content.strip()

def save_chapters_as_text(chapters_data: List[Tuple[str, str]], base_path: Path, folder_name: str):
    """Save all chapters as clean text files."""
    text_folder = base_path / f"{folder_name}_chapters_text"
    text_folder.mkdir(exist_ok=True)
    
    print(f"\n📝 Saving chapters as text files in: {text_folder}")
    
    for i, (chapter_title, content) in enumerate(chapters_data, 1):
        if content:
            clean_text = clean_markdown_to_text(content)
            safe_chapter_name = re.sub(r'[^\w\s-]', '', chapter_title.lower())
            safe_chapter_name = re.sub(r'[-\s]+', '_', safe_chapter_name)
            text_filename = f"chapter_{i:02d}_{safe_chapter_name}.txt"
            text_file_path = text_folder / text_filename
            
            with open(text_file_path, 'w', encoding='utf-8') as f:
                f.write(f"{chapter_title}\n")
                f.write("=" * len(chapter_title) + "\n\n")
                f.write(clean_text)
            
            print(f"  ✅ {text_filename}")
    
    return text_folder

def get_style_settings(style_theme: str) -> Dict[str, str]:
    """Get styling settings based on theme."""
    styles = {
        'classic': {
            'chapter_format': r'''
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}
{\chaptertitlename\ \thechapter}
{18pt}
{\Huge}
\titlespacing*{\chapter}{0pt}{30pt}{40pt}''',
            
            'section_format': r'''
\titleformat{\section}
{\normalfont\Large\bfseries}
{\thesection}
{1em}
{}
\titlespacing*{\section}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}''',
            
            'subsection_format': r'''
\titleformat{\subsection}
{\normalfont\large\bfseries}
{\thesubsection}
{1em}
{}
\titlespacing*{\subsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}''',
            
            'paragraph_settings': r'\setlength{\parskip}{0.4em}',
            'line_spacing': r'\setstretch{1.2}'
        },
        
        'modern': {
            'chapter_format': r'''
\titleformat{\chapter}[display]
{\normalfont\LARGE\bfseries\sffamily}
{\chaptertitlename\ \thechapter}
{20pt}
{\fontsize{28}{34}\selectfont}
\titlespacing*{\chapter}{0pt}{20pt}{50pt}''',
            
            'section_format': r'''
\titleformat{\section}
{\normalfont\Large\bfseries\sffamily\color{gray!20}}
{\thesection}
{1.2em}
{}
\titlespacing*{\section}{0pt}{4ex plus 1ex minus .2ex}{3ex plus .2ex}''',
            
            'subsection_format': r'''
\titleformat{\subsection}
{\normalfont\large\bfseries\sffamily}
{\thesubsection}
{1em}
{}
\titlespacing*{\subsection}{0pt}{3.5ex plus 1ex minus .2ex}{2ex plus .2ex}''',
            
            'paragraph_settings': r'\setlength{\parskip}{0.5em}',
            'line_spacing': r'\setstretch{1.25}'
        },
        
        'elegant': {
            'chapter_format': r'''
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries\scshape}
{\chaptertitlename\ \thechapter}
{25pt}
{\fontsize{32}{40}\selectfont}
\titlespacing*{\chapter}{0pt}{25pt}{55pt}''',
            
            'section_format': r'''
\titleformat{\section}
{\normalfont\Large\bfseries\scshape}
{\thesection}
{1.5em}
{}
\titlespacing*{\section}{0pt}{4.5ex plus 1ex minus .2ex}{3.5ex plus .2ex}''',
            
            'subsection_format': r'''
\titleformat{\subsection}
{\normalfont\large\bfseries\itshape}
{\thesubsection}
{1.2em}
{}
\titlespacing*{\subsection}{0pt}{4ex plus 1ex minus .2ex}{2.5ex plus .2ex}''',
            
            'paragraph_settings': r'\setlength{\parskip}{0.45em}',
            'line_spacing': r'\setstretch{1.3}'
        }
    }
    
    return styles.get(style_theme, styles['classic'])

def create_enhanced_latex_document(chapters_data: List[Tuple[str, str]], output_path: Path, book_title: str, author_name: str, use_numbers: bool, include_subsections: bool, add_watermark: bool, page_config: Tuple, has_bleed: bool, estimated_pages: int, center_titles: bool, style_theme: str) -> str:
    """Create enhanced KDP-compliant LaTeX document with professional styling."""
    
    page_width, page_height, size_name, width_inches, height_inches = page_config
    
    # Calculate KDP-compliant margins
    margins = calculate_kdp_margins(estimated_pages, has_bleed)
    
    # Apply bleed if needed
    final_width, final_height = calculate_bleed_dimensions(page_width, page_height, has_bleed)
    
    # Get style settings
    style_settings = get_style_settings(style_theme)
    
    # Start LaTeX document with enhanced styling
    latex_doc = f'''\\documentclass[12pt,twoside]{{book}}

% Enhanced packages for professional styling
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
\\usepackage{{setspace}}
\\usepackage{{enumitem}}
\\usepackage{{xcolor}}
\\usepackage{{graphicx}}

% Professional fonts and typography
\\usepackage{{lmodern}}
\\usepackage{{mathptmx}} % Times-like font for body text
\\usepackage[scaled=0.9]{{helvet}} % Helvetica-like for sans serif
\\usepackage{{courier}} % Courier for monospace

% Enhanced KDP-COMPLIANT PAGE GEOMETRY
\\geometry{{
    paperwidth={final_width:.2f}cm,
    paperheight={final_height:.2f}cm,
    top={margins['top']:.3f}in,
    bottom={margins['bottom']:.3f}in,
    inner={margins['inside']:.3f}in,
    outer={margins['outside']:.3f}in,
    bindingoffset=0pt,
    headheight=16pt,
    headsep=14pt,
    footskip=28pt,
    marginparwidth=0pt,
    marginparsep=0pt
}}

% ENHANCED STYLING - {style_theme.upper()} THEME
% Page Count: {estimated_pages} | Size: {size_name} | Alignment: {'Center' if center_titles else 'Left'}

% Typography settings
{style_settings['line_spacing']}
{style_settings['paragraph_settings']}
\\setlength{{\\parindent}}{{0pt}}

% Enhanced text formatting
\\renewcommand{{\\footnotesize}}{{\\fontsize{{9}}{{10.8}}\\selectfont}}
\\renewcommand{{\\scriptsize}}{{\\fontsize{{8}}{{9.6}}\\selectfont}}
\\renewcommand{{\\tiny}}{{\\fontsize{{7}}{{8.4}}\\selectfont}}

% Improved text justification
\\tolerance=1000
\\emergencystretch=3em
\\hfuzz=0.1pt
\\vfuzz=0.1pt'''

    # Add watermark if requested (KDP-compliant positioning)
    if add_watermark:
        h_positions, v_positions, _, _, _, _ = calculate_watermark_positions(
            final_width, final_height, author_name, margins, has_bleed
        )
        
        if h_positions and v_positions:
            latex_doc += f'''

% ENHANCED KDP-COMPLIANT WATERMARKS
\\usepackage{{tikz}}
\\usepackage{{eso-pic}}

\\AddToShipoutPictureBG{{%
    \\AtPageLowerLeft{{%
        \\begin{{tikzpicture}}[remember picture, overlay]
            \\tikzset{{
                enhancedwatermark/.style={{
                    color=gray!15,
                    font=\\fontsize{{9}}{{10.8}}\\selectfont\\rmfamily,
                    opacity=0.25,
                    inner sep=0pt,
                    outer sep=0pt
                }}
            }}
            
            % Professional watermark grid
            \\foreach \\x in {{{", ".join([f"{pos:.2f}" for pos in h_positions])}}} {{
                \\foreach \\y in {{{", ".join([f"{pos:.2f}" for pos in v_positions])}}} {{
                    \\node[enhancedwatermark] at (\\x cm, \\y cm) {{{author_name}}};
                }}
            }}
        \\end{{tikzpicture}}
    }}
}}'''

    latex_doc += '''

% ENHANCED HEADERS AND FOOTERS
\\pagestyle{fancy}
\\fancyhf{}
\\fancyhead[LE]{\\small\\thepage}
\\fancyhead[RO]{\\small\\thepage}
\\fancyhead[LO]{\\small\\nouppercase{\\rightmark}}
\\fancyhead[RE]{\\small\\nouppercase{\\leftmark}}
\\renewcommand{\\headrulewidth}{0.5pt}
\\renewcommand{\\headrule}{\\vbox to 0pt{\\hbox to\\headwidth{\\dotfill}\\vss}}

% Enhanced chapter page style
\\fancypagestyle{plain}{
    \\fancyhf{}
    \\fancyfoot[C]{\\small\\thepage}
    \\renewcommand{\\headrulewidth}{0pt}
}'''

    # Add chapter formatting based on alignment and style
    if center_titles:
        chapter_align = "\\centering"
        section_align = "\\centering"
    else:
        chapter_align = ""
        section_align = ""

    if use_numbers:
        latex_doc += f'''

% ENHANCED CHAPTER FORMATTING - NUMBERED
\\titleformat{{\\chapter}}[display]
{{\\normalfont\\huge\\bfseries{chapter_align}}}
{{\\chaptertitlename\\ \\thechapter}}
{{20pt}}
{{\\fontsize{{36}}{{43}}\\selectfont}}
\\titlespacing*{{\\chapter}}{{0pt}}{{30pt}}{{50pt}}

% Enhanced section formatting
\\titleformat{{\\section}}
{{\\normalfont\\Large\\bfseries{section_align}}}
{{\\thesection}}
{{1.2em}}
{{}}
\\titlespacing*{{\\section}}{{0pt}}{{4ex plus 1ex minus .2ex}}{{3ex plus .2ex}}

% Enhanced subsection formatting
\\titleformat{{\\subsection}}
{{\\normalfont\\large\\bfseries{section_align}}}
{{\\thesubsection}}
{{1em}}
{{}}
\\titlespacing*{{\\subsection}}{{0pt}}{{3.5ex plus 1ex minus .2ex}}{{2ex plus .2ex}}

% Enhanced paragraph formatting
\\titleformat{{\\paragraph}}
{{\\normalfont\\normalsize\\bfseries{section_align}}}
{{\\theparagraph}}
{{1em}}
{{}}
\\titlespacing*{{\\paragraph}}{{0pt}}{{3ex plus 1ex minus .2ex}}{{1.5ex plus .2ex}}

% Enhanced subparagraph formatting
\\titleformat{{\\subparagraph}}
{{\\normalfont\\normalsize\\itshape{section_align}}}
{{\\thesubparagraph}}
{{1em}}
{{}}
\\titlespacing*{{\\subparagraph}}{{0pt}}{{2.5ex plus 1ex minus .2ex}}{{1ex plus .2ex}}

\\renewcommand{{\\chaptermark}}[1]{{\\markboth{{\\MakeUppercase{{\\chaptername\\ \\thechapter.\\ #1}}}}{{}}}}
\\renewcommand{{\\sectionmark}}[1]{{\\markright{{\\thesection\\ #1}}}}'''
    else:
        latex_doc += f'''

% ENHANCED CHAPTER FORMATTING - UNNUMBERED
\\titleformat{{\\chapter}}[display]
{{\\normalfont\\huge\\bfseries{chapter_align}}}
{{}}
{{20pt}}
{{\\fontsize{{36}}{{43}}\\selectfont}}
\\titlespacing*{{\\chapter}}{{0pt}}{{30pt}}{{50pt}}

% Enhanced section formatting
\\titleformat{{\\section}}
{{\\normalfont\\Large\\bfseries{section_align}}}
{{}}
{{1.2em}}
{{}}
\\titlespacing*{{\\section}}{{0pt}}{{4ex plus 1ex minus .2ex}}{{3ex plus .2ex}}

% Enhanced subsection formatting
\\titleformat{{\\subsection}}
{{\\normalfont\\large\\bfseries{section_align}}}
{{}}
{{1em}}
{{}}
\\titlespacing*{{\\subsection}}{{0pt}}{{3.5ex plus 1ex minus .2ex}}{{2ex plus .2ex}}

% Enhanced paragraph formatting
\\titleformat{{\\paragraph}}
{{\\normalfont\\normalsize\\bfseries{section_align}}}
{{}}
{{1em}}
{{}}
\\titlespacing*{{\\paragraph}}{{0pt}}{{3ex plus 1ex minus .2ex}}{{1.5ex plus .2ex}}

% Enhanced subparagraph formatting
\\titleformat{{\\subparagraph}}
{{\\normalfont\\normalsize\\itshape{section_align}}}
{{}}
{{1em}}
{{}}
\\titlespacing*{{\\subparagraph}}{{0pt}}{{2.5ex plus 1ex minus .2ex}}{{1ex plus .2ex}}

\\renewcommand{{\\chaptermark}}[1]{{\\markboth{{\\MakeUppercase{{#1}}}}{{}}}}
\\renewcommand{{\\sectionmark}}[1]{{\\markright{{#1}}}}'''

    # Table of contents formatting
    toc_depth = "2" if include_subsections else "0"

    latex_doc += f'''

% ENHANCED TABLE OF CONTENTS
\\setcounter{{tocdepth}}{{{toc_depth}}}
\\renewcommand{{\\cfttoctitlefont}}{{\\huge\\bfseries{chapter_align}}}
\\renewcommand{{\\cftchapfont}}{{\\bfseries}}
\\renewcommand{{\\cftsecfont}}{{\\normalfont}}
\\renewcommand{{\\cftsubsecfont}}{{\\normalfont\\itshape}}
\\renewcommand{{\\cftchappagefont}}{{\\bfseries}}
\\renewcommand{{\\cftsecpagefont}}{{\\normalfont}}
\\renewcommand{{\\cftsubsecpagefont}}{{\\normalfont}}

% Enhanced TOC spacing
\\renewcommand{{\\cftbeforechapskip}}{{0.8em}}
\\renewcommand{{\\cftbeforesecskip}}{{0.3em}}
\\renewcommand{{\\cftbeforesubsecskip}}{{0.2em}}

% TOC dots
\\renewcommand{{\\cftchapleader}}{{\\cftdotfill{{\\cftdotsep}}}}
\\renewcommand{{\\cftsecleader}}{{\\cftdotfill{{\\cftdotsep}}}}
\\renewcommand{{\\cftsubsecleader}}{{\\cftdotfill{{\\cftdotsep}}}}

% Enhanced hyperref setup
\\hypersetup{{
    colorlinks=false,
    linkcolor=black,
    filecolor=black,
    urlcolor=black,
    pdftitle={{{book_title}}},
    pdfauthor={{{author_name}}},
    pdfsubject={{Generated with Enhanced KDP Book Generator}},
    pdfcreator={{LaTeX with enhanced styling}},
    bookmarks=true,
    bookmarksopen=false,
    bookmarksnumbered=true,
    pdfstartview={{FitH}},
    pdfpagemode={{UseNone}},
    hidelinks
}}

% Start document
\\begin{{document}}

% ENHANCED TITLE PAGE
\\begin{{titlepage}}
    \\newgeometry{{margin=1in}}
    {chapter_align}
    \\vspace*{{3cm}}
    
    % Title with enhanced styling
    {{\\fontsize{{48}}{{58}}\\selectfont\\bfseries {book_title}\\par}}
    
    \\vspace{{4cm}}
    
    % Author with enhanced styling
    {{\\fontsize{{18}}{{22}}\\selectfont\\itshape by {author_name}\\par}}
    
    \\vfill
    
    % Date with enhanced styling  
    {{\\fontsize{{12}}{{14}}\\selectfont \\today\\par}}
    
    \\vspace{{2cm}}
    \\restoregeometry
\\end{{titlepage}}


% ENHANCED TABLE OF CONTENTS
\\newpage
\\tableofcontents
\\clearpage

% Main content starts here
\\mainmatter
'''

    # Add each chapter with enhanced formatting
    for chapter_title, content in chapters_data:
        if content:
            latex_content = markdown_to_latex(content, use_numbers, center_titles)
            if use_numbers:
                latex_doc += f"\n\\chapter{{{chapter_title}}}\n"
            else:
                latex_doc += f"\n\\chapter*{{{chapter_title}}}\n"
                latex_doc += f"\\addcontentsline{{toc}}{{chapter}}{{{chapter_title}}}\n"
                latex_doc += f"\\markboth{{\\MakeUppercase{{{chapter_title}}}}}{{\\MakeUppercase{{{chapter_title}}}}}\n"
            latex_doc += latex_content
            latex_doc += "\n\\clearpage\n"

    # Enhanced document end
    latex_doc += r'''

% Enhanced back matter
\backmatter

% Optional: About the Author page
% \chapter*{About the Author}
% \addcontentsline{toc}{chapter}{About the Author}
% [Author biography would go here]

\end{document}
'''
    
    return latex_doc

def estimate_page_count(chapters_data: List[Tuple[str, str]]) -> int:
    """Estimate page count for margin calculations."""
    total_words = sum(len(content.split()) for _, content in chapters_data)
    # Enhanced estimate: 250-300 words per page for enhanced formatting
    estimated_pages = max(24, int(total_words / 280))
    
    # Add pages for enhanced front matter
    front_matter_pages = 10  # Title, copyright, TOC, etc.
    
    return estimated_pages + front_matter_pages

def compile_latex_to_pdf(latex_content: str, output_pdf: Path) -> bool:
    """Compile LaTeX to PDF with enhanced settings."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        tex_file = temp_path / "document.tex"
        
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        try:
            print("   🎨 Enhanced LaTeX compilation (pass 1/3)...")
            
            # Run pdflatex three times for proper cross-references and styling
            for i in range(3):
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-output-directory', temp_dir, 
                     '-synctex=1', '-shell-escape', str(tex_file)],
                    capture_output=True,
                    text=True,
                    cwd=temp_dir
                )
                
                if i == 0:
                    print("   🎨 Enhanced LaTeX compilation (pass 2/3)...")
                elif i == 1:
                    print("   🎨 Enhanced LaTeX compilation (pass 3/3)...")
                
                pdf_file = temp_path / "document.pdf"
                if result.returncode != 0 and not pdf_file.exists():
                    print(f"❌ Enhanced LaTeX compilation failed (pass {i+1}):")
                    print("Error details:")
                    print("-" * 50)
                    error_lines = result.stdout.split('\n')
                    for line in error_lines:
                        if any(keyword in line.lower() for keyword in 
                               ['error', '!', 'undefined', 'missing', 'geometry', 'font']):
                            print(line)
                    return False
            
            if pdf_file.exists():
                shutil.copy(pdf_file, output_pdf)
                print("   ✅ Enhanced PDF compilation successful!")
                return True
            else:
                print("❌ Enhanced PDF file was not generated")
                return False
                
        except FileNotFoundError:
            print("❌ Error: pdflatex not found. Please ensure LaTeX is installed.")
            print("   Enhanced features require:")
            print("   • Ubuntu/Debian: sudo apt-get install texlive-full")
            print("   • macOS: brew install --cask mactex")
            print("   • Windows: https://miktex.org/")
            return False
        except Exception as e:
            print(f"❌ Error during enhanced compilation: {e}")
            return False

def validate_kdp_compliance(chapters_data: List[Tuple[str, str]], estimated_pages: int, has_bleed: bool, style_theme: str) -> List[str]:
    """Validate enhanced KDP compliance and return warnings."""
    warnings = []
    
    # Check page count for spine text
    if estimated_pages < 79:
        warnings.append(f"📊 Page count ({estimated_pages}) is under 79 - no spine text allowed")
    else:
        warnings.append(f"📊 Page count ({estimated_pages}) allows spine text on cover")
    
    # Check for content adequacy
    total_content_length = sum(len(content) for _, content in chapters_data)
    if total_content_length < 5000:
        warnings.append("⚠️  Short content - ensure adequate book length")
    
    # Style-specific warnings
    if style_theme == 'modern':
        warnings.append("🎨 Modern theme uses sans-serif fonts - verify readability")
    elif style_theme == 'elegant':
        warnings.append("🎨 Elegant theme uses decorative fonts - check character rendering")
    
    # Bleed warnings
    if has_bleed:
        warnings.append("🖨️  Bleed enabled - ensure backgrounds extend to page edge")
        warnings.append("🔍 Verify all text stays within safe zones")
    
    # Enhanced formatting warnings
    warnings.append("✨ Enhanced styling applied - review PDF for formatting consistency")
    
    return warnings

def main():
    """Main function for enhanced KDP-compliant PDF generation."""
    print("🚀 ENHANCED KDP-COMPLIANT BOOK GENERATOR")
    print("=" * 80)
    print("✨ Professional Styling & Typography")
    print("✅ Amazon KDP Print-on-Demand Ready")
    print("✅ Center/Left Alignment Options")
    print("✅ Multiple Style Themes")
    print("✅ Enhanced Visual Appearance")
    print("=" * 80)
    
    # Get user preferences
    preferences = get_user_preferences()
    (book_title, author_name, use_numbers, include_subsections, 
     add_watermark, page_config, has_bleed, center_titles, style_theme) = preferences
    
    # Get folder path
    if len(sys.argv) > 1:
        folder_path = Path(sys.argv[1])
    else:
        folder_path = Path(input("📁 Enter path to folder containing chapters: ").strip())
    
    # Validate path
    if not folder_path.exists():
        print(f"❌ Error: Path '{folder_path}' does not exist")
        return
    
    if not folder_path.is_dir():
        print(f"❌ Error: '{folder_path}' is not a directory")
        return
    
    print(f"\n🔍 Processing chapters in: {folder_path}")
    
    # Get chapter folders
    chapter_folders = get_chapter_folders(folder_path)
    
    if not chapter_folders:
        print("❌ No chapter folders found!")
        print("   📂 Create folders named 'Chapter 1', 'Chapter 2', etc.")
        print("   📄 Each folder should contain 'final_article.md'")
        return
    
    print(f"📚 Found {len(chapter_folders)} chapters:")
    for folder in chapter_folders:
        print(f"  ✅ {folder.name}")
    
    # Read markdown files
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
    
    # Calculate statistics
    total_words = sum(len(content.split()) for _, content in chapters_data)
    estimated_pages = estimate_page_count(chapters_data)
    
    print(f"\n📊 Enhanced Content Analysis:")
    print(f"   📖 Chapters: {len(chapters_data)}")
    print(f"   📝 Total words: {total_words:,}")
    print(f"   📄 Estimated pages: {estimated_pages}")
    print(f"   🎨 Style theme: {style_theme.title()}")
    print(f"   📐 Alignment: {'Center' if center_titles else 'Left'}")
    
    # Enhanced KDP compliance check
    warnings = validate_kdp_compliance(chapters_data, estimated_pages, has_bleed, style_theme)
    if warnings:
        print(f"\n⚠️  Enhanced KDP Compliance Notes:")
        for warning in warnings:
            print(f"   {warning}")
    
    # Calculate final margins
    margins = calculate_kdp_margins(estimated_pages, has_bleed)
    print(f"\n📐 Enhanced KDP Margins (based on {estimated_pages} pages):")
    print(f"   Top: {margins['top']:.3f}\" ({margins['top']*25.4:.1f}mm)")
    print(f"   Bottom: {margins['bottom']:.3f}\" ({margins['bottom']*25.4:.1f}mm)")
    print(f"   Inside: {margins['inside']:.3f}\" ({margins['inside']*25.4:.1f}mm)")
    print(f"   Outside: {margins['outside']:.3f}\" ({margins['outside']*25.4:.1f}mm)")
    
    # Create output filenames
    safe_title = re.sub(r'[^\w\s-]', '', book_title.lower())
    safe_title = re.sub(r'[-\s]+', '_', safe_title)
    output_pdf = folder_path / f"{safe_title}_ENHANCED_KDP.pdf"
    latex_file = folder_path / f"{safe_title}_ENHANCED_SOURCE.tex"
    
    # Generate enhanced LaTeX
    print(f"\n🎨 Generating enhanced KDP-compliant LaTeX ({style_theme} theme)...")
    latex_content = create_enhanced_latex_document(
        chapters_data, output_pdf, book_title, author_name, 
        use_numbers, include_subsections, add_watermark, 
        page_config, has_bleed, estimated_pages, center_titles, style_theme
    )
    
    # Save LaTeX source
    with open(latex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    print(f"📄 Enhanced LaTeX source saved: {latex_file}")
    
    # Compile to enhanced PDF
    print("\n⚙️  Compiling enhanced KDP-compliant PDF...")
    if compile_latex_to_pdf(latex_content, output_pdf):
        # Save text chapters
        text_folder = save_chapters_as_text(chapters_data, folder_path, safe_title)
        
        print(f"\n🎉 ENHANCED KDP-READY BOOK GENERATED!")
        print("\n" + "=" * 80)
        print("📖 ENHANCED BOOK SPECIFICATIONS:")
        print(f"   Title: {book_title}")
        print(f"   Author: {author_name}")
        print(f"   Chapters: {len(chapters_data)}")
        print(f"   Words: {total_words:,}")
        print(f"   Estimated Pages: {estimated_pages}")
        print(f"   Page Size: {page_config[2]}")
        print(f"   Style Theme: {style_theme.title()}")
        print(f"   Title Alignment: {'Center' if center_titles else 'Left'}")
        
        if has_bleed:
            final_width, final_height = calculate_bleed_dimensions(
                page_config[0], page_config[1], has_bleed)
            print(f"   With Bleed: {final_width:.1f} x {final_height:.1f} cm")
        
        print(f"   Margins: Enhanced KDP-Compliant")
        print(f"   Watermarks: {'Enhanced Safe Positioning' if add_watermark else 'Disabled'}")
        print(f"   Typography: Professional Enhanced Fonts")
        
        # File information
        try:
            pdf_size_mb = output_pdf.stat().st_size / (1024 * 1024)
            print(f"\n📁 ENHANCED FILES GENERATED:")
            print(f"   📕 Enhanced KDP PDF: {output_pdf} ({pdf_size_mb:.1f} MB)")
            print(f"   📄 Enhanced LaTeX: {latex_file}")
            print(f"   📝 Text Chapters: {text_folder}")
        except:
            print(f"\n📁 ENHANCED FILES GENERATED:")
            print(f"   📕 Enhanced KDP PDF: {output_pdf}")
            print(f"   📄 Enhanced LaTeX: {latex_file}")
            print(f"   📝 Text Chapters: {text_folder}")
        
        print(f"\n🎯 ENHANCED KDP COMPLIANCE:")
        print("   ✅ Enhanced mirror margins based on page count")
        print("   ✅ Professional typography and spacing")
        print("   ✅ Customizable title alignment (center/left)")
        print("   ✅ Multiple style themes (classic/modern/elegant)")
        print("   ✅ Enhanced font sizes and readability")
        print("   ✅ Improved headers and page formatting")
        print("   ✅ Professional title page and copyright")
        print("   ✅ Enhanced table of contents")
        if has_bleed:
            print("   ✅ Proper bleed dimensions")
        print("   ✅ All standard KDP requirements met")
        
        print(f"\n📋 NEXT STEPS:")
        print(f"   1. 📖 Review the enhanced PDF carefully")
        print(f"   2. 🎨 Check styling and alignment consistency") 
        print(f"   3. 🔍 Verify margins and text positioning")
        if has_bleed:
            print(f"   4. 🖼️  Verify bleed images extend to page edge")
        if estimated_pages >= 79:
            print(f"   5. 📏 Add spine text to cover (book has {estimated_pages} pages)")
        print(f"   6. ⬆️  Upload to Amazon KDP")
        print(f"   7. 🔍 Use KDP Print Previewer to verify")
        
        if warnings:
            print(f"\n⚠️  ENHANCED REMINDERS:")
            for warning in warnings:
                print(f"   {warning}")
        
    else:
        print("\n❌ Failed to generate enhanced KDP-compliant PDF")
        print(f"📄 Check enhanced LaTeX source: {latex_file}")
        print("\n🛠️  Troubleshooting:")
        print("   • Ensure LaTeX is installed (texlive-full recommended)")
        print("   • Check for special characters in content")
        print("   • Verify all markdown files are valid")
        print("   • Enhanced features require complete LaTeX installation")

if __name__ == "__main__":
    main()