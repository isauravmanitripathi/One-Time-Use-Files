#!/usr/bin/env python3
"""
PDF Merger Tool
Takes two PDFs and merges them in this order:
1. First page of PDF 2
2. All pages from PDF 1 
3. Remaining pages from PDF 2 (page 2 onwards)
"""

import sys
from pathlib import Path

# Check for required library
try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("Error: PyPDF2 library not found!")
    print("Install with: pip install PyPDF2")
    sys.exit(1)

def validate_pdf_file(file_path: Path) -> bool:
    """Validate that the file exists and is a valid PDF."""
    if not file_path.exists():
        print(f"Error: File '{file_path}' does not exist")
        return False
    
    if not file_path.suffix.lower() == '.pdf':
        print(f"Error: '{file_path}' is not a PDF file")
        return False
    
    try:
        # Try to read the PDF to verify it's valid
        reader = PdfReader(str(file_path))
        page_count = len(reader.pages)
        print(f"Valid PDF: {file_path.name} ({page_count} pages)")
        return True
    except Exception as e:
        print(f"Error: Cannot read PDF '{file_path}': {e}")
        return False

def get_pdf_info(file_path: Path) -> tuple:
    """Get PDF information including page count."""
    try:
        reader = PdfReader(str(file_path))
        page_count = len(reader.pages)
        file_size_mb = file_path.stat().st_size / (1024 * 1024)
        return page_count, file_size_mb, reader
    except Exception as e:
        print(f"Error reading PDF info: {e}")
        return 0, 0, None

def merge_pdfs(pdf1_path: Path, pdf2_path: Path, output_path: Path) -> bool:
    """
    Merge PDFs in this order:
    1. First page of PDF2
    2. All pages from PDF1  
    3. Remaining pages from PDF2 (page 2 onwards)
    """
    try:
        print("\nStarting PDF merge process...")
        
        # Read both PDFs
        reader1 = PdfReader(str(pdf1_path))
        reader2 = PdfReader(str(pdf2_path))
        
        pdf1_pages = len(reader1.pages)
        pdf2_pages = len(reader2.pages)
        
        print(f"PDF 1: {pdf1_pages} pages")
        print(f"PDF 2: {pdf2_pages} pages")
        
        # Check if PDF 2 has at least 1 page
        if pdf2_pages < 1:
            print("Error: PDF 2 must have at least 1 page")
            return False
        
        # Create writer for output
        writer = PdfWriter()
        
        # Step 1: Add first page of PDF 2
        print("Adding first page of PDF 2...")
        writer.add_page(reader2.pages[0])
        
        # Step 2: Add ALL pages from PDF 1
        print(f"Adding all {pdf1_pages} pages from PDF 1...")
        for page_num in range(pdf1_pages):
            writer.add_page(reader1.pages[page_num])
        
        # Step 3: Add remaining pages from PDF 2 (if any)
        if pdf2_pages > 1:
            remaining_pages = pdf2_pages - 1
            print(f"Adding remaining {remaining_pages} pages from PDF 2...")
            for page_num in range(1, pdf2_pages):
                writer.add_page(reader2.pages[page_num])
        else:
            print("PDF 2 has only 1 page, no additional pages to add")
        
        # Calculate final page count
        final_page_count = 1 + pdf1_pages + max(0, pdf2_pages - 1)
        
        # Write the merged PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"Merged PDF created: {output_path}")
        print(f"Final page count: {final_page_count}")
        
        return True
        
    except Exception as e:
        print(f"Error during PDF merge: {e}")
        return False

def get_user_input():
    """Get PDF file paths from user."""
    print("PDF MERGER TOOL")
    print("="*50)
    print("Merges: PDF2[page1] + PDF1[all pages] + PDF2[remaining pages]")
    
    # Get PDF 1 path
    if len(sys.argv) >= 2:
        pdf1_path = Path(sys.argv[1])
    else:
        pdf1_input = input("\nEnter path to PDF 1 (will be inserted): ").strip()
        pdf1_path = Path(pdf1_input)
    
    # Get PDF 2 path  
    if len(sys.argv) >= 3:
        pdf2_path = Path(sys.argv[2])
    else:
        pdf2_input = input("Enter path to PDF 2 (first page stays first): ").strip()
        pdf2_path = Path(pdf2_input)
    
    return pdf1_path, pdf2_path

def create_output_filename(pdf1_path: Path, pdf2_path: Path) -> Path:
    """Create output filename based on input files."""
    # Use the same directory as PDF 2
    output_dir = pdf2_path.parent
    
    # Create descriptive filename
    pdf1_name = pdf1_path.stem
    pdf2_name = pdf2_path.stem
    
    output_filename = f"merged_{pdf2_name}_with_{pdf1_name}.pdf"
    return output_dir / output_filename

def main():
    """Main function for PDF merging."""
    print("PDF MERGER - INSERT PDF1 INTO PDF2")
    print("="*50)
    print("Result: [PDF2-Page1] + [PDF1-AllPages] + [PDF2-RemainingPages]")
    
    # Get input files
    pdf1_path, pdf2_path = get_user_input()
    
    print(f"\nValidating input files...")
    
    # Validate both PDFs
    if not validate_pdf_file(pdf1_path):
        return
    if not validate_pdf_file(pdf2_path):
        return
    
    # Get PDF information
    pdf1_pages, pdf1_size, _ = get_pdf_info(pdf1_path)
    pdf2_pages, pdf2_size, _ = get_pdf_info(pdf2_path)
    
    if pdf1_pages == 0 or pdf2_pages == 0:
        print("Error: Could not read PDF page information")
        return
    
    print(f"\nPDF Analysis:")
    print(f"   PDF 1: {pdf1_path.name}")
    print(f"      Pages: {pdf1_pages}")
    print(f"      Size: {pdf1_size:.1f} MB")
    print(f"   PDF 2: {pdf2_path.name}")
    print(f"      Pages: {pdf2_pages}")  
    print(f"      Size: {pdf2_size:.1f} MB")
    
    # Show merge plan
    final_pages = 1 + pdf1_pages + max(0, pdf2_pages - 1)
    print(f"\nMerge Plan:")
    print(f"   Page 1: From PDF 2 (page 1)")
    print(f"   Pages 2-{1+pdf1_pages}: From PDF 1 (all {pdf1_pages} pages)")
    if pdf2_pages > 1:
        print(f"   Pages {2+pdf1_pages}-{final_pages}: From PDF 2 (pages 2-{pdf2_pages})")
    print(f"   Final PDF: {final_pages} total pages")
    
    # Confirm with user
    confirm = input(f"\nProceed with merge? (y/n): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("Merge cancelled")
        return
    
    # Create output filename
    output_path = create_output_filename(pdf1_path, pdf2_path)
    
    # Check if output file already exists
    if output_path.exists():
        overwrite = input(f"\nOutput file exists: {output_path.name}\nOverwrite? (y/n): ").strip().lower()
        if overwrite not in ['y', 'yes']:
            # Create alternative filename
            counter = 1
            while output_path.exists():
                base_name = output_path.stem
                output_path = output_path.parent / f"{base_name}_{counter}.pdf"
                counter += 1
            print(f"Using alternative filename: {output_path.name}")
    
    # Perform the merge
    if merge_pdfs(pdf1_path, pdf2_path, output_path):
        final_size_mb = output_path.stat().st_size / (1024 * 1024)
        
        print(f"\nSUCCESS! PDF merge completed.")
        print(f"\nOutput Details:")
        print(f"   File: {output_path}")
        print(f"   Pages: {final_pages}")
        print(f"   Size: {final_size_mb:.1f} MB")
        
        print(f"\nMerge Summary:")
        print(f"   PDF 2 first page: Preserved at beginning")
        print(f"   PDF 1 all pages: Inserted after page 1") 
        print(f"   PDF 2 remaining: Added at end")
        
        # Show page breakdown
        print(f"\nPage Breakdown:")
        print(f"   Page 1: {pdf2_path.name} (original page 1)")
        if pdf1_pages == 1:
            print(f"   Page 2: {pdf1_path.name} (only page)")
        else:
            print(f"   Pages 2-{1+pdf1_pages}: {pdf1_path.name} (pages 1-{pdf1_pages})")
        
        if pdf2_pages > 1:
            start_page = 2 + pdf1_pages
            end_page = final_pages
            print(f"   Pages {start_page}-{end_page}: {pdf2_path.name} (original pages 2-{pdf2_pages})")
    else:
        print("Failed to merge PDFs")

if __name__ == "__main__":
    # Usage instructions
    if len(sys.argv) == 1:
        print("Usage:")
        print(f"  {sys.argv[0]} <pdf1_path> <pdf2_path>")
        print("  OR run without arguments for interactive mode")
        print()
    
    main()