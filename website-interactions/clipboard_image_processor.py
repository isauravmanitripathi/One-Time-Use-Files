import os
import csv
import time
import hashlib
import requests
from urllib.parse import urlparse
from PIL import Image, ImageDraw
import pyperclip
import threading
import random
import string
import argparse
from pathlib import Path

class ClipboardImageProcessor:
    def __init__(self, output_folder=None):
        # Set up paths
        if output_folder:
            self.processed_folder = Path(output_folder)
        else:
            self.processed_folder = Path("processed_images")
        
        # CSV file is always created where the script lives
        self.csv_file = "downloaded_links.csv"
        self.youtube_size = (1280, 720)  # Standard YouTube thumbnail size
        
        # Create temp download folder for original images
        self.temp_folder = Path("temp_downloads")
        
        # Create directories if they don't exist
        self.processed_folder.mkdir(exist_ok=True, parents=True)
        self.temp_folder.mkdir(exist_ok=True)
        
        # Initialize CSV file
        self.init_csv()
        
        # Load existing URLs to avoid duplicates
        self.downloaded_urls = self.load_downloaded_urls()
        
        # Track last clipboard content to avoid processing same content multiple times
        self.last_clipboard = ""
        
        print(f"📁 Processed images folder: {self.processed_folder}")
        print(f"📊 CSV file: {self.csv_file}")
        print(f"🖼️  Processing size: {self.youtube_size}")
        print("🚀 Starting clipboard monitor...")
    
    def generate_unique_id(self):
        """Generate a random 6-character unique ID"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    
    def init_csv(self):
        """Initialize CSV file with headers if it doesn't exist"""
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['unique_id', 'url', 'processed_filename', 'timestamp', 'status'])
    
    def load_downloaded_urls(self):
        """Load previously downloaded URLs from CSV"""
        urls = set()
        if os.path.exists(self.csv_file):
            try:
                with open(self.csv_file, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row['status'] == 'success':
                            urls.add(row['url'])
            except Exception as e:
                print(f"⚠️  Error loading CSV: {e}")
        return urls
    
    def is_image_url(self, url):
        """Check if URL points to an image"""
        try:
            # Check file extension
            parsed_url = urlparse(url)
            path = parsed_url.path.lower()
            image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')
            
            if any(path.endswith(ext) for ext in image_extensions):
                return True
            
            # Check content-type header
            response = requests.head(url, timeout=10, allow_redirects=True)
            content_type = response.headers.get('content-type', '').lower()
            return content_type.startswith('image/')
            
        except Exception:
            return False
    
    def generate_filename(self, url):
        """Generate a safe filename from URL for temporary storage"""
        # Use URL hash to create unique filename
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        
        # Try to get original extension
        parsed_url = urlparse(url)
        path = parsed_url.path
        if '.' in path:
            ext = path.split('.')[-1].lower()
            if ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'tiff']:
                return f"temp_{url_hash}.{ext}"
        
        return f"temp_{url_hash}.jpg"
    
    def download_image(self, url):
        """Download image from URL to temporary folder"""
        try:
            print(f"⬇️  Downloading: {url}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=30, stream=True)
            response.raise_for_status()
            
            filename = self.generate_filename(url)
            filepath = self.temp_folder / filename
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✅ Downloaded: {filename}")
            return str(filepath)
            
        except Exception as e:
            print(f"❌ Download failed: {e}")
            return None
    
    def process_image(self, image_path, unique_id):
        """
        Process image with smart sizing:
        - If image is smaller than canvas: increase by 20% (stretch on all sides)
        - If image is larger than canvas: leave 20% gap from all sides
        """
        try:
            with Image.open(image_path) as img:
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Get dimensions
                img_width, img_height = img.size
                canvas_width, canvas_height = self.youtube_size
                
                # Check if image is smaller or larger than canvas
                img_area = img_width * img_height
                canvas_area = canvas_width * canvas_height
                
                if img_area < canvas_area:
                    # Image is smaller - increase by 20% (stretch on all sides)
                    print(f"📏 Small image detected - stretching by 20%")
                    
                    # Calculate new size with 20% increase
                    new_width = int(img_width * 1.2)
                    new_height = int(img_height * 1.2)
                    
                    # Make sure it doesn't exceed canvas size
                    if new_width > canvas_width or new_height > canvas_height:
                        # If 20% stretch would exceed canvas, fit to canvas instead
                        scale_w = canvas_width / img_width
                        scale_h = canvas_height / img_height
                        scale = min(scale_w, scale_h)
                        new_width = int(img_width * scale)
                        new_height = int(img_height * scale)
                    
                    img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    
                else:
                    # Image is larger - leave 20% gap from all sides
                    print(f"📏 Large image detected - leaving 20% gap")
                    
                    # Calculate target size with 20% margins (80% of canvas)
                    target_width = int(canvas_width * 0.8)
                    target_height = int(canvas_height * 0.8)
                    
                    # Scale to fit within the 80% area
                    scale_w = target_width / img_width
                    scale_h = target_height / img_height
                    scale = min(scale_w, scale_h)
                    
                    new_width = int(img_width * scale)
                    new_height = int(img_height * scale)
                    
                    img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Create gray canvas
                canvas = Image.new('RGB', self.youtube_size, color=(128, 128, 128))
                
                # Calculate position to center the image
                x = (canvas_width - new_width) // 2
                y = (canvas_height - new_height) // 2
                
                # Paste image onto canvas
                canvas.paste(img_resized, (x, y))
                
                # Generate processed filename with unique ID
                processed_filename = f"{unique_id}.jpg"
                processed_path = self.processed_folder / processed_filename
                
                # Save processed image
                canvas.save(processed_path, 'JPEG', quality=95)
                
                print(f"🎨 Processed: {processed_filename} (Final size: {new_width}x{new_height})")
                
                # Clean up temporary file
                try:
                    os.remove(image_path)
                    print(f"🗑️  Cleaned temp file: {Path(image_path).name}")
                except:
                    pass
                
                return str(processed_path)
                
        except Exception as e:
            print(f"❌ Processing failed: {e}")
            return None
    
    def log_to_csv(self, unique_id, url, processed_filename=None, status="failed"):
        """Log download attempt to CSV"""
        try:
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([unique_id, url, processed_filename or '', timestamp, status])
        except Exception as e:
            print(f"⚠️  CSV logging error: {e}")
    
    def process_url(self, url):
        """Process a single URL"""
        url = url.strip()
        
        if not url or not url.startswith(('http://', 'https://')):
            return
        
        if url in self.downloaded_urls:
            print(f"⏭️  Skipping already downloaded: {url}")
            return
        
        if not self.is_image_url(url):
            print(f"⏭️  Not an image URL: {url}")
            return
        
        # Generate unique ID for this image
        unique_id = self.generate_unique_id()
        
        # Download image
        downloaded_path = self.download_image(url)
        if not downloaded_path:
            self.log_to_csv(unique_id, url, status="download_failed")
            return
        
        # Process image with unique ID
        processed_path = self.process_image(downloaded_path, unique_id)
        if not processed_path:
            self.log_to_csv(unique_id, url, status="processing_failed")
            return
        
        # Log success
        self.log_to_csv(
            unique_id,
            url, 
            Path(processed_path).name, 
            "success"
        )
        
        # Add to downloaded URLs set
        self.downloaded_urls.add(url)
        
        print(f"🎉 Successfully processed: {url} -> {unique_id}.jpg")
    
    def monitor_clipboard(self):
        """Monitor clipboard for new URLs"""
        print("👁️  Monitoring clipboard... (Press Ctrl+C to stop)")
        
        try:
            while True:
                try:
                    # Get current clipboard content
                    current_clipboard = pyperclip.paste()
                    
                    # Check if clipboard content has changed
                    if current_clipboard != self.last_clipboard:
                        self.last_clipboard = current_clipboard
                        
                        # Process URLs (handle multiple URLs separated by newlines)
                        lines = current_clipboard.split('\n')
                        for line in lines:
                            line = line.strip()
                            if line and (line.startswith('http://') or line.startswith('https://')):
                                # Process in background thread to avoid blocking clipboard monitoring
                                thread = threading.Thread(target=self.process_url, args=(line,))
                                thread.daemon = True
                                thread.start()
                    
                    time.sleep(1)  # Check clipboard every second
                    
                except Exception as e:
                    print(f"⚠️  Clipboard error: {e}")
                    time.sleep(2)
                    
        except KeyboardInterrupt:
            print("\n👋 Stopping clipboard monitor...")

def main():
    parser = argparse.ArgumentParser(description='Monitor clipboard for image URLs and process them')
    parser.add_argument('--output-folder', '-o', type=str, 
                       help='Path to folder where processed images will be stored (default: processed_images)')
    
    args = parser.parse_args()
    
    processor = ClipboardImageProcessor(args.output_folder)
    processor.monitor_clipboard()

if __name__ == "__main__":
    main()