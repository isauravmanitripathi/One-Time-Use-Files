import csv
import requests
import os
from urllib.parse import urlparse
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk

def download_images_with_gui():
    # Ask for input CSV file
    csv_path = input("Enter the path to the input CSV file (e.g., image_urls.csv): ").strip()
    
    # Ask for output folder
    output_folder = input("Enter the path to the output folder: ").strip()
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    # Read URLs from CSV
    urls = []
    with open(csv_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0].strip():  # Skip empty rows
                urls.append(row[0].strip())
    
    print(f"Found {len(urls)} URLs in the CSV.")
    
    if not urls:
        print("No URLs found. Exiting.")
        return
    
    # Set up GUI
    root = tk.Tk()
    root.title("Image Downloader")
    root.geometry("800x600")
    
    # Progress label
    progress_label = tk.Label(root, text="Loading first image...")
    progress_label.pack(pady=10)
    
    # Image display label
    image_label = tk.Label(root)
    image_label.pack(expand=True)
    
    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    
    yes_button = tk.Button(button_frame, text="Yes (Download)", command=lambda: handle_decision(True))
    yes_button.pack(side=tk.LEFT, padx=10)
    
    no_button = tk.Button(button_frame, text="No (Skip)", command=lambda: handle_decision(False))
    no_button.pack(side=tk.RIGHT, padx=10)
    
    # Keyboard bindings
    root.bind('<z>', lambda e: handle_decision(True))
    root.bind('<x>', lambda e: handle_decision(False))
    
    current_index = 0
    current_photo = None  # To keep reference
    
    def show_next_image():
        nonlocal current_index, current_photo
        if current_index >= len(urls):
            print("All images reviewed.")
            root.quit()
            return
        
        url = urls[current_index]
        progress_label.config(text=f"Image {current_index + 1}/{len(urls)}: {url}")
        
        try:
            # Fetch image for preview
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Open and resize for display
            img = Image.open(BytesIO(response.content))
            img.thumbnail((800, 600))  # Resize to fit window
            current_photo = ImageTk.PhotoImage(img)
            image_label.config(image=current_photo)
        except Exception as e:
            print(f"Failed to load preview for {url}: {e}")
            image_label.config(image=None)
            progress_label.config(text=f"Error loading {url}. Use keys/buttons to decide.")
    
    def handle_decision(download):
        nonlocal current_index
        url = urls[current_index]
        
        if download:
            try:
                # Download full image
                parsed_url = urlparse(url)
                ext = os.path.splitext(parsed_url.path)[1] or '.jpg'
                filename = f"image_{current_index + 1}{ext}"
                file_path = os.path.join(output_folder, filename)
                
                response = requests.get(url, stream=True)
                response.raise_for_status()
                
                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                print(f"Downloaded: {url} -> {file_path}")
            except Exception as e:
                print(f"Failed to download {url}: {e}")
        
        current_index += 1
        show_next_image()
    
    # Start with first image
    show_next_image()
    
    root.mainloop()

# Run the function
download_images_with_gui()