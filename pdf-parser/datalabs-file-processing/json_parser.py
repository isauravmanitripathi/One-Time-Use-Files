#!/usr/bin/env python3
"""
Datalab JSON Parser - Extract Sections and Text
Parses Datalab.to JSON output and extracts structured sections with headings and text.

Usage:
  python json_parser.py <json_file_path>
  python json_parser.py /path/to/document.json
"""

import json
import argparse
import sys
from pathlib import Path
import re
from typing import List, Dict, Any, Optional

class DatalabJSONParser:
    def __init__(self):
        self.sections = []
        self.current_section_number = ""
        self.current_section_name = ""
        self.current_text_content = []
        self.section_counters = {}  # Track section numbering at each level
        
    def parse_json_file(self, json_file_path: str) -> List[Dict[str, Any]]:
        """
        Parse a Datalab JSON file and extract structured sections
        
        Args:
            json_file_path (str): Path to the JSON file
            
        Returns:
            List[Dict]: Structured sections with metadata
        """
        # Get chapter name from filename
        json_path = Path(json_file_path)
        if not json_path.exists():
            raise FileNotFoundError(f"JSON file not found: {json_file_path}")
        
        chapter_name = json_path.stem.replace('_parsed', '').replace('_', ' ').title()
        
        # Load JSON data
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        print(f"📄 Processing: {json_path.name}")
        print(f"📖 Chapter: {chapter_name}")
        print("-" * 50)
        
        # Reset parser state
        self.sections = []
        self.current_section_number = ""
        self.current_section_name = ""
        self.current_text_content = []
        self.section_counters = {}
        
        # Parse the JSON structure
        self._parse_blocks(json_data, chapter_name)
        
        # Add final section if there's remaining content
        self._finalize_current_section(chapter_name)
        
        print(f"✅ Extracted {len(self.sections)} sections")
        return self.sections
    
    def _parse_blocks(self, data: Dict[str, Any], chapter_name: str, level: int = 0):
        """Recursively parse JSON blocks to extract content"""
        
        # Handle different JSON structures
        if isinstance(data, dict):
            # Check if this is a single block or root structure
            if 'block_type' in data:
                self._process_block(data, chapter_name, level)
            elif 'children' in data:
                # Root structure with children
                for child in data['children']:
                    self._parse_blocks(child, chapter_name, level)
            else:
                # Check for common root keys
                for key in ['pages', 'content', 'blocks']:
                    if key in data:
                        if isinstance(data[key], list):
                            for item in data[key]:
                                self._parse_blocks(item, chapter_name, level)
                        else:
                            self._parse_blocks(data[key], chapter_name, level)
        elif isinstance(data, list):
            # Handle list of blocks
            for item in data:
                self._parse_blocks(item, chapter_name, level)
    
    def _process_block(self, block: Dict[str, Any], chapter_name: str, level: int):
        """Process a single block based on its type"""
        
        block_type = block.get('block_type', '')
        html_content = block.get('html', '')
        section_hierarchy = block.get('section_hierarchy', [])
        
        if block_type == 'SectionHeader':
            # Found a heading - save previous section and start new one
            self._finalize_current_section(chapter_name)
            self._start_new_section(html_content, section_hierarchy)
            
        elif block_type in ['Text', 'TextInlineMath']:
            # Found text content - add to current section
            text_content = self._extract_text_from_html(html_content)
            if text_content.strip():
                self.current_text_content.append(text_content)
        
        elif block_type == 'Table':
            # Found table - add as formatted text
            table_text = self._extract_text_from_html(html_content)
            if table_text.strip():
                self.current_text_content.append(f"\n[TABLE]\n{table_text}\n[/TABLE]\n")
        
        elif block_type in ['ListGroup', 'ListItem']:
            # Found list content - add as formatted text
            list_text = self._extract_text_from_html(html_content)
            if list_text.strip():
                self.current_text_content.append(list_text)
        
        # Process children blocks recursively
        if 'children' in block and isinstance(block['children'], list):
            for child in block['children']:
                self._process_block(child, chapter_name, level + 1)
    
    def _start_new_section(self, html_content: str, section_hierarchy: dict):
        """Start a new section with heading information"""
        
        # Extract clean heading text
        heading_text = self._extract_text_from_html(html_content)
        
        # Generate section number based on hierarchy
        section_number = self._generate_section_number(section_hierarchy)
        
        # Set current section info
        self.current_section_name = heading_text
        self.current_section_number = section_number
        self.current_text_content = []
        
        print(f"📋 Found section: {section_number} - {heading_text}")
    
    def _generate_section_number(self, section_hierarchy: dict) -> str:
        """Generate section number like 1.1, 1.2, 2.1, etc."""
        
        if not section_hierarchy or not isinstance(section_hierarchy, dict):
            return "1"
        
        # Extract hierarchy levels from the dictionary keys
        # Keys like "1", "2", "3" represent h1, h2, h3 levels
        hierarchy_levels = []
        for key in sorted(section_hierarchy.keys()):
            if key.isdigit():
                hierarchy_levels.append(int(key))
        
        if not hierarchy_levels:
            return "1"
        
        # Get the current level (highest level in hierarchy)
        current_level = max(hierarchy_levels)
        
        # Initialize counters for this level if needed
        if current_level not in self.section_counters:
            self.section_counters[current_level] = 0
        
        # Reset counters for deeper levels when we encounter a higher level
        keys_to_remove = [k for k in self.section_counters.keys() if k > current_level]
        for key in keys_to_remove:
            del self.section_counters[key]
        
        # Increment counter for current level
        self.section_counters[current_level] += 1
        
        # Build section number string based on hierarchy
        section_parts = []
        for level in sorted(hierarchy_levels):
            if level in self.section_counters:
                section_parts.append(str(self.section_counters[level]))
            else:
                # Initialize missing levels
                self.section_counters[level] = 1
                section_parts.append("1")
        
        return ".".join(section_parts)
    
    def _finalize_current_section(self, chapter_name: str):
        """Save the current section to the results"""
        
        if self.current_section_name or self.current_text_content:
            # Combine all text content
            combined_text = "\n\n".join(self.current_text_content).strip()
            
            # Only add section if there's meaningful content
            if combined_text or self.current_section_name:
                section_data = {
                    "section_number": self.current_section_number or "0",
                    "text": combined_text,
                    "chapter_name": chapter_name,
                    "section_name": self.current_section_name or "Introduction"
                }
                
                self.sections.append(section_data)
        
        # Reset current section
        self.current_section_number = ""
        self.current_section_name = ""
        self.current_text_content = []
    
    def _extract_text_from_html(self, html_content: str) -> str:
        """Extract clean text from HTML, preserving some formatting"""
        
        if not html_content:
            return ""
        
        # Remove content-ref tags (they're just references)
        text = re.sub(r'<content-ref[^>]*></content-ref>', '', html_content)
        
        # Convert some HTML tags to text equivalents
        text = re.sub(r'<br\s*/?>', '\n', text)
        text = re.sub(r'</p>\s*<p>', '\n\n', text)
        text = re.sub(r'<li[^>]*>', '• ', text)
        text = re.sub(r'</li>', '\n', text)
        text = re.sub(r'<ul[^>]*>', '', text)
        text = re.sub(r'</ul>', '', text)
        
        # Remove all remaining HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Clean up whitespace
        text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)  # Max 2 newlines
        text = re.sub(r'[ \t]+', ' ', text)  # Multiple spaces to single
        text = text.strip()
        
        return text

def save_output(sections: List[Dict[str, Any]], output_path: str):
    """Save the extracted sections to a JSON file"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sections, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved structured output to: {output_path}")

def print_summary(sections: List[Dict[str, Any]]):
    """Print a summary of extracted sections"""
    
    print("\n" + "=" * 60)
    print("📋 EXTRACTION SUMMARY")
    print("=" * 60)
    
    for i, section in enumerate(sections, 1):
        section_num = section['section_number']
        section_name = section['section_name']
        text_length = len(section['text'])
        
        print(f"{i:2d}. Section {section_num}: {section_name}")
        print(f"     Text length: {text_length} characters")
    
    print(f"\n📊 Total sections extracted: {len(sections)}")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(
        description="Parse Datalab JSON output and extract structured sections",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Parse JSON file and save structured output
  python json_parser.py document.json
  
  # Parse JSON file and specify output location
  python json_parser.py document.json --output structured_sections.json
  
  # Parse with summary display
  python json_parser.py document.json --summary
        """
    )
    
    parser.add_argument('json_file', help='Path to the Datalab JSON file')
    parser.add_argument('--output', '-o', 
                       help='Output JSON file path (default: {input_name}_structured.json)')
    parser.add_argument('--summary', '-s', action='store_true',
                       help='Display detailed summary of extracted sections')
    
    args = parser.parse_args()
    
    try:
        # Initialize parser
        json_parser = DatalabJSONParser()
        
        # Parse the JSON file
        sections = json_parser.parse_json_file(args.json_file)
        
        if not sections:
            print("⚠️  No sections were extracted from the JSON file.")
            print("   This might indicate an unsupported JSON structure.")
            sys.exit(1)
        
        # Determine output path
        if args.output:
            output_path = args.output
        else:
            input_path = Path(args.json_file)
            output_path = input_path.parent / f"{input_path.stem}_structured.json"
        
        # Save results
        save_output(sections, str(output_path))
        
        # Show summary if requested
        if args.summary:
            print_summary(sections)
        
        print(f"\n🎉 Successfully extracted {len(sections)} sections!")
        print(f"📂 Structured output saved to: {output_path}")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON file - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()