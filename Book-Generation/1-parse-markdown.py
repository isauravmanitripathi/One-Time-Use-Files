import json
import re
import sys
from pathlib import Path

def parse_markdown_to_json(markdown_content: str, chapter_name: str = "Document") -> list:
    """
    Parses clean markdown content and converts it into a structured JSON format.
    
    Args:
        markdown_content (str): The markdown content to parse
        chapter_name (str): Name for the chapter (defaults to "Document")
    
    Returns:
        list: List of dictionaries with structured section data
    """
    lines = markdown_content.split('\n')
    
    preliminary_data = []
    current_section = None
    
    # Find the first heading to separate intro content
    first_heading_index = -1
    for i, line in enumerate(lines):
        if line.strip().startswith('#'):
            first_heading_index = i
            break

    # Split content into intro and body sections
    intro_content_lines = lines[:first_heading_index] if first_heading_index != -1 else lines
    body_lines = lines[first_heading_index:] if first_heading_index != -1 else []

    # Process introduction content (content before first heading)
    intro_text = "\n".join(intro_content_lines).strip()
    if intro_text:
        preliminary_data.append({
            "level": 1,
            "section_name": "Introduction",
            "generated_section_content_md": intro_text
        })

    # Process headings and their content
    for line in body_lines:
        # Check if line is a heading
        heading_match = re.match(r'^(#+)\s+(.*)', line)
        if heading_match:
            # Save previous section if it exists
            if current_section:
                current_section["generated_section_content_md"] = current_section["generated_section_content_md"].strip()
                preliminary_data.append(current_section)
            
            # Start new section
            level = len(heading_match.group(1))  # Count # symbols
            heading_text = heading_match.group(2).strip()
            current_section = {
                "level": level,
                "section_name": heading_text,
                "generated_section_content_md": ""
            }
        elif current_section:
            # Add content to current section
            current_section["generated_section_content_md"] += "\n" + line.strip()

    # Don't forget the last section
    if current_section:
        current_section["generated_section_content_md"] = current_section["generated_section_content_md"].strip()
        preliminary_data.append(current_section)

    # Filter out sections with no content
    filtered_data = [s for s in preliminary_data if s["generated_section_content_md"]]
    
    # Create final JSON structure with hierarchical numbering
    final_json_data = []
    counters = [0] * 6  # Support up to 6 levels of nesting

    for section in filtered_data:
        level = section["level"]
        
        # Special handling for Introduction
        if section["section_name"] == "Introduction":
            section_number = "1"
        else:
            # Calculate hierarchical section numbering
            counter_index = level - 2  # Adjust for 0-based indexing
            if 0 <= counter_index < len(counters):
                counters[counter_index] += 1
                # Reset all deeper level counters
                for i in range(counter_index + 1, len(counters)):
                    counters[i] = 0
                
                # Build section number (e.g., "1.2.3")
                section_number_parts = [str(c) for c in counters[:counter_index + 1]]
                section_number = ".".join(section_number_parts)
            else:
                section_number = "invalid_level"

        # Create final section object
        final_json_data.append({
            "chapter_name": chapter_name,
            "chapter_id": "1",
            "section_number": section_number,
            "section_name": section["section_name"],
            "generated_section_content_md": section["generated_section_content_md"]
        })

    return final_json_data

def markdown_file_to_json(input_md_path: str, output_json_path: str = None, chapter_name: str = None):
    """
    Reads a markdown file and converts it to structured JSON.
    
    Args:
        input_md_path (str): Path to input markdown file
        output_json_path (str): Path for output JSON file (optional)
        chapter_name (str): Name for the chapter (optional, uses filename if not provided)
    """
    # Validate input file
    input_path = Path(input_md_path)
    if not input_path.exists():
        print(f"❌ Error: File '{input_md_path}' not found.")
        return
    
    # Set default output path if not provided
    if output_json_path is None:
        output_json_path = input_path.with_suffix('.json')
    
    # Set default chapter name if not provided
    if chapter_name is None:
        chapter_name = input_path.stem.replace('_', ' ').title()
    
    try:
        # Read markdown content
        with open(input_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Parse markdown to JSON
        json_data = parse_markdown_to_json(markdown_content, chapter_name)
        
        # Write JSON output
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Successfully converted '{input_md_path}' to '{output_json_path}'")
        print(f"📄 Found {len(json_data)} sections")
        
        # Show section summary
        for section in json_data:
            print(f"   {section['section_number']}. {section['section_name']}")
            
    except Exception as e:
        print(f"❌ Error processing file: {e}")

def markdown_string_to_json(markdown_string: str, chapter_name: str = "Document") -> str:
    """
    Converts a markdown string directly to JSON string.
    
    Args:
        markdown_string (str): Markdown content as string
        chapter_name (str): Name for the chapter
        
    Returns:
        str: JSON string
    """
    json_data = parse_markdown_to_json(markdown_string, chapter_name)
    return json.dumps(json_data, indent=4, ensure_ascii=False)

# Example usage and CLI interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python markdown_parser.py <input.md> [output.json] [chapter_name]")
        print("\nExample:")
        print("  python markdown_parser.py document.md")
        print("  python markdown_parser.py document.md output.json 'My Document'")
        
        # Demo with sample markdown
        print("\n--- Demo with sample markdown ---")
        sample_md = """This is some introduction text before any headings.

# Main Section
This is content under the main section.

## Subsection A
Content for subsection A.

### Deep Subsection
Very specific content here.

## Subsection B  
Content for subsection B.

# Another Main Section
More main content here.
"""
        
        result = markdown_string_to_json(sample_md, "Sample Document")
        print("Sample JSON output:")
        print(result)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        chapter_name = sys.argv[3] if len(sys.argv) > 3 else None
        
        markdown_file_to_json(input_file, output_file, chapter_name)