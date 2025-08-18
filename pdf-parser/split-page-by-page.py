import os
import PyPDF2

def split_pdf():
    # Ask user for PDF path
    pdf_path = input("Enter the path of the PDF file: ").strip()
    
    if not os.path.isfile(pdf_path):
        print("Error: File not found.")
        return
    
    # Extract base name (without extension) for folder name
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create output folder
    output_folder = os.path.join("/Volumes/hard-drive/miscellaneous-files/pdf-parser/Books", pdf_name)
    os.makedirs(output_folder, exist_ok=True)
    
    # Open PDF file
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)
        
        for i in range(total_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[i])
            
            output_filename = os.path.join(output_folder, f"chapter {i+1}.pdf")
            with open(output_filename, "wb") as output_file:
                writer.write(output_file)
    
    print(f"PDF successfully split into {total_pages} chapters in: {output_folder}")

if __name__ == "__main__":
    split_pdf()
