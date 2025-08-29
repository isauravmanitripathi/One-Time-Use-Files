#!/usr/bin/env python3
"""
PDF Analyzer - Analyzes PDF files for page count, printing requirements, and page dimensions
"""

import PyPDF2
import math
import os

def get_pdf_info(pdf_path):
    """
    Analyze PDF file and return detailed information
    """
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Get total number of pages
            total_pages = len(pdf_reader.pages)
            
            # Calculate pages needed for double-sided printing
            double_sided_sheets = math.ceil(total_pages / 2)
            
            # Get first page to analyze dimensions
            first_page = pdf_reader.pages[0]
            
            # Get page dimensions (in points - PDF default unit)
            # 1 point = 1/72 inch
            mediabox = first_page.mediabox
            width_points = float(mediabox.width)
            height_points = float(mediabox.height)
            
            # Convert to inches (1 point = 1/72 inch)
            width_inches = width_points / 72
            height_inches = height_points / 72
            
            # Convert to centimeters (1 inch = 2.54 cm)
            width_cm = width_inches * 2.54
            height_cm = height_inches * 2.54
            
            return {
                'total_pages': total_pages,
                'double_sided_sheets': double_sided_sheets,
                'dimensions': {
                    'points': (width_points, height_points),
                    'inches': (width_inches, height_inches),
                    'cm': (width_cm, height_cm)
                }
            }
            
    except FileNotFoundError:
        return None
    except Exception as e:
        return {'error': str(e)}

def format_dimensions(width, height, unit):
    """Format dimensions with appropriate precision"""
    return f"{width:.2f} x {height:.2f} {unit}"

def main():
    """Main function to run the PDF analyzer"""
    print("=" * 60)
    print("         PDF ANALYZER")
    print("=" * 60)
    
    while True:
        # Get PDF path from user
        pdf_path = input("\nEnter the path to your PDF file (or 'quit' to exit): ").strip()
        
        if pdf_path.lower() in ['quit', 'exit', 'q']:
            print("Thanks for using PDF Analyzer!")
            break
            
        # Remove quotes if user wrapped path in quotes
        pdf_path = pdf_path.strip('"\'')
        
        # Check if file exists
        if not os.path.exists(pdf_path):
            print(f"❌ Error: File '{pdf_path}' not found!")
            continue
            
        # Check if it's a PDF file
        if not pdf_path.lower().endswith('.pdf'):
            print("❌ Error: Please provide a PDF file!")
            continue
            
        print(f"\n📄 Analyzing: {os.path.basename(pdf_path)}")
        print("-" * 50)
        
        # Analyze the PDF
        result = get_pdf_info(pdf_path)
        
        if result is None:
            print("❌ Error: Could not read the PDF file!")
            continue
        elif 'error' in result:
            print(f"❌ Error: {result['error']}")
            continue
            
        # Display results
        total_pages = result['total_pages']
        double_sided_sheets = result['double_sided_sheets']
        dims = result['dimensions']
        
        print(f"📊 Total Pages: {total_pages}")
        print(f"📖 Double-sided printing sheets needed: {double_sided_sheets}")
        
        if total_pages > double_sided_sheets:
            saved_sheets = total_pages - double_sided_sheets
            print(f"💡 You'll save {saved_sheets} sheet{'s' if saved_sheets > 1 else ''} with double-sided printing!")
        
        print(f"\n📏 Page Dimensions:")
        print(f"   • Inches: {format_dimensions(dims['inches'][0], dims['inches'][1], 'in')}")
        print(f"   • Centimeters: {format_dimensions(dims['cm'][0], dims['cm'][1], 'cm')}")
        print(f"   • Points: {format_dimensions(dims['points'][0], dims['points'][1], 'pts')}")
        
        # Additional page size information
        width_in, height_in = dims['inches']
        
        # Common paper sizes for reference
        paper_sizes = {
            'Letter': (8.5, 11.0),
            'A4': (8.27, 11.69),
            'Legal': (8.5, 14.0),
            'A3': (11.69, 16.53),
            'Tabloid': (11.0, 17.0)
        }
        
        # Find closest paper size
        min_diff = float('inf')
        closest_size = None
        
        for size_name, (w, h) in paper_sizes.items():
            # Check both orientations
            diff1 = abs(width_in - w) + abs(height_in - h)
            diff2 = abs(width_in - h) + abs(height_in - w)
            
            if min(diff1, diff2) < min_diff:
                min_diff = min(diff1, diff2)
                closest_size = size_name
                
        if min_diff < 0.5:  # If close enough to a standard size
            orientation = "Portrait" if height_in > width_in else "Landscape"
            print(f"📋 Closest standard size: {closest_size} ({orientation})")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please make sure you have PyPDF2 installed: pip install PyPDF2")