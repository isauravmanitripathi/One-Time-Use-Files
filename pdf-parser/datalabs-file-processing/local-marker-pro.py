#!/usr/bin/env python3
"""
Advanced PDF to Markdown/JSON Converter using Marker CLI
Supports single file and batch folder processing with custom output formats.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple


def show_menu():
    """Display the main menu."""
    print("=== Advanced PDF to Markdown/JSON Converter using Marker ===\n")
    print("Choose processing mode:")
    print("1. Process a single PDF file")
    print("2. Process all PDFs in a folder (batch)")
    print("3. Exit")
    return input("\nEnter your choice (1-3): ").strip()


def choose_output_formats():
    """Let user choose which output formats to generate."""
    print("\nChoose output format(s):")
    print("1. Markdown only (.md)")
    print("2. JSON only (.json)")
    print("3. Both Markdown and JSON")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == "1":
            return ["markdown"]
        elif choice == "2":
            return ["json"]
        elif choice == "3":
            return ["markdown", "json"]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_single_file_input():
    """Get single PDF file path from user."""
    while True:
        pdf_path_str = input("\nEnter the path to the PDF file: ").strip().strip('"\'')
        if not pdf_path_str:
            print("Please enter a valid path.")
            continue
            
        pdf_path = Path(pdf_path_str)
        
        if not pdf_path.exists():
            print(f"Error: File '{pdf_path}' does not exist.")
            continue
            
        if not pdf_path.is_file():
            print(f"Error: '{pdf_path}' is not a file.")
            continue
            
        if pdf_path.suffix.lower() != '.pdf':
            print(f"Error: '{pdf_path}' is not a PDF file.")
            continue
            
        return pdf_path


def get_folder_input():
    """Get folder path from user."""
    while True:
        folder_path_str = input("\nEnter the path to the folder containing PDFs: ").strip().strip('"\'')
        if not folder_path_str:
            print("Please enter a valid path.")
            continue
            
        folder_path = Path(folder_path_str)
        
        if not folder_path.exists():
            print(f"Error: Folder '{folder_path}' does not exist.")
            continue
            
        if not folder_path.is_dir():
            print(f"Error: '{folder_path}' is not a directory.")
            continue
            
        return folder_path


def find_pdf_files(folder_path: Path) -> List[Path]:
    """Find all PDF files in the given folder."""
    pdf_files = []
    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() == '.pdf':
            pdf_files.append(file_path)
    
    pdf_files.sort()  # Sort alphabetically
    return pdf_files


def create_output_folder(pdf_path: Path) -> Path:
    """Create output folder next to the PDF file with the same name as the PDF."""
    # Get the folder where the PDF is located
    pdf_directory = pdf_path.parent
    
    # Create folder name (PDF name without extension)
    folder_name = pdf_path.stem
    
    # Create the output folder path
    output_folder = pdf_directory / folder_name
    
    # Create the folder
    try:
        output_folder.mkdir(exist_ok=True)
        return output_folder
    except Exception as e:
        print(f"Error creating output folder '{output_folder}': {e}")
        raise


def run_marker_conversion(pdf_path: Path, output_dir: Path, output_format: str, use_llm: bool = False) -> bool:
    """Run marker_single command for the specified format."""
    
    cmd = [
        "marker_single",
        str(pdf_path),
        "--output_format", output_format,
        "--output_dir", str(output_dir)
    ]
    
    if use_llm:
        cmd.append("--use_llm")
    
    print(f"   Converting to {output_format.upper()}...")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        
        # Marker seems to create files in different ways, let's check multiple possible locations
        possible_files = [
            output_dir / f"{pdf_path.stem}.{output_format}",  # Expected location
            output_dir / f"{pdf_path.stem}",  # Without extension (as seen in logs)
            output_dir / pdf_path.stem / f"{pdf_path.stem}.{output_format}",  # Nested folder
            output_dir / pdf_path.stem / f"{pdf_path.stem}",  # Nested without extension
        ]
        
        # Find which file was actually created
        created_file = None
        for possible_file in possible_files:
            if possible_file.exists():
                created_file = possible_file
                break
        
        if created_file:
            # If file was created in a nested folder, move it to the main output directory
            if created_file.parent != output_dir:
                target_file = output_dir / f"{pdf_path.stem}.{output_format}"
                try:
                    # Move/copy the file to the correct location
                    import shutil
                    shutil.move(str(created_file), str(target_file))
                    created_file = target_file
                    
                    # Clean up empty nested folder if it exists
                    nested_folder = output_dir / pdf_path.stem
                    if nested_folder.exists() and nested_folder.is_dir():
                        try:
                            nested_folder.rmdir()  # Only removes if empty
                        except:
                            pass  # Ignore if folder is not empty
                except Exception as e:
                    print(f"   Warning: Could not move file: {e}")
            
            # Ensure the file has the correct extension
            if not created_file.name.endswith(f".{output_format}"):
                correct_name = output_dir / f"{pdf_path.stem}.{output_format}"
                try:
                    import shutil
                    shutil.move(str(created_file), str(correct_name))
                    created_file = correct_name
                except Exception as e:
                    print(f"   Warning: Could not rename file: {e}")
            
            print(f"   ✅ {output_format.upper()} file created: {created_file}")
            return True
        else:
            print(f"   ❌ {output_format.upper()} file not found in any expected location")
            print(f"   Checked locations:")
            for pf in possible_files:
                print(f"     - {pf}")
            if result.stderr:
                print(f"   Error output: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"   ❌ ERROR: Conversion timed out after 10 minutes")
        return False
    except FileNotFoundError:
        print(f"   ❌ ERROR: marker_single command not found. Make sure marker-pdf is installed.")
        return False
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        return False


def process_single_pdf(pdf_path: Path, output_formats: List[str], use_llm: bool = False) -> Tuple[int, int]:
    """Process a single PDF file."""
    print(f"\n📄 Processing: {pdf_path.name}")
    
    try:
        # Create output folder
        output_folder = create_output_folder(pdf_path)
        print(f"📁 Output folder: {output_folder}")
        
        successes = 0
        total = len(output_formats)
        
        # Convert to each requested format
        for output_format in output_formats:
            if run_marker_conversion(pdf_path, output_folder, output_format, use_llm):
                successes += 1
        
        if successes > 0:
            print(f"✅ Completed {pdf_path.name} ({successes}/{total} formats successful)")
        else:
            print(f"❌ Failed {pdf_path.name} (0/{total} formats successful)")
        
        return successes, total
        
    except Exception as e:
        print(f"❌ Error processing {pdf_path.name}: {e}")
        return 0, len(output_formats)


def process_single_file_mode():
    """Handle single file processing mode."""
    pdf_path = get_single_file_input()
    output_formats = choose_output_formats()
    
    use_llm = input("\nUse LLM for better accuracy? (y/N): ").strip().lower() in ['y', 'yes']
    
    print(f"\n{'='*60}")
    print("PROCESSING SINGLE FILE")
    print(f"{'='*60}")
    
    successes, total = process_single_pdf(pdf_path, output_formats, use_llm)
    
    print(f"\n{'='*60}")
    print("PROCESSING COMPLETE")
    print(f"{'='*60}")
    
    if successes > 0:
        print(f"🎉 Successfully converted {successes}/{total} format(s)")
    else:
        print("💥 All conversions failed!")


def process_batch_mode():
    """Handle batch processing mode."""
    folder_path = get_folder_input()
    
    # Find PDF files
    pdf_files = find_pdf_files(folder_path)
    
    if not pdf_files:
        print(f"\n❌ No PDF files found in '{folder_path}'")
        return
    
    print(f"\n📚 Found {len(pdf_files)} PDF file(s):")
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"   {i}. {pdf_file.name}")
    
    # Confirm processing
    confirm = input(f"\nProcess all {len(pdf_files)} PDF files? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("Batch processing cancelled.")
        return
    
    output_formats = choose_output_formats()
    use_llm = input("\nUse LLM for better accuracy? (y/N): ").strip().lower() in ['y', 'yes']
    
    print(f"\n{'='*60}")
    print("BATCH PROCESSING STARTED")
    print(f"{'='*60}")
    
    total_successes = 0
    total_conversions = 0
    failed_files = []
    
    # Process each PDF
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] " + "="*50)
        successes, total = process_single_pdf(pdf_file, output_formats, use_llm)
        
        total_successes += successes
        total_conversions += total
        
        if successes == 0:
            failed_files.append(pdf_file.name)
    
    # Final summary
    print(f"\n{'='*60}")
    print("BATCH PROCESSING COMPLETE")
    print(f"{'='*60}")
    
    print(f"📊 Overall Results:")
    print(f"   • Files processed: {len(pdf_files)}")
    print(f"   • Total conversions: {total_successes}/{total_conversions}")
    print(f"   • Success rate: {(total_successes/total_conversions)*100:.1f}%" if total_conversions > 0 else "   • Success rate: 0%")
    
    if failed_files:
        print(f"\n❌ Files that failed completely:")
        for failed_file in failed_files:
            print(f"   • {failed_file}")
    else:
        print(f"\n🎉 All files processed successfully!")


def main():
    """Main function."""
    try:
        while True:
            choice = show_menu()
            
            if choice == "1":
                process_single_file_mode()
                
            elif choice == "2":
                process_batch_mode()
                
            elif choice == "3":
                print("\nGoodbye! 👋")
                break
                
            else:
                print("\n❌ Invalid choice. Please enter 1, 2, or 3.")
                continue
            
            # Ask if user wants to continue
            if choice in ["1", "2"]:
                continue_choice = input("\nDo you want to process more files? (y/N): ").strip().lower()
                if continue_choice not in ['y', 'yes']:
                    print("\nGoodbye! 👋")
                    break
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Goodbye! 👋")
        sys.exit(0)


if __name__ == "__main__":
    main()