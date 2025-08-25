import csv
import requests
import os
from urllib.parse import urlparse
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk
import concurrent.futures
import queue
import shutil

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
    root.geometry("800x700")  # Fixed larger window
    root.resizable(False, False)  # Disable resizing to keep buttons fixed
    
    # Progress label (for URL and index)
    progress_label = tk.Label(root, text="Loading first image...")
    progress_label.pack(pady=10)
    
    # Fixed frame for image to prevent resizing
    image_frame = tk.Frame(root, width=800, height=500, bg="gray")
    image_frame.pack_propagate(False)  # Prevent frame from shrinking
    image_frame.pack()
    
    # Image display label inside frame (centered)
    image_label = tk.Label(image_frame)
    image_label.place(relx=0.5, rely=0.5, anchor="center")
    
    # Dimensions box (colored frame with label)
    dim_frame = tk.Frame(root, bg="lightblue", padx=10, pady=5)
    dim_frame.pack(pady=5)
    dim_label = tk.Label(dim_frame, text="Dimensions: Unknown", font=("Arial", 12), bg="lightblue")
    dim_label.pack()
    
    # Buttons frame (fixed at bottom)
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10, fill=tk.X)
    
    yes_button = tk.Button(button_frame, text="Yes (Download)", command=lambda: handle_decision(True))
    yes_button.pack(side=tk.LEFT, padx=10)
    
    no_button = tk.Button(button_frame, text="No (Skip)", command=lambda: handle_decision(False))
    no_button.pack(side=tk.RIGHT, padx=10)
    
    # Keyboard bindings
    root.bind('<z>', lambda e: handle_decision(True))
    root.bind('<x>', lambda e: handle_decision(False))
    
    current_index = 0
    current_photo = None  # To keep reference
    fetch_queue = queue.Queue()  # Changed to regular Queue for FIFO, as priority might not be needed if prefetch is controlled
    preloaded = {}  # Store preloaded results by index
    
    # Create temp folder in the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    temp_dir = os.path.join(script_dir, 'temp_images')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Thread pool for concurrent downloads
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)  # Reduced workers to avoid overload
    
    def fetch_image_in_thread(url, index):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            # Save to temp file
            parsed_url = urlparse(url)
            ext = os.path.splitext(parsed_url.path)[1] or '.jpg'
            temp_path = os.path.join(temp_dir, f"temp_image_{index}{ext}")
            
            with open(temp_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Open to get size
            with Image.open(temp_path) as img:
                width, height = img.size
                if width < 100 or height < 100 or (width <= 64 and height <= 64):
                    os.remove(temp_path)
                    fetch_queue.put((index, None, "Discarded (small image)"))  # Signal discard
                else:
                    dimensions = f"{width}x{height}"
                    fetch_queue.put((index, temp_path, dimensions))
        except Exception as e:
            fetch_queue.put((index, None, str(e)))
    
    def prefetch_images(start_index, count):
        for i in range(start_index, min(start_index + count, len(urls))):
            executor.submit(fetch_image_in_thread, urls[i], i)
    
    def update_gui_from_queue():
        while not fetch_queue.empty():
            index, temp_path, info = fetch_queue.get()
            preloaded[index] = (temp_path, info)
        
        if current_index in preloaded:
            temp_path, info = preloaded[current_index]
            if temp_path is None:
                # Error or discarded
                progress_label.config(text=f"Image {current_index + 1}/{len(urls)}: {urls[current_index]} ({info})")
                dim_label.config(text="Dimensions: N/A")
                image_label.config(image=None)
                # Auto-skip if discarded
                if "Discarded" in info:
                    handle_decision(False)  # Skip automatically
                return True  # Ready
            else:
                # Success
                dimensions = info
                progress_label.config(text=f"Image {current_index + 1}/{len(urls)}: {urls[current_index]}")
                dim_label.config(text=f"Dimensions: {dimensions}")
                
                # Load preview from temp file
                img = Image.open(temp_path)
                img.thumbnail((800, 500))
                global current_photo
                current_photo = ImageTk.PhotoImage(img)
                image_label.config(image=current_photo)
                return True  # Ready
        
        return False  # Not ready yet
    
    def check_queue():
        if update_gui_from_queue():
            # Ready, stop checking until next image
            pass
        else:
            root.after(100, check_queue)  # Check again if not ready
    
    def show_next_image():
        nonlocal current_index
        if current_index >= len(urls):
            print("All images reviewed.")
            root.quit()
            return
        
        url = urls[current_index]
        progress_label.config(text=f"Waiting for image {current_index + 1}/{len(urls)}: {url}")
        dim_label.config(text="Dimensions: Fetching...")
        image_label.config(image=None)
        
        # Prefetch more if needed
        prefetch_images(current_index, 10)  # Fetch current and next 9
        
        # Start checking queue
        check_queue()
    
    def handle_decision(download):
        nonlocal current_index
        if current_index in preloaded:
            temp_path, _ = preloaded[current_index]
            if temp_path:
                if download:
                    try:
                        # Move to output
                        parsed_url = urlparse(urls[current_index])
                        ext = os.path.splitext(parsed_url.path)[1] or '.jpg'
                        filename = f"image_{current_index + 1}{ext}"
                        file_path = os.path.join(output_folder, filename)
                        shutil.move(temp_path, file_path)
                        print(f"Downloaded: {urls[current_index]} -> {file_path}")
                    except Exception as e:
                        print(f"Failed to save {urls[current_index]}: {e}")
                else:
                    os.remove(temp_path)  # Delete if skip
            del preloaded[current_index]  # Clean up
        
        current_index += 1
        show_next_image()
    
    # Initial prefetch
    prefetch_images(0, 10)  # Start with first 10
    
    # Start with first image
    show_next_image()
    
    root.mainloop()
    
    # Shutdown executor
    executor.shutdown(wait=True)
    
    # Cleanup temp dir (remove remaining files and folder)
    for file in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, file))
    os.rmdir(temp_dir)

# Run the function
download_images_with_gui()