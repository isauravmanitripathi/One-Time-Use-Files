import os
from PIL import Image
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

def convert_pdf_to_markdown(pdf_path, output_path):
    # Create the model dictionary
    artifact_dict = create_model_dict()
    
    # Initialize the converter
    converter = PdfConverter(artifact_dict=artifact_dict)
    
    # Convert the PDF
    rendered = converter(pdf_path)
    
    # Extract the markdown text
    markdown_text, _, images = text_from_rendered(rendered)
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    # Save the markdown to the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_text)
    
    # Optionally, handle images (save them in the same directory as output)
    for img_name, img_data in images.items():
        img_path = os.path.join(output_dir, img_name)
        img_data.save(img_path)
    
    print(f"Conversion complete. Markdown saved to: {output_path}")
    if images:
        print(f"Images saved to: {output_dir}")

if __name__ == "__main__":
    # Ask for input paths
    pdf_path = input("Enter the path to the PDF file: ").strip()
    while not pdf_path or not os.path.exists(pdf_path):
        if not pdf_path:
            print("Error: PDF path cannot be empty.")
        else:
            print("Error: PDF file does not exist.")
        pdf_path = input("Enter the path to the PDF file: ").strip()
    
    output_path = input("Enter the path for the output Markdown file (e.g., output.md): ").strip()
    if not output_path:
        # Default to the same name as PDF but with .md extension in the current directory
        pdf_filename = os.path.basename(pdf_path)
        output_filename = os.path.splitext(pdf_filename)[0] + ".md"
        output_path = os.path.join(os.getcwd(), output_filename)
        print(f"No output path provided. Using default: {output_path}")
    
    convert_pdf_to_markdown(pdf_path, output_path)