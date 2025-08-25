import csv
import requests
import os
from urllib.parse import urlparse
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True  # Fix for truncated images
import concurrent.futures
import queue
import shutil
from datetime import datetime

def download_images_with_gui():
    # Ask for input CSV file
    csv_path = input("Enter the path to the input CSV file (e.g., image_urls.csv): ").strip()
    
    # Ask for output folder
    output_folder = input("Enter the path to the output folder: ").strip()
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    # Create temp folder in the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    temp_dir = os.path.join(script_dir, 'temp_images')
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Read URLs from CSV and check if it has progress columns
    urls_data = []
    has_progress_columns = False
    
    # Check if CSV has existing progress columns
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        
        # Check if progress columns exist
        if header and len(header) >= 5:
            expected_cols = ['url', 'temp_downloaded', 'user_decision', 'temp_path', 'final_path']
            if header[:5] == expected_cols:
                has_progress_columns = True
                print("Found existing progress tracking columns in CSV")
                
                # Load existing data
                for row in reader:
                    if row and row[0].strip():  # Skip empty rows
                        urls_data.append({
                            'url': row[0].strip(),
                            'temp_downloaded': row[1] if len(row) > 1 else 'no',
                            'user_decision': row[2] if len(row) > 2 else 'pending',
                            'temp_path': row[3] if len(row) > 3 else '',
                            'final_path': row[4] if len(row) > 4 else ''
                        })
    
    # If no progress columns, read as simple URL list
    if not has_progress_columns:
        print("No progress tracking found. Creating new tracking structure.")
        with open(csv_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0].strip():  # Skip empty rows
                    urls_data.append({
                        'url': row[0].strip(),
                        'temp_downloaded': 'no',
                        'user_decision': 'pending',
                        'temp_path': '',
                        'final_path': ''
                    })
    
    print(f"Found {len(urls_data)} URLs in the CSV.")
    
    if not urls_data:
        print("No URLs found. Exiting.")
        return
    
    # Create backup of original CSV
    backup_path = csv_path.replace('.csv', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    shutil.copy2(csv_path, backup_path)
    print(f"Created backup: {backup_path}")
    
    def save_progress():
        """Save current progress to CSV"""
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # Write header
            writer.writerow(['url', 'temp_downloaded', 'user_decision', 'temp_path', 'final_path'])
            # Write data
            for data in urls_data:
                writer.writerow([
                    data['url'],
                    data['temp_downloaded'],
                    data['user_decision'],
                    data['temp_path'],
                    data['final_path']
                ])
    
    # Find starting index (first pending item)
    start_index = 0
    for i, data in enumerate(urls_data):
        if data['user_decision'] == 'pending':
            start_index = i
            break
    else:
        print("All images have been processed!")
        return
    
    print(f"Resuming from image {start_index + 1}")
    
    # Set up GUI
    root = tk.Tk()
    root.title("Image Downloader with Progress Tracking")
    root.geometry("800x750")
    root.resizable(False, False)
    
    # Progress label (for URL and index)
    progress_label = tk.Label(root, text="Loading...")
    progress_label.pack(pady=5)
    
    # Status label (for tracking info)
    status_label = tk.Label(root, text="", fg="blue", font=("Arial", 10))
    status_label.pack(pady=2)
    
    # Fixed frame for image to prevent resizing
    image_frame = tk.Frame(root, width=800, height=500, bg="gray")
    image_frame.pack_propagate(False)
    image_frame.pack()
    
    # Image display label inside frame (centered)
    image_label = tk.Label(image_frame)
    image_label.place(relx=0.5, rely=0.5, anchor="center")
    
    # Dimensions box
    dim_frame = tk.Frame(root, bg="lightblue", padx=10, pady=5)
    dim_frame.pack(pady=5)
    dim_label = tk.Label(dim_frame, text="Dimensions: Unknown", font=("Arial", 12), bg="lightblue")
    dim_label.pack()
    
    # Buttons frame
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10, fill=tk.X)
    
    yes_button = tk.Button(button_frame, text="Yes (Download)", command=lambda: handle_decision(True))
    yes_button.pack(side=tk.LEFT, padx=10)
    
    no_button = tk.Button(button_frame, text="No (Skip)", command=lambda: handle_decision(False))
    no_button.pack(side=tk.RIGHT, padx=10)
    
    # Save progress button
    save_button = tk.Button(button_frame, text="Save Progress & Exit", command=lambda: save_and_exit())
    save_button.pack(side=tk.BOTTOM, pady=5)
    
    # Keyboard bindings
    root.bind('<z>', lambda e: handle_decision(True))
    root.bind('<x>', lambda e: handle_decision(False))
    root.bind('<s>', lambda e: save_and_exit())
    
    current_index = start_index
    current_photo = None
    fetch_queue = queue.Queue()
    preloaded = {}
    
    # Thread pool for concurrent downloads
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=15)
    
    def get_temp_filename(index, url):
        """Generate consistent temp filename"""
        parsed_url = urlparse(url)
        ext = os.path.splitext(parsed_url.path)[1] or '.jpg'
        return os.path.join(temp_dir, f"temp_image_{index}{ext}")
    
    def get_final_filename(index, url):
        """Generate final filename"""
        parsed_url = urlparse(url)
        ext = os.path.splitext(parsed_url.path)[1] or '.jpg'
        return os.path.join(output_folder, f"image_{index + 1}{ext}")
    
    def fetch_image_in_thread(url, index):
        try:
            # Check if already exists in temp
            temp_path = get_temp_filename(index, url)
            if os.path.exists(temp_path):
                # Verify it's still a valid image
                try:
                    with Image.open(temp_path) as img:
                        width, height = img.size
                        dimensions = f"{width}x{height}"
                        fetch_queue.put((index, temp_path, dimensions))
                        # Update tracking
                        urls_data[index]['temp_downloaded'] = 'yes'
                        urls_data[index]['temp_path'] = temp_path
                        return
                except:
                    # Invalid cached image, re-download
                    os.remove(temp_path)
            
            response = requests.get(url, stream=True, timeout=10)
            response.raise_for_status()
            
            # Save to temp file
            with open(temp_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Verify it's a valid image and get size
            try:
                with Image.open(temp_path) as img:
                    width, height = img.size
                    if width < 100 or height < 100 or (width <= 64 and height <= 64):
                        os.remove(temp_path)
                        fetch_queue.put((index, None, "Discarded (small image)"))
                        urls_data[index]['temp_downloaded'] = 'discarded'
                    else:
                        dimensions = f"{width}x{height}"
                        fetch_queue.put((index, temp_path, dimensions))
                        # Update tracking
                        urls_data[index]['temp_downloaded'] = 'yes'
                        urls_data[index]['temp_path'] = temp_path
            except Exception as img_error:
                os.remove(temp_path)
                fetch_queue.put((index, None, f"Invalid image: {str(img_error)[:50]}"))
                urls_data[index]['temp_downloaded'] = 'invalid'
        except Exception as e:
            fetch_queue.put((index, None, f"Download error: {str(e)[:50]}"))
            urls_data[index]['temp_downloaded'] = 'error'
    
    def prefetch_images(start_index, count):
        for i in range(start_index, min(start_index + count, len(urls_data))):
            if i not in preloaded and urls_data[i]['user_decision'] == 'pending':
                executor.submit(fetch_image_in_thread, urls_data[i]['url'], i)
    
    def update_gui_from_queue():
        nonlocal current_index
        updated = False
        while not fetch_queue.empty():
            index, temp_path, info = fetch_queue.get()
            preloaded[index] = (temp_path, info)
            updated = True
        
        if current_index in preloaded:
            temp_path, info = preloaded[current_index]
            url_data = urls_data[current_index]
            
            if temp_path is None:
                # Error or discarded
                progress_label.config(text=f"Image {current_index + 1}/{len(urls_data)}: {url_data['url']} ({info})")
                status_label.config(text=f"Status: {url_data['temp_downloaded']} | Decision: {url_data['user_decision']}")
                dim_label.config(text="Dimensions: N/A")
                image_label.config(image=None)
                
                if "Discarded" in info or "Error" in info or "Invalid" in info:
                    del preloaded[current_index]
                    urls_data[current_index]['user_decision'] = 'auto_skipped'
                    current_index = find_next_pending(current_index + 1)
                    show_next_image()
                    return False
                return True
            else:
                # Success
                dimensions = info
                progress_label.config(text=f"Image {current_index + 1}/{len(urls_data)}: {url_data['url']}")
                status_label.config(text=f"Status: temp downloaded | Decision: pending")
                dim_label.config(text=f"Dimensions: {dimensions}")
                
                try:
                    img = Image.open(temp_path)
                    img.thumbnail((800, 500))
                    global current_photo
                    current_photo = ImageTk.PhotoImage(img)
                    image_label.config(image=current_photo)
                    return True
                except Exception as e:
                    print(f"Error opening image {temp_path}: {e}")
                    progress_label.config(text=f"Image {current_index + 1}/{len(urls_data)}: Corrupted image")
                    status_label.config(text="Status: corrupted")
                    dim_label.config(text="Dimensions: N/A")
                    image_label.config(image=None)
                    
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                    del preloaded[current_index]
                    urls_data[current_index]['user_decision'] = 'auto_skipped'
                    urls_data[current_index]['temp_downloaded'] = 'corrupted'
                    current_index = find_next_pending(current_index + 1)
                    show_next_image()
                    return False
        
        return updated
    
    def find_next_pending(start_idx):
        """Find next pending image"""
        for i in range(start_idx, len(urls_data)):
            if urls_data[i]['user_decision'] == 'pending':
                return i
        return len(urls_data)  # All done
    
    def check_queue():
        if update_gui_from_queue():
            pass
        else:
            root.after(100, check_queue)
    
    def show_next_image():
        nonlocal current_index
        if current_index >= len(urls_data):
            print("All images reviewed.")
            save_progress()
            root.quit()
            return
        
        url_data = urls_data[current_index]
        progress_label.config(text=f"Loading image {current_index + 1}/{len(urls_data)}: {url_data['url']}")
        status_label.config(text=f"Status: {url_data['temp_downloaded']} | Decision: {url_data['user_decision']}")
        dim_label.config(text="Dimensions: Fetching...")
        image_label.config(image=None)
        
        # Check if already processed
        if url_data['user_decision'] != 'pending':
            current_index = find_next_pending(current_index + 1)
            show_next_image()
            return
        
        # Prefetch more if needed
        prefetch_images(current_index, 25)
        check_queue()
    
    def handle_decision(download):
        nonlocal current_index
        if current_index in preloaded:
            temp_path, _ = preloaded[current_index]
            url_data = urls_data[current_index]
            
            if temp_path:
                if download:
                    try:
                        # Move to final location
                        final_path = get_final_filename(current_index, url_data['url'])
                        shutil.move(temp_path, final_path)
                        print(f"Downloaded: {url_data['url']} -> {final_path}")
                        
                        # Update tracking
                        urls_data[current_index]['user_decision'] = 'accepted'
                        urls_data[current_index]['final_path'] = final_path
                        
                    except Exception as e:
                        print(f"Failed to save {url_data['url']}: {e}")
                        urls_data[current_index]['user_decision'] = 'save_error'
                else:
                    # User chose to skip
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                    urls_data[current_index]['user_decision'] = 'rejected'
                    urls_data[current_index]['temp_path'] = ''
            else:
                # No temp file (error case)
                urls_data[current_index]['user_decision'] = 'skipped_error'
            
            del preloaded[current_index]
        
        # Save progress periodically (every 10 decisions)
        if (current_index + 1) % 10 == 0:
            save_progress()
            print(f"Progress saved at image {current_index + 1}")
        
        current_index = find_next_pending(current_index + 1)
        show_next_image()
    
    def save_and_exit():
        save_progress()
        print("Progress saved. Exiting...")
        root.quit()
    
    # Handle window close
    def on_closing():
        save_progress()
        print("Progress saved on exit.")
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    # Initial prefetch
    prefetch_images(current_index, 25)
    
    # Start with current image
    show_next_image()
    
    root.mainloop()
    
    # Final cleanup
    executor.shutdown(wait=True)
    save_progress()
    print("Session completed. Progress saved.")

# Run the function
download_images_with_gui()