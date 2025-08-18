import os
import re

def clean_filename(filename: str) -> str:
    # Remove extension for processing
    name, ext = os.path.splitext(filename)
    
    # Remove (Z-Library)
    name = name.replace("(Z-Library)", "")
    
    # Remove other unwanted characters and replace with underscore
    name = re.sub(r"[\"\'\+\(\),]", "", name)   # remove specific special characters
    name = re.sub(r"\s+", "_", name)            # replace spaces with underscores
    name = re.sub(r"_+", "_", name)             # collapse multiple underscores
    
    # Strip leading/trailing underscores
    name = name.strip("_")
    
    return f"{name}{ext}"

def rename_pdfs_in_folder(folder_path: str):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            old_path = os.path.join(folder_path, filename)
            new_filename = clean_filename(filename)
            new_path = os.path.join(folder_path, new_filename)
            
            if old_path != new_path:
                print(f"Renaming: {filename} -> {new_filename}")
                os.rename(old_path, new_path)

if __name__ == "__main__":
    folder = input("Enter the path to your folder containing PDF files: ").strip()
    rename_pdfs_in_folder(folder)
