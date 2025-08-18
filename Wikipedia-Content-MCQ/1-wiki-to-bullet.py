#!/usr/bin/env python3
"""
JSON Content Processor
Processes content.json files from nested folders and extracts enhanced content.
"""

import json
import os
from pathlib import Path
import shutil

def process_content_json(input_folder, output_folder):
    """
    Process all content.json files in nested folders.
    
    Args:
        input_folder (str): Path to the results folder containing nested directories
        output_folder (str): Path to store processed JSON files
    """
    
    input_path = Path(input_folder)
    output_path = Path(output_folder)
    
    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Statistics
    processed_count = 0
    failed_count = 0
    
    print(f"🔍 Scanning folder: {input_path}")
    print(f"📁 Output folder: {output_path}")
    print("-" * 60)
    
    # Iterate through all subdirectories
    for folder_path in input_path.iterdir():
        if folder_path.is_dir():
            folder_name = folder_path.name
            content_json_path = folder_path / "content.json"
            
            if content_json_path.exists():
                try:
                    print(f"📄 Processing: {folder_name}/content.json")
                    
                    # Load the content.json file
                    with open(content_json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Process each section in the JSON array
                    modified_data = []
                    sections_processed = 0
                    
                    for section in data:
                        # Create a clean new section with only essential fields
                        new_section = {}
                        
                        # Keep only the basic required fields
                        essential_fields = [
                            'chapter_name', 
                            'chapter_id', 
                            'section_number', 
                            'section_name'
                        ]
                        
                        # Copy essential fields if they exist
                        for field in essential_fields:
                            if field in section:
                                new_section[field] = section[field]
                        
                        # Replace generated_section_content_md with enhanced_section_content_md
                        if 'enhanced_section_content_md' in section:
                            new_section['generated_section_content_md'] = section['enhanced_section_content_md']
                            sections_processed += 1
                        elif 'generated_section_content_md' in section:
                            # Fallback to original if enhanced doesn't exist
                            new_section['generated_section_content_md'] = section['generated_section_content_md']
                        
                        # Only add sections that have content
                        if 'generated_section_content_md' in new_section:
                            modified_data.append(new_section)
                    
                    # Save to output folder with folder name as filename
                    output_filename = f"{folder_name}.json"
                    output_file_path = output_path / output_filename
                    
                    with open(output_file_path, 'w', encoding='utf-8') as f:
                        json.dump(modified_data, f, indent=2, ensure_ascii=False)
                    
                    print(f"   ✅ Saved as: {output_filename}")
                    print(f"   📊 Sections processed: {sections_processed}/{len(data)}")
                    
                    processed_count += 1
                    
                except Exception as e:
                    print(f"   ❌ Error processing {folder_name}: {str(e)}")
                    failed_count += 1
            else:
                print(f"   ⚠️  No content.json found in: {folder_name}")
    
    # Summary
    print("-" * 60)
    print(f"📈 Processing Summary:")
    print(f"   ✅ Successfully processed: {processed_count} files")
    print(f"   ❌ Failed: {failed_count} files")
    print(f"   📁 Output location: {output_path}")
    
    if processed_count > 0:
        print(f"\n🎉 Processing complete! Check {output_path} for your files.")
    else:
        print(f"\n⚠️  No files were processed. Please check the input path.")

def main():
    """Main function to run the processor"""
    
    # Define paths
    input_folder = "/Volumes/hard-drive/miscellaneous-files/wikipedia/wiki-gov-exam/json/results"
    output_folder = "/Volumes/hard-drive/miscellaneous-files/json_parser/processed-files"
    
    print("🚀 JSON Content Processor")
    print("=" * 60)
    
    # Check if input folder exists
    if not Path(input_folder).exists():
        print(f"❌ Input folder not found: {input_folder}")
        print("Please check the path and try again.")
        return
    
    # Process the files
    process_content_json(input_folder, output_folder)

if __name__ == "__main__":
    main()