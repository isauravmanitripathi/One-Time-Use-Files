#!/usr/bin/env python3
"""
Advanced PDF to Markdown/JSON Converter using Marker CLI
Command-line interface with flags for single file and batch processing.

Usage Examples:
  # Process single PDF to markdown
  python3 marker_converter.py --single-pdf --input-file "path/to/file.pdf" --output markdown
  
  # Process single PDF to both formats with LLM
  python3 marker_converter.py --single-pdf --input-file "path/to/file.pdf" --output both --use-llm
  
  # Process all PDFs in folder to JSON
  python3 marker_converter.py --all-pdf --input-folder "path/to/folder" --output json
  
  # Interactive mode (original menu)
  python3 marker_converter.py --interactive
"""

import os
import sys
import subprocess
import shutil
import argparse
from pathlib import Path
from typing import List, Tuple


def setup_argument_parser():
    """Set up command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Advanced PDF to Markdown/JSON Converter using Marker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --single-pdf --input-file "Chapter 1.pdf" --output markdown
  %(prog)s --single-pdf --input-file "Chapter 1.pdf" --output both --use-llm
  %(prog)s --all-pdf --input-folder "/path/to/pdfs" --output json
  %(prog)s --interactive
        """
    )
    
    # Processing mode (mutually exclusive)
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('--single-pdf', action='store_true',
                           help='Process a single PDF file')
    mode_group.add_argument('--all-pdf', action='store_true',
                           help='Process all PDFs in a folder')
    mode_group.add_argument('--interactive', action='store_true',
                           help='Run in interactive mode with menu')
    
    # Input options
    parser.add_argument('--input-file', type=str,
                       help='Path to the PDF file (required for --single-pdf)')
    parser.add_argument('--input-folder', type=str,
                       help='Path to folder containing PDFs (required for --all-pdf)')
    
    # Output format
    parser.add_argument('--output', choices=['markdown', 'json', 'both'],
                       help='Output format: markdown, json, or both')
    
    # Optional flags
    parser.add_argument('--use-llm', action='store_true',
                       help='Use LLM for better accuracy (slower but more accurate)')
    parser.add_argument('--quiet', action='store_true',
                       help='Reduce output verbosity')
    
    return parser


def validate_arguments(args):
    """Validate command line arguments."""
    errors = []
    
    if args.single_pdf:
        if not args.input_file:
            errors.append("--input-file is required when using --single-pdf")
        elif not Path(args.input_file).exists():
            errors.append(f"Input file does not exist: {args.input_file}")
        elif not Path(args.input_file).suffix.lower() == '.pdf':
            errors.append(f"Input file is not a PDF: {args.input_file}")
        
        if not args.output:
            errors.append("--output is required when using --single-pdf")
    
    elif args.all_pdf:
        if not args.input_folder:
            errors.append("--input-folder is required when using --all-pdf")
        elif not Path(args.input_folder).exists():
            errors.append(f"Input folder does not exist: {args.input_folder}")
        elif not Path(args.input_folder).is_dir():
            errors.append(f"Input path is not a directory: {args.input_folder}")
        
        if not args.output:
            errors.append("--output is required when using --all-pdf")
    
    if errors:
        for error in errors:
            print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


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
    pdf_directory = pdf_path.parent
    folder_name = pdf_path.stem
    output_folder = pdf_directory / folder_name
    
    try:
        output_folder.mkdir(exist_ok=True)
        return output_folder
    except Exception as e:
        print(f"Error creating output folder '{output_folder}': {e}")
        raise


def find_files_recursively(directory: Path, pdf_stem: str, output_format: str) -> List[Path]:
    """Find files recursively in directory and subdirectories."""
    found_files = []
    
    if not directory.exists() or not directory.is_dir():
        return found_files
    
    for item in directory.rglob("*"):
        if item.is_file():
            if output_format == "markdown":
                if (item.suffix.lower() in ['.md', '.markdown'] or 
                    item.name == pdf_stem or 
                    item.name.startswith(pdf_stem)):
                    found_files.append(item)
            elif output_format == "json":
                if (item.suffix.lower() == '.json' and 
                    not item.name.endswith('_meta.json') and
                    (item.name == f"{pdf_stem}.json" or item.name == pdf_stem)):
                    found_files.append(item)
    
    return found_files


def cleanup_empty_directories(base_dir: Path, quiet: bool = False):
    """Remove empty directories recursively."""
    if not base_dir.exists() or not base_dir.is_dir():
        return
    
    subdirs = [d for d in base_dir.iterdir() if d.is_dir()]
    
    for subdir in subdirs:
        cleanup_empty_directories(subdir, quiet)
        
        try:
            subdir.rmdir()
            if not quiet:
                print(f"   🗑️  Removed empty directory: {subdir.name}")
        except OSError:
            pass


def organize_marker_output(pdf_path: Path, output_dir: Path, output_format: str, quiet: bool = False) -> bool:
    """Intelligently organize Marker's output files."""
    if not quiet:
        print("   📁 Organizing output files...")
    
    found_files = find_files_recursively(output_dir, pdf_path.stem, output_format)
    
    if not found_files:
        if not quiet:
            print(f"   ❌ No {output_format} files found")
        return False
    
    target_file = output_dir / f"{pdf_path.stem}.{output_format}"
    
    # Find the best file to use
    best_file = None
    for file_path in found_files:
        if file_path.suffix.lower() in [f'.{output_format}', '.md', '.markdown']:
            best_file = file_path
            break
    
    if not best_file and found_files:
        best_file = found_files[0]
    
    if best_file:
        try:
            if best_file == target_file:
                if not quiet:
                    print(f"   ✅ File already properly located: {target_file}")
                return True
            
            if target_file.exists():
                target_file.unlink()
            
            shutil.move(str(best_file), str(target_file))
            if not quiet:
                print(f"   📄 Moved: {best_file.name} → {target_file.name}")
            
            # Move metadata files
            for item in output_dir.rglob("*_meta.json"):
                if item.parent != output_dir:
                    target_meta = output_dir / item.name
                    try:
                        if target_meta.exists():
                            target_meta.unlink()
                        shutil.move(str(item), str(target_meta))
                        if not quiet:
                            print(f"   📄 Moved metadata: {item.name}")
                    except Exception as e:
                        if not quiet:
                            print(f"   ⚠️  Could not move metadata {item.name}: {e}")
            
            cleanup_empty_directories(output_dir, quiet)
            return True
            
        except Exception as e:
            if not quiet:
                print(f"   ❌ Error moving file: {e}")
            return False
    
    return False


def run_marker_conversion(pdf_path: Path, output_dir: Path, output_format: str, use_llm: bool = False, quiet: bool = False) -> bool:
    """Run marker_single command for the specified format."""
    
    cmd = [
        "marker_single",
        str(pdf_path),
        "--output_format", output_format,
        "--output_dir", str(output_dir)
    ]
    
    if use_llm:
        cmd.append("--use_llm")
    
    if not quiet:
        print(f"   Converting to {output_format.upper()}...")
    
    try:
        if quiet:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        else:
            result = subprocess.run(cmd, text=True, timeout=600)
        
        success = organize_marker_output(pdf_path, output_dir, output_format, quiet)
        
        if success:
            final_file = output_dir / f"{pdf_path.stem}.{output_format}"
            if not quiet:
                print(f"   ✅ {output_format.upper()} file created: {final_file}")
            return True
        else:
            if not quiet:
                print(f"   ❌ Failed to organize {output_format.upper()} output")
            return False
            
    except subprocess.TimeoutExpired:
        if not quiet:
            print(f"   ❌ ERROR: Conversion timed out after 10 minutes")
        return False
    except FileNotFoundError:
        print(f"   ❌ ERROR: marker_single command not found. Make sure marker-pdf is installed.")
        return False
    except Exception as e:
        if not quiet:
            print(f"   ❌ ERROR: {e}")
        return False


def get_output_formats(output_choice: str) -> List[str]:
    """Convert output choice to list of formats."""
    if output_choice == "markdown":
        return ["markdown"]
    elif output_choice == "json":
        return ["json"]
    elif output_choice == "both":
        return ["markdown", "json"]
    else:
        return []


def process_single_pdf(pdf_path: Path, output_formats: List[str], use_llm: bool = False, quiet: bool = False) -> Tuple[int, int]:
    """Process a single PDF file."""
    if not quiet:
        print(f"\n📄 Processing: {pdf_path.name}")
    
    try:
        output_folder = create_output_folder(pdf_path)
        if not quiet:
            print(f"📁 Output folder: {output_folder}")
        
        successes = 0
        total = len(output_formats)
        
        for output_format in output_formats:
            if run_marker_conversion(pdf_path, output_folder, output_format, use_llm, quiet):
                successes += 1
        
        if not quiet:
            if successes > 0:
                print(f"✅ Completed {pdf_path.name} ({successes}/{total} formats successful)")
            else:
                print(f"❌ Failed {pdf_path.name} (0/{total} formats successful)")
        
        return successes, total
        
    except Exception as e:
        if not quiet:
            print(f"❌ Error processing {pdf_path.name}: {e}")
        return 0, len(output_formats)


def process_single_file_cli(args):
    """Handle single file processing from command line."""
    pdf_path = Path(args.input_file)
    output_formats = get_output_formats(args.output)
    
    if not args.quiet:
        print("=== Processing Single File ===")
        print(f"Input: {pdf_path}")
        print(f"Output formats: {', '.join(output_formats)}")
        if args.use_llm:
            print("Using LLM: Yes")
        print()
    
    successes, total = process_single_pdf(pdf_path, output_formats, args.use_llm, args.quiet)
    
    if not args.quiet:
        if successes > 0:
            print(f"\n🎉 Successfully converted {successes}/{total} format(s)")
        else:
            print("\n💥 All conversions failed!")


def process_batch_cli(args):
    """Handle batch processing from command line."""
    folder_path = Path(args.input_folder)
    output_formats = get_output_formats(args.output)
    
    pdf_files = find_pdf_files(folder_path)
    
    if not pdf_files:
        print(f"❌ No PDF files found in '{folder_path}'")
        return
    
    if not args.quiet:
        print("=== Batch Processing ===")
        print(f"Input folder: {folder_path}")
        print(f"Output formats: {', '.join(output_formats)}")
        print(f"Files found: {len(pdf_files)}")
        if args.use_llm:
            print("Using LLM: Yes")
        print()
    
    total_successes = 0
    total_conversions = 0
    failed_files = []
    
    for i, pdf_file in enumerate(pdf_files, 1):
        if not args.quiet:
            print(f"[{i}/{len(pdf_files)}] Processing {pdf_file.name}")
        
        successes, total = process_single_pdf(pdf_file, output_formats, args.use_llm, args.quiet)
        
        total_successes += successes
        total_conversions += total
        
        if successes == 0:
            failed_files.append(pdf_file.name)
    
    # Final summary
    if not args.quiet:
        print(f"\n=== Batch Processing Complete ===")
        print(f"📊 Results:")
        print(f"   • Files processed: {len(pdf_files)}")
        print(f"   • Total conversions: {total_successes}/{total_conversions}")
        print(f"   • Success rate: {(total_successes/total_conversions)*100:.1f}%" if total_conversions > 0 else "   • Success rate: 0%")
        
        if failed_files:
            print(f"\n❌ Failed files:")
            for failed_file in failed_files:
                print(f"   • {failed_file}")
        else:
            print(f"\n🎉 All files processed successfully!")


# Interactive mode functions (keeping the original menu system)
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
    pdf_files = find_pdf_files(folder_path)
    
    if not pdf_files:
        print(f"\n❌ No PDF files found in '{folder_path}'")
        return
    
    print(f"\n📚 Found {len(pdf_files)} PDF file(s):")
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"   {i}. {pdf_file.name}")
    
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
    
    for i, pdf_file in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] " + "="*50)
        successes, total = process_single_pdf(pdf_file, output_formats, use_llm)
        
        total_successes += successes
        total_conversions += total
        
        if successes == 0:
            failed_files.append(pdf_file.name)
    
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


def run_interactive_mode():
    """Run the interactive menu mode."""
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
            
            if choice in ["1", "2"]:
                continue_choice = input("\nDo you want to process more files? (y/N): ").strip().lower()
                if continue_choice not in ['y', 'yes']:
                    print("\nGoodbye! 👋")
                    break
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Goodbye! 👋")
        sys.exit(0)


def main():
    """Main function."""
    parser = setup_argument_parser()
    args = parser.parse_args()
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    try:
        if args.interactive:
            run_interactive_mode()
        else:
            validate_arguments(args)
            
            if args.single_pdf:
                process_single_file_cli(args)
            elif args.all_pdf:
                process_batch_cli(args)
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Goodbye! 👋")
        sys.exit(0)


if __name__ == "__main__":
    main()