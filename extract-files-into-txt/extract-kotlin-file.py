#!/usr/bin/env python3
"""
Android Project File Extractor
Extracts content from .kt and .gradle.kts files in an Android project
Ignores common build/IDE folders and files
"""

import os
import datetime

def should_ignore_folder(folder_name):
    """Check if folder should be ignored"""
    ignore_folders = {
        '.git', '.idea', '.kotlin', '.gradle', 
        'build', 'gradle', '.settings', 
        'bin', 'gen', 'out', '__pycache__'
    }
    return folder_name in ignore_folders

def should_ignore_file(file_name):
    """Check if file should be ignored"""
    ignore_files = {
        '.gitignore', '.DS_Store', 'local.properties',
        'gradle-wrapper.jar', 'gradle-wrapper.properties'
    }
    ignore_extensions = {'.class', '.dex', '.ap_', '.apk', '.jar', '.war', '.ear'}
    
    if file_name in ignore_files:
        return True
    
    _, ext = os.path.splitext(file_name)
    return ext in ignore_extensions

def extract_project_files(project_path, output_file):
    """Extract .kt and .gradle.kts files from Android project"""
    
    target_extensions = {'.kt', '.kts'}
    extracted_files = []
    
    print(f"Scanning project: {project_path}")
    print(f"Output file: {output_file}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write("=" * 80 + "\n")
        f.write("GOVERNMENT EXAM GURU APP - PROJECT FILES EXTRACTION\n")
        f.write("=" * 80 + "\n")
        f.write(f"Extraction Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Project Path: {project_path}\n")
        f.write("=" * 80 + "\n\n")
        
        # Walk through directory
        for root, dirs, files in os.walk(project_path):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if not should_ignore_folder(d)]
            
            for file in files:
                # Check if file should be processed
                if should_ignore_file(file):
                    continue
                
                file_path = os.path.join(root, file)
                _, ext = os.path.splitext(file)
                
                # Process .kt and .gradle.kts files
                if ext in target_extensions or file.endswith('.gradle.kts'):
                    try:
                        # Calculate relative path from project root
                        rel_path = os.path.relpath(file_path, project_path)
                        
                        print(f"Processing: {rel_path}")
                        
                        # Write file header
                        f.write("\n" + "=" * 60 + "\n")
                        f.write(f"FILE: {rel_path}\n")
                        f.write(f"FULL PATH: {file_path}\n")
                        f.write("=" * 60 + "\n\n")
                        
                        # Read and write file content
                        with open(file_path, 'r', encoding='utf-8') as source_file:
                            content = source_file.read()
                            f.write(content)
                            
                        f.write("\n\n")
                        extracted_files.append(rel_path)
                        
                    except Exception as e:
                        f.write(f"ERROR READING FILE: {e}\n\n")
                        print(f"Error reading {rel_path}: {e}")
        
        # Write summary
        f.write("\n" + "=" * 80 + "\n")
        f.write("EXTRACTION SUMMARY\n")
        f.write("=" * 80 + "\n")
        f.write(f"Total files extracted: {len(extracted_files)}\n\n")
        f.write("Files processed:\n")
        for file_path in sorted(extracted_files):
            f.write(f"  - {file_path}\n")
        f.write("\n" + "=" * 80 + "\n")
    
    print(f"\nExtraction completed!")
    print(f"Total files extracted: {len(extracted_files)}")
    print(f"Output saved to: {output_file}")

def main():
    # Project configuration
    project_path = "/Users/sauravtripathi/AndroidStudioProjects/GovernmentExamGuruApp"
    output_file = "government_exam_guru_project_files.txt"
    
    # Check if project path exists
    if not os.path.exists(project_path):
        print(f"Error: Project path does not exist: {project_path}")
        return
    
    # Extract files
    extract_project_files(project_path, output_file)

if __name__ == "__main__":
    main()