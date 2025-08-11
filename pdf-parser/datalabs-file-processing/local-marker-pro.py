#!/usr/bin/env python3
"""
Simple PDF to Markdown/JSON Converter using Marker CLI
This script runs marker_single commands to convert PDFs to both Markdown and JSON.
"""

import os
import sys
import subprocess
from pathlib import Path


def get_user_input():
    """Get PDF file path and output directory from user input."""
    
    # Get PDF file path
    while True:
        pdf_path_str = input("Enter the path to the PDF file: ").strip().strip('"\'')
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
            
        break
    
    # Get output directory path
    while True:
        output_dir_str = input("Enter the output directory path: ").strip().strip('"\'')
        if not output_dir_str:
            print("Please enter a valid output directory path.")
            continue
            
        output_dir = Path(output_dir_str)
        
        # Create directory if it doesn't exist
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory '{output_dir}': {e}")
            continue
            
        if not output_dir.is_dir():
            print(f"Error: Could not create or access directory '{output_dir}'.")
            continue
            
        break
    
    return pdf_path, output_dir


def run_marker_command(pdf_path, output_dir, output_format):
    """Run marker_single command for the specified format."""
    
    cmd = [
        "marker_single",
        str(pdf_path),
        "--output_format", output_format,
        "--output_dir", str(output_dir)
    ]
    
    print(f"\nRunning command for {output_format.upper()}:")
    print(" ".join(f'"{arg}"' if " " in arg else arg for arg in cmd))
    print()
    
    try:
        # Run the command and show output in real-time
        result = subprocess.run(cmd, text=True, timeout=600)  # 10 minute timeout
        
        if result.returncode == 0:
            expected_file = output_dir / f"{pdf_path.stem}.{output_format}"
            if expected_file.exists():
                print(f"✅ SUCCESS: {output_format.upper()} file created: {expected_file}")
                return True
            else:
                print(f"⚠️  Command completed but file not found: {expected_file}")
                return False
        else:
            print(f"❌ ERROR: Command failed with return code {result.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"❌ ERROR: Command timed out after 10 minutes")
        return False
    except FileNotFoundError:
        print(f"❌ ERROR: marker_single command not found. Make sure marker-pdf is installed.")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


def main():
    """Main function."""
    print("=== Simple PDF to Markdown/JSON Converter using Marker ===\n")
    
    # Get user input
    try:
        pdf_path, output_dir = get_user_input()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    
    print(f"\n📄 PDF File: {pdf_path}")
    print(f"📁 Output Directory: {output_dir}")
    
    # Ask if user wants to use LLM
    use_llm = input("\nUse LLM for better accuracy? (y/N): ").strip().lower() in ['y', 'yes']
    
    # Convert to Markdown
    print("\n" + "="*60)
    print("CONVERTING TO MARKDOWN")
    print("="*60)
    
    md_cmd = [
        "marker_single",
        str(pdf_path),
        "--output_format", "markdown",
        "--output_dir", str(output_dir)
    ]
    
    if use_llm:
        md_cmd.append("--use_llm")
    
    print("Running command:")
    print(" ".join(f'"{arg}"' if " " in arg else arg for arg in md_cmd))
    print()
    
    try:
        md_result = subprocess.run(md_cmd, text=True, timeout=600)
        md_file = output_dir / f"{pdf_path.stem}.md"
        
        # Check if file was created (regardless of return code)
        if md_file.exists():
            print(f"✅ SUCCESS: Markdown file created: {md_file}")
            md_success = True
        else:
            print(f"❌ FAILED: Markdown file not found: {md_file}")
            print(f"   Return code: {md_result.returncode}")
            md_success = False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        md_success = False
    
    # Convert to JSON
    print("\n" + "="*60)
    print("CONVERTING TO JSON")
    print("="*60)
    
    json_cmd = [
        "marker_single",
        str(pdf_path),
        "--output_format", "json",
        "--output_dir", str(output_dir)
    ]
    
    if use_llm:
        json_cmd.append("--use_llm")
    
    print("Running command:")
    print(" ".join(f'"{arg}"' if " " in arg else arg for arg in json_cmd))
    print()
    
    try:
        json_result = subprocess.run(json_cmd, text=True, timeout=600)
        json_file = output_dir / f"{pdf_path.stem}.json"
        
        # Check if file was created (regardless of return code)
        if json_file.exists():
            print(f"✅ SUCCESS: JSON file created: {json_file}")
            json_success = True
        else:
            print(f"❌ FAILED: JSON file not found: {json_file}")
            print(f"   Return code: {json_result.returncode}")
            json_success = False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        json_success = False
    
    # Final summary
    print("\n" + "="*60)
    print("CONVERSION SUMMARY")
    print("="*60)
    
    if md_success:
        print(f"✅ Markdown: {output_dir / f'{pdf_path.stem}.md'}")
    else:
        print("❌ Markdown: Failed")
    
    if json_success:
        print(f"✅ JSON: {output_dir / f'{pdf_path.stem}.json'}")
    else:
        print("❌ JSON: Failed")
    
    if md_success or json_success:
        print(f"\n📁 All output files are in: {output_dir}")
        print("🎉 Conversion completed!")
    else:
        print("\n💥 All conversions failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()