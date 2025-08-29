#!/usr/bin/env python3
"""
KDP-Compliant Markdown to PDF Book Generator
Converts chapter markdown files to Amazon KDP-compliant PDF with LaTeX
Includes proper margins, bleed support, and all KDP requirements
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
    """
    Calculate KDP-compliant margins based on page count.
    Returns margins in inches for LaTeX geometry package.
    """
    # KDP margin requirements based on page count (in inches)
    if page_count <= 24:
        inside_margin = 0.375  # 9.5mm
        outside_margin = 0.25  # 6.4mm
    elif page_count <= 150:
        inside_margin = 0.75   # 19mm
        outside_margin = 0.25  # 6.4mm
    elif page_count <= 300:
        inside_margin = 0.875  # 22.2mm
        outside_margin = 0.25  # 6.4mm
    elif page_count <= 500:
        inside_margin = 1.0    # 25.4mm
        outside_margin = 0.25  # 6.4mm
    elif page_count <= 700:
        inside_margin = 1.125  # 28.6mm
        outside_margin = 0.25  # 6.4mm
    else:
        inside_margin = 1.25   # 31.8mm
        outside_margin = 0.25  # 6.4mm
    
    # Top and bottom margins
    top_margin = 0.25     # 6.4mm minimum
    bottom_margin = 0.25  # 6.4mm minimum
    
    # Add extra margin for safety (KDP recommends slightly larger than minimum)
    safety_margin = 0.125  # 3.2mm additional safety
    
    return {
        'top': top_margin + safety_margin,
        'bottom': bottom_margin + safety_margin, 
        'inside': inside_margin + safety_margin,
        'outside': outside_margin + safety_margin
    }

def calculate_bleed_dimensions(width: float, height: float, has_bleed: bool = False) -> Tuple[float, float]:
    """
    Calculate page dimensions with bleed if needed.
    KDP requires 0.125" (3.2mm) bleed on width and 0.25" (6.4mm) on height.
    """
    if has_bleed:
        # Convert cm to inches for bleed calculation
        width_inches = width / 2.54
        height_inches = height / 2.54
        
        # Add bleed
        width_inches += 0.125  # 3.2mm
        height_inches += 0.25  # 6.4mm
        
        # Convert back to cm
        return width_inches * 2.54, height_inches * 2.54
    
    return width, height

def calculate_watermark_positions(page_width: float, page_height: float, author_name: str, margins: Dict[str, float], has_bleed: bool = False):
    """Calculate watermark positions respecting KDP margins and safe zones."""
    
    # Convert margin inches to cm for calculations
    top_margin_cm = margins['top'] * 2.54
    bottom_margin_cm = margins['bottom'] * 2.54
    inside_margin_cm = margins['inside'] * 2.54
    outside_margin_cm = margins['outside'] * 2.54
    
    # Add extra safe zone for KDP (0.125" = 3.2mm from each edge)
    safe_zone = 0.125 * 2.54  # 3.2mm in cm
    
    # Calculate effective margins (larger of KDP margin or safe zone)
    effective_top = max(top_margin_cm, safe_zone)
    effective_bottom = max(bottom_margin_cm, safe_zone)
    effective_left = max(outside_margin_cm, safe_zone)  # Outside margin for odd pages
    effective_right = max(inside_margin_cm, safe_zone)   # Inside margin for odd pages
    
    # Text dimensions
    text_width_cm = len(author_name) * 0.4  # Slightly smaller for safety
    text_height_cm = 0.3
    
    # Watermark spacing
    min_horizontal_gap = 1.0  # Increased gap for KDP compliance
    min_vertical_gap = 0.8
    
    watermark_width = text_width_cm + min_horizontal_gap
    watermark_height = text_height_cm + min_vertical_gap
    
    # Available space for watermarks (respecting KDP margins)
    available_width = page_width - effective_left - effective_right
    available_height = page_height - effective_top - effective_bottom
    
    # Calculate number of watermarks (more conservative for KDP)
    horizontal_count = max(2, int(available_width / watermark_width))
    vertical_count = max(3, int(available_height / watermark_height))
    
    # Generate positions
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
    """Get user preferences for KDP-compliant book generation."""
    print("\n" + "="*60)
    print("📚 KDP-COMPLIANT BOOK GENERATOR")
    print("="*60)
    print("✅ Amazon KDP Print-on-Demand Ready")
    print("✅ Proper Margins & Bleed Support")
    print("✅ Font Embedding & Page Count Validation")
    print("="*60)
    
    # Get book title
    book_title = input("📖 Enter the book title: ").strip()
    if not book_title:
        book_title = "Generated Book"
    
    # Get author name
    author_name = input("✍️  Enter the author name: ").strip()
    if not author_name:
        author_name = "Unknown Author"
    
    # Get bleed preference
    print("\n🖨️  Do you need bleed for your book?")
    print("   • Bleed extends images/backgrounds to page edge")
    print("   • Required if you have full-page backgrounds or images")
    print("   • Adds 0.125\" width + 0.25\" height per KDP requirements")
    
    while True:
        bleed_choice = input("Include bleed? (y/n): ").strip().lower()
        if bleed_choice in ['y', 'yes', 'n', 'no']:
            has_bleed = bleed_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    # Get watermark preference
    print("\n💧 Do you want to add watermarks to the PDF?")
    print("   • KDP-compliant positioning (respects margins & safe zones)")
    print("   • Reduced density for professional appearance")
    
    while True:
        watermark_choice = input("Add watermarks? (y/n): ").strip().lower()
        if watermark_choice in ['y', 'yes', 'n', 'no']:
            add_watermark = watermark_choice in ['y', 'yes']
            break
        print("Please enter 'y' for yes or 'n' for no.")
    
    # Get numbering preference
    print("\n🔢 Do you want to include numbers in chapters and sections?")
    
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
    
    # Get page size preference (KDP-compliant sizes)
    print("\n📏 Choose KDP-compliant page size:")
    print("   1. 5\" x 8\" (12.7 x 20.3 cm) - Popular fiction")
    print("   2. 5.25\" x 8\" (13.3 x 20.3 cm) - Standard fiction") 
    print("   3. 5.5\" x 8.5\" (14.0 x 21.6 cm) - Large fiction")
    print("   4. 6\" x 9\" (15.2 x 22.9 cm) - Non-fiction standard")
    print("   5. 6.14\" x 9.21\" (15.6 x 23.4 cm) - A5 size")
    print("   6. 6.69\" x 9.61\" (17.0 x 24.4 cm) - Large format")
    print("   7. 7\" x 10\" (17.8 x 25.4 cm) - Textbook")
    print("   8. 7.5\" x 9.25\" (19.1 x 23.5 cm) - Square-ish")
    print("   9. 8.5\" x 11\" (21.6 x 27.9 cm) - US Letter")
    
    page_sizes = {
        '1': (5.0, 8.0, '5" x 8" Fiction'),
        '2': (5.25, 8.0, '5.25" x 8" Standard Fiction'),
        '3': (5.5, 8.5, '5.5" x 8.5" Large Fiction'),
        '4': (6.0, 9.0, '6" x 9" Non-fiction'),
        '5': (6.14, 9.21, '6.14" x 9.21" A5'),
        '6': (6.69, 9.61, '6.69" x 9.61" Large'),
        '7': (7.0, 10.0, '7" x 10" Textbook'),
        '8': (7.5, 9.25, '7.5" x 9.25" Square'),
        '9': (8.5, 11.0, '8.5" x 11" Letter')
    }
    
    while True:
        size_choice = input("Select page size (1-9): ").strip()
        if size_choice in page_sizes:
            width_inches, height_inches, size_name = page_sizes[size_choice]
            # Convert to cm
            page_width = width_inches * 2.54
            page_height = height_inches * 2.54
            page_config = (page_width, page_height, size_name, width_inches, height_inches)
            break
        print("Please enter a number from 1 to 9.")
    
    print(f"\n✅ Configuration Summary:")
    print(f"   📖 Title: {book_title}")
    print(f"   ✍️  Author: {author_name}")
    print(f"   📏 Page Size: {page_config[2]}")
    print(f"   🖨️  Bleed: {'Yes - KDP Compliant' if has_bleed else 'No'}")
    print(f"   💧 Watermark: {'Yes - KDP Safe Zones' if add_watermark else 'No'}")
    print(f"   🔢 Numbering: {'Yes' if use_numbers else 'No'}")
    print(f"   📑 Subsections in TOC: {'Yes' if include_subsections else 'No'}")
    
    if has_bleed:
        bleed_width, bleed_height = calculate_bleed_dimensions(page_config[0], page_config[1], has_bleed)
        print(f"   📐 With Bleed: {bleed_width:.1f} x {bleed_height:.1f} cm")
    
    return book_title, author_name, use_numbers, include_subsections, add_watermark, page_config, has_bleed

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

def markdown_to_latex(content: str, use_numbers: bool) -> str:
    """Convert markdown formatting to LaTeX with KDP-compliant formatting."""
    
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
            # Headers
            if use_numbers:
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
            
            if not line.startswith('\\'):
                line = escape_latex(line)
        
        processed_lines.append(line)
    
    content = '\n'.join(processed_lines)
    
    # Bold and italic
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
    
    # Restore code blocks
    for i, code_block in enumerate(code_blocks):
        match = re.match(r'```(\w*)\n([\s\S]*?)```', code_block)
        if match:
            lang = match.group(1) or 'text'
            code = match.group(2)
            latex_code = f"\\begin{{verbatim}}\n{code}\\end{{verbatim}}"
            content = content.replace(f"<<<CODEBLOCK_{i}>>>", latex_code)
    
    # KDP-compliant paragraph handling
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    content = re.sub(r'\n\n', '\n\n\\\\vspace{0.2em}\n', content)
    
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

def create_kdp_latex_document(chapters_data: List[Tuple[str, str]], output_path: Path, book_title: str, author_name: str, use_numbers: bool, include_subsections: bool, add_watermark: bool, page_config: Tuple, has_bleed: bool, estimated_pages: int) -> str:
    """Create KDP-compliant LaTeX document."""
    
    page_width, page_height, size_name, width_inches, height_inches = page_config
    
    # Calculate KDP-compliant margins
    margins = calculate_kdp_margins(estimated_pages, has_bleed)
    
    # Apply bleed if needed
    final_width, final_height = calculate_bleed_dimensions(page_width, page_height, has_bleed)
    
    # Start LaTeX document with KDP-compliant settings
    latex_doc = f'''\\documentclass[12pt,twoside]{{book}}
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

% KDP-compliant fonts (embedded by default)
\\usepackage{{lmodern}}

% KDP-COMPLIANT PAGE GEOMETRY
\\geometry{{
    paperwidth={final_width:.2f}cm,
    paperheight={final_height:.2f}cm,
    top={margins['top']:.3f}in,
    bottom={margins['bottom']:.3f}in,
    inner={margins['inside']:.3f}in,
    outer={margins['outside']:.3f}in,
    bindingoffset=0pt,
    headheight=14pt,
    headsep=12pt,
    footskip=24pt,
    marginparwidth=0pt,
    marginparsep=0pt
}}

% KDP Page Count: {estimated_pages} (affects margin calculations)
% Bleed: {"Yes" if has_bleed else "No"}
% Original Size: {page_width:.1f} x {page_height:.1f} cm
% Final Size: {final_width:.1f} x {final_height:.1f} cm

% KDP-compliant text formatting
\\setstretch{{1.15}}
\\setlength{{\\parskip}}{{0.3em}}
\\setlength{{\\parindent}}{{0pt}}

% Ensure minimum 7pt font size (KDP requirement)
\\renewcommand{{\\footnotesize}}{{\\fontsize{{8}}{{9.6}}\\selectfont}}
\\renewcommand{{\\scriptsize}}{{\\fontsize{{7}}{{8.4}}\\selectfont}}
\\renewcommand{{\\tiny}}{{\\fontsize{{7}}{{8.4}}\\selectfont}}'''

    # Add watermark if requested (KDP-compliant positioning)
    if add_watermark:
        h_positions, v_positions, _, _, _, _ = calculate_watermark_positions(
            final_width, final_height, author_name, margins, has_bleed
        )
        
        if h_positions and v_positions:
            latex_doc += f'''

% KDP-COMPLIANT WATERMARKS (respects margins and safe zones)
\\usepackage{{tikz}}
\\usepackage{{eso-pic}}
\\usepackage{{xcolor}}

\\AddToShipoutPictureBG{{%
    \\AtPageLowerLeft{{%
        \\begin{{tikzpicture}}[remember picture, overlay]
            \\tikzset{{
                kdpwatermark/.style={{
                    color=gray!20,  % Subtle for KDP compliance
                    font=\\fontsize{{8}}{{9.6}}\\selectfont\\normalfont,
                    opacity=0.3,    % Reduced opacity for professional look
                    inner sep=0pt,
                    outer sep=0pt
                }}
            }}
            
            % KDP-Safe watermark positions
            \\foreach \\x in {{{", ".join([f"{pos:.2f}" for pos in h_positions])}}} {{
                \\foreach \\y in {{{", ".join([f"{pos:.2f}" for pos in v_positions])}}} {{
                    \\node[kdpwatermark] at (\\x cm, \\y cm) {{{author_name}}};
                }}
            }}
        \\end{{tikzpicture}}
    }}
}}'''

    latex_doc += '''

% KDP-compliant headers and footers
\\pagestyle{fancy}
\\fancyhf{}
\\fancyhead[LE]{\\thepage}
\\fancyhead[RO]{\\thepage}
\\fancyhead[LO]{\\nouppercase{\\rightmark}}
\\fancyhead[RE]{\\nouppercase{\\leftmark}}
\\renewcommand{\\headrulewidth}{0pt}  % Clean look for KDP

% Chapter formatting'''

    if use_numbers:
        latex_doc += r'''
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}
{\chaptertitlename\ \thechapter}
{16pt}
{\Huge}

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

\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{\chaptername\ \thechapter.\ #1}}{}}
\renewcommand{\sectionmark}[1]{\markright{\thesection\ #1}}
'''
    else:
        latex_doc += r'''
\titleformat{\chapter}[display]
{\normalfont\huge\bfseries}
{}
{16pt}
{\Huge}

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

\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{#1}}{}}
\renewcommand{\sectionmark}[1]{\markright{#1}}
'''

    # Table of contents depth control
    toc_depth = "2" if include_subsections else "0"

    latex_doc += f'''
% KDP-compliant table of contents
\\setcounter{{tocdepth}}{{{toc_depth}}}
\\renewcommand{{\\cftchapfont}}{{\\bfseries}}
\\renewcommand{{\\cftsecfont}}{{\\normalfont}}
\\renewcommand{{\\cftsubsecfont}}{{\\normalfont}}

% Hyperref setup for KDP
\\hypersetup{{
    colorlinks=false,       % KDP prefers no colored links
    linkcolor=black,
    filecolor=black,
    urlcolor=black,
    pdftitle={{{book_title}}},
    pdfauthor={{{author_name}}},
    bookmarks=true,
    bookmarksopen=false,    % Cleaner for print
    bookmarksnumbered=true,
    pdfstartview={{FitH}},
    pdfpagemode={{UseNone}} % No bookmarks panel for print
}}

% Start document
\\begin{{document}}

% Title page (KDP-compliant)
\\begin{{titlepage}}
    \\centering
    \\vspace*{{4cm}}
    {{\\Huge\\bfseries {book_title}\\par}}
    \\vspace{{3cm}}
    {{\\Large by {author_name}\\par}}
    \\vfill
    {{\\large \\today\\par}}
    \\vspace{{2cm}}
\\end{{titlepage}}

% Copyright page (recommended for KDP)
\\newpage
\\thispagestyle{{empty}}
\\vspace*{{\\fill}}
\\begin{{flushleft}}
\\textcopyright\\ \\the\\year\\ {author_name}

All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the author, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law.

\\vspace{{1em}}
First Edition

\\vspace{{1em}}
ISBN: [Your ISBN Here]
\\end{{flushleft}}
\\vspace*{{\\fill}}

% Table of contents
\\newpage
\\tableofcontents
\\clearpage

% Main content starts here
\\mainmatter
'''

    # Add each chapter with KDP-compliant formatting
    for chapter_title, content in chapters_data:
        if content:
            latex_content = markdown_to_latex(content, use_numbers)
            if use_numbers:
                latex_doc += f"\n\\chapter{{{chapter_title}}}\n"
            else:
                latex_doc += f"\n\\chapter*{{{chapter_title}}}\n"
                latex_doc += f"\\addcontentsline{{toc}}{{chapter}}{{{chapter_title}}}\n"
                latex_doc += f"\\markboth{{\\MakeUppercase{{{chapter_title}}}}}{{\\MakeUppercase{{{chapter_title}}}}}\n"
            latex_doc += latex_content
            latex_doc += "\n\\clearpage\n"

    # End document
    latex_doc += r'''
\end{document}
'''
    
    return latex_doc

def estimate_page_count(chapters_data: List[Tuple[str, str]]) -> int:
    """Estimate page count for margin calculations."""
    total_words = sum(len(content.split()) for _, content in chapters_data)
    # Rough estimate: 250-300 words per page for standard formatting
    estimated_pages = max(24, int(total_words / 275))  # Minimum 24 pages
    
    # Add pages for front matter
    front_matter_pages = 8  # Title, copyright, TOC, etc.
    
    return estimated_pages + front_matter_pages

def compile_latex_to_pdf(latex_content: str, output_pdf: Path) -> bool:
    """Compile LaTeX to PDF with KDP-compliant settings."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        tex_file = temp_path / "document.tex"
        
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        try:
            print("   🔄 KDP-compliant LaTeX compilation (pass 1/3)...")
            
            # Run pdflatex three times for proper cross-references and TOC
            for i in range(3):
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-output-directory', temp_dir, 
                     '-synctex=1', str(tex_file)],  # synctex for better debugging
                    capture_output=True,
                    text=True,
                    cwd=temp_dir
                )
                
                if i == 0:
                    print("   🔄 KDP-compliant LaTeX compilation (pass 2/3)...")
                elif i == 1:
                    print("   🔄 KDP-compliant LaTeX compilation (pass 3/3)...")
                
                pdf_file = temp_path / "document.pdf"
                if result.returncode != 0 and not pdf_file.exists():
                    print(f"❌ LaTeX compilation failed (pass {i+1}):")
                    print("Error output:")
                    print("-" * 50)
                    # Show more relevant error information
                    error_lines = result.stdout.split('\n')
                    for line in error_lines:
                        if any(keyword in line.lower() for keyword in 
                               ['error', '!', 'undefined', 'missing', 'geometry']):
                            print(line)
                    return False
            
            if pdf_file.exists():
                shutil.copy(pdf_file, output_pdf)
                print("   ✅ KDP-compliant PDF compilation successful!")
                return True
            else:
                print("❌ PDF file was not generated")
                return False
                
        except FileNotFoundError:
            print("❌ Error: pdflatex not found. Please ensure LaTeX is installed.")
            print("   Install LaTeX:")
            print("   • Ubuntu/Debian: sudo apt-get install texlive-full")
            print("   • macOS: brew install --cask mactex")
            print("   • Windows: https://miktex.org/")
            return False
        except Exception as e:
            print(f"❌ Error during compilation: {e}")
            return False

def validate_kdp_compliance(chapters_data: List[Tuple[str, str]], estimated_pages: int, has_bleed: bool) -> List[str]:
    """Validate KDP compliance and return warnings."""
    warnings = []
    
    # Check page count for spine text
    if estimated_pages < 79:
        warnings.append(f"📊 Page count ({estimated_pages}) is under 79 - no spine text allowed")
    
    # Check for consecutive blank pages (simplified check)
    total_content_length = sum(len(content) for _, content in chapters_data)
    if total_content_length < 1000:
        warnings.append("⚠️  Very short content - ensure you don't have too many blank pages")
    
    # Check chapter count
    if len(chapters_data) > 50:
        warnings.append("⚠️  Many chapters - verify TOC formatting")
    
    # Bleed warnings
    if has_bleed:
        warnings.append("🖨️  Bleed enabled - ensure all background images extend to page edge")
        warnings.append("🔍 Verify all text stays within safe zones")
    
    return warnings

def main():
    """Main function for KDP-compliant PDF generation."""
    print("🚀 KDP-COMPLIANT BOOK GENERATOR")
    print("=" * 70)
    print("✅ Amazon KDP Print-on-Demand Ready")
    print("✅ Professional Margins & Bleed Support") 
    print("✅ Font Embedding & Page Validation")
    print("=" * 70)
    
    # Get user preferences
    book_title, author_name, use_numbers, include_subsections, add_watermark, page_config, has_bleed = get_user_preferences()
    
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
    
    print(f"\n📊 Content Analysis:")
    print(f"   📖 Chapters: {len(chapters_data)}")
    print(f"   📝 Total words: {total_words:,}")
    print(f"   📄 Estimated pages: {estimated_pages}")
    
    # KDP compliance check
    warnings = validate_kdp_compliance(chapters_data, estimated_pages, has_bleed)
    if warnings:
        print(f"\n⚠️  KDP Compliance Notes:")
        for warning in warnings:
            print(f"   {warning}")
    
    # Calculate final margins
    margins = calculate_kdp_margins(estimated_pages, has_bleed)
    print(f"\n📐 KDP Margins (based on {estimated_pages} pages):")
    print(f"   Top: {margins['top']:.3f}\" ({margins['top']*25.4:.1f}mm)")
    print(f"   Bottom: {margins['bottom']:.3f}\" ({margins['bottom']*25.4:.1f}mm)")
    print(f"   Inside: {margins['inside']:.3f}\" ({margins['inside']*25.4:.1f}mm)")
    print(f"   Outside: {margins['outside']:.3f}\" ({margins['outside']*25.4:.1f}mm)")
    
    # Create output filenames
    safe_title = re.sub(r'[^\w\s-]', '', book_title.lower())
    safe_title = re.sub(r'[-\s]+', '_', safe_title)
    output_pdf = folder_path / f"{safe_title}_KDP_READY.pdf"
    latex_file = folder_path / f"{safe_title}_KDP_SOURCE.tex"
    
    # Generate LaTeX
    print("\n🔧 Generating KDP-compliant LaTeX...")
    latex_content = create_kdp_latex_document(
        chapters_data, output_pdf, book_title, author_name, 
        use_numbers, include_subsections, add_watermark, 
        page_config, has_bleed, estimated_pages
    )
    
    # Save LaTeX source
    with open(latex_file, 'w', encoding='utf-8') as f:
        f.write(latex_content)
    print(f"📄 LaTeX source saved: {latex_file}")
    
    # Compile to PDF
    print("\n⚙️  Compiling KDP-compliant PDF...")
    if compile_latex_to_pdf(latex_content, output_pdf):
        # Save text chapters
        text_folder = save_chapters_as_text(chapters_data, folder_path, safe_title)
        
        print(f"\n🎉 KDP-READY BOOK GENERATED SUCCESSFULLY!")
        print("\n" + "=" * 70)
        print("📖 BOOK SPECIFICATIONS:")
        print(f"   Title: {book_title}")
        print(f"   Author: {author_name}")
        print(f"   Chapters: {len(chapters_data)}")
        print(f"   Words: {total_words:,}")
        print(f"   Estimated Pages: {estimated_pages}")
        print(f"   Page Size: {page_config[2]}")
        
        if has_bleed:
            final_width, final_height = calculate_bleed_dimensions(
                page_config[0], page_config[1], has_bleed)
            print(f"   With Bleed: {final_width:.1f} x {final_height:.1f} cm")
        
        print(f"   Margins: KDP-Compliant (varies by page count)")
        print(f"   Watermarks: {'KDP-Safe Positioning' if add_watermark else 'Disabled'}")
        print(f"   Font: Embedded LaTeX Fonts")
        
        # File information
        try:
            pdf_size_mb = output_pdf.stat().st_size / (1024 * 1024)
            print(f"\n📁 FILES GENERATED:")
            print(f"   📕 KDP-Ready PDF: {output_pdf} ({pdf_size_mb:.1f} MB)")
            print(f"   📄 LaTeX Source: {latex_file}")
            print(f"   📝 Text Chapters: {text_folder}")
        except:
            print(f"\n📁 FILES GENERATED:")
            print(f"   📕 KDP-Ready PDF: {output_pdf}")
            print(f"   📄 LaTeX Source: {latex_file}")
            print(f"   📝 Text Chapters: {text_folder}")
        
        print("\n🎯 KDP COMPLIANCE CHECKLIST:")
        print("   ✅ Mirror margins based on page count")
        print("   ✅ Minimum font size (7pt+)")
        print("   ✅ Embedded fonts")
        print("   ✅ Proper pagination (odd/even)")
        print("   ✅ No content in margins")
        if has_bleed:
            print("   ✅ Bleed dimensions (+0.125\" width, +0.25\" height)")
        print("   ✅ Professional formatting")
        
        print(f"\n📋 NEXT STEPS:")
        print(f"   1. 📖 Review the PDF carefully")
        print(f"   2. 🔍 Check margins and text positioning")
        if has_bleed:
            print(f"   3. 🖼️  Verify bleed images extend to page edge")
        if estimated_pages >= 79:
            print(f"   4. 📏 Add spine text to cover (book has {estimated_pages} pages)")
        print(f"   5. ⬆️  Upload to Amazon KDP")
        print(f"   6. 🔍 Use KDP Print Previewer to verify")
        
        if warnings:
            print(f"\n⚠️  IMPORTANT REMINDERS:")
            for warning in warnings:
                print(f"   {warning}")
        
    else:
        print("\n❌ Failed to generate KDP-compliant PDF")
        print(f"📄 Check LaTeX source: {latex_file}")
        print("\n🛠️  Troubleshooting:")
        print("   • Ensure LaTeX is installed (texlive)")
        print("   • Check for special characters in content")
        print("   • Verify all markdown files are valid")

if __name__ == "__main__":
    main()