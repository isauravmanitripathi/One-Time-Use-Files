import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
import fitz  # pymupdf
from PIL import Image, ImageTk
import os
import sys
from io import BytesIO
from datetime import datetime
import re

class PDFEPUBViewer:
    def __init__(self, root, output_folder=None):
        self.root = root
        self.root.title("PDF & EPUB Viewer & Cropper")
        self.root.geometry("800x900")
        
        self.document = None
        self.current_page = 0
        self.total_pages = 0
        self.zoom_level = 1.0
        self.base_zoom = 1.0  # Auto-calculated base zoom for page fitting
        self.output_folder = output_folder
        self.filename = None
        self.file_type = None  # 'pdf' or 'epub'
        
        # Cropping variables
        self.crop_start_page = None
        self.crop_end_page = None
        self.is_cropping = False
        
        # Chapter counter for automatic naming
        self.chapter_counter = 1
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Control frame
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Open file button
        ttk.Button(control_frame, text="Open PDF/EPUB", command=self.open_file).pack(side=tk.LEFT, padx=(0, 10))
        
        # Navigation buttons
        ttk.Button(control_frame, text="Previous (1)", command=self.prev_page).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(control_frame, text="Next (2)", command=self.next_page).pack(side=tk.LEFT, padx=(0, 10))
        
        # Page info label
        self.page_label = ttk.Label(control_frame, text="No file loaded")
        self.page_label.pack(side=tk.LEFT, padx=(0, 10))
        
        # Zoom controls
        ttk.Label(control_frame, text="Zoom:").pack(side=tk.LEFT, padx=(10, 5))
        ttk.Button(control_frame, text="-", command=self.zoom_out).pack(side=tk.LEFT, padx=(0, 2))
        ttk.Button(control_frame, text="Fit", command=self.fit_to_window).pack(side=tk.LEFT, padx=(0, 2))
        ttk.Button(control_frame, text="+", command=self.zoom_in).pack(side=tk.LEFT, padx=(0, 10))
        
        # Output folder button
        ttk.Button(control_frame, text="Set Output Folder", command=self.set_output_folder).pack(side=tk.RIGHT, padx=(10, 0))
        
        # Crop status frame
        crop_frame = ttk.Frame(main_frame)
        crop_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Crop status label
        self.crop_status_label = ttk.Label(crop_frame, text="Keys: 1=Previous, 2=Next, B=Start crop, N=Finish crop, ESC=Cancel crop", 
                                         foreground="blue", font=("Arial", 10, "bold"))
        self.crop_status_label.pack(side=tk.LEFT)
        
        # File type indicator
        self.file_type_label = ttk.Label(crop_frame, text="", 
                                       foreground="purple", font=("Arial", 9, "italic"))
        self.file_type_label.pack(side=tk.RIGHT)
        
        # Chapter counter info frame
        counter_frame = ttk.Frame(main_frame)
        counter_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Chapter counter label
        self.chapter_counter_label = ttk.Label(counter_frame, text=f"Next chapter: Chapter {self.chapter_counter}", 
                                             foreground="darkblue", font=("Arial", 9, "bold"))
        self.chapter_counter_label.pack(side=tk.LEFT)
        
        # Reset counter button
        ttk.Button(counter_frame, text="Reset Counter", command=self.reset_chapter_counter).pack(side=tk.RIGHT, padx=(10, 0))
        
        # Output folder info frame
        folder_frame = ttk.Frame(main_frame)
        folder_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Output folder label
        self.folder_label = ttk.Label(folder_frame, text=f"Output folder: {self.output_folder or 'Not set'}", 
                                    foreground="darkgreen", font=("Arial", 9))
        self.folder_label.pack(side=tk.LEFT)
        
        # Create scrollable frame for document display
        self.canvas_frame = ttk.Frame(main_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas with scrollbars
        self.canvas = tk.Canvas(self.canvas_frame, bg='white')
        v_scrollbar = ttk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        h_scrollbar = ttk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack scrollbars and canvas
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Bind mouse wheel for scrolling
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Configure>", self.on_window_resize)  # Handle window resize
        self.root.focus_set()  # Enable key bindings
        
    def reset_chapter_counter(self):
        """Reset chapter counter to 1"""
        self.chapter_counter = 1
        self.update_chapter_counter_display()
        messagebox.showinfo("Counter Reset", "Chapter counter has been reset to 1.")
    
    def update_chapter_counter_display(self):
        """Update the chapter counter display"""
        self.chapter_counter_label.config(text=f"Next chapter: Chapter {self.chapter_counter}")
    
    def get_next_chapter_number(self):
        """Get the next available chapter number by scanning existing files"""
        if not self.output_folder or not os.path.exists(self.output_folder):
            return self.chapter_counter
        
        # Get all PDF files in the output folder
        existing_files = [f for f in os.listdir(self.output_folder) if f.lower().endswith('.pdf')]
        
        # Extract chapter numbers from existing files
        chapter_numbers = []
        for filename in existing_files:
            # Look for "Chapter X" pattern (case insensitive)
            match = re.search(r'chapter\s*(\d+)', filename, re.IGNORECASE)
            if match:
                chapter_numbers.append(int(match.group(1)))
        
        if not chapter_numbers:
            return self.chapter_counter
        
        # Find the next available chapter number
        chapter_numbers.sort()
        next_number = 1
        for num in chapter_numbers:
            if num == next_number:
                next_number += 1
            elif num > next_number:
                break
        
        return max(next_number, self.chapter_counter)
    
    def calculate_fit_zoom(self):
        """Calculate zoom level to fit page in window"""
        if not self.document:
            return 1.0
            
        try:
            # Get current page dimensions
            page = self.document[self.current_page]
            page_rect = page.rect
            page_width = page_rect.width
            page_height = page_rect.height
            
            # Get canvas dimensions (subtract some padding for scrollbars)
            canvas_width = self.canvas.winfo_width() - 20
            canvas_height = self.canvas.winfo_height() - 20
            
            # Ensure minimum dimensions
            if canvas_width < 100:
                canvas_width = 600
            if canvas_height < 100:
                canvas_height = 700
            
            # Calculate scale factors for width and height
            width_scale = canvas_width / page_width
            height_scale = canvas_height / page_height
            
            # Use the smaller scale factor to ensure page fits completely
            fit_zoom = min(width_scale, height_scale, 3.0)  # Cap at 3x max
            
            # Set minimum zoom to ensure readability
            fit_zoom = max(fit_zoom, 0.3)
            
            return fit_zoom
            
        except Exception as e:
            print(f"Error calculating fit zoom: {e}")
            return 1.0
    
    def fit_to_window(self):
        """Reset zoom to fit page in window"""
        if self.document:
            self.base_zoom = self.calculate_fit_zoom()
            self.zoom_level = self.base_zoom
            self.display_page()
    
    def on_window_resize(self, event):
        """Handle window resize event"""
        # Only respond to canvas resize events, not all widget resize events
        if event.widget == self.root and self.document:
            # Add a small delay to avoid too many rapid recalculations
            self.root.after(100, self.auto_fit_if_needed)
    
    def auto_fit_if_needed(self):
        """Auto-fit page if zoom is at base level"""
        if self.document and abs(self.zoom_level - self.base_zoom) < 0.1:
            self.fit_to_window()
        
    def set_output_folder(self):
        """Let user select output folder"""
        folder = filedialog.askdirectory(title="Select Output Folder for Cropped PDFs")
        if folder:
            self.output_folder = folder
            self.folder_label.config(text=f"Output folder: {self.output_folder}")
            # Update chapter counter based on existing files
            self.chapter_counter = self.get_next_chapter_number()
            self.update_chapter_counter_display()
        
    def open_file(self):
        """Open and load a PDF or EPUB file"""
        file_path = filedialog.askopenfilename(
            title="Select PDF or EPUB file",
            filetypes=[
                ("PDF and EPUB files", "*.pdf;*.epub"),
                ("PDF files", "*.pdf"), 
                ("EPUB files", "*.epub"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.load_file(file_path)
            
    def load_file(self, file_path):
        """Load a PDF or EPUB file from given path"""
        try:
            # Close previous document if any
            if self.document:
                self.document.close()
            
            # Reset cropping variables
            self.crop_start_page = None
            self.crop_end_page = None
            self.is_cropping = False
            self.update_crop_status()
            
            # Determine file type
            file_extension = os.path.splitext(file_path)[1].lower()
            if file_extension == '.pdf':
                self.file_type = 'pdf'
            elif file_extension == '.epub':
                self.file_type = 'epub'
            else:
                messagebox.showerror("Error", "Unsupported file format. Please select a PDF or EPUB file.")
                return
            
            # Open document (PyMuPDF handles both PDF and EPUB)
            self.document = fitz.open(file_path)
            self.total_pages = len(self.document)
            self.current_page = 0
            
            # Store filename for folder creation
            self.filename = os.path.splitext(os.path.basename(file_path))[0]
            
            # Update window title and file type indicator
            filename = os.path.basename(file_path)
            self.root.title(f"PDF & EPUB Viewer & Cropper - {filename}")
            self.file_type_label.config(text=f"File type: {self.file_type.upper()}")
            
            # Create output folder if not set
            if not self.output_folder:
                self.create_default_output_folder()
            
            # Update chapter counter based on existing files in output folder
            self.chapter_counter = self.get_next_chapter_number()
            self.update_chapter_counter_display()
            
            # Calculate initial fit zoom and display first page
            self.root.after(100, self.fit_to_window)  # Small delay to ensure canvas is ready
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")
    
    def create_default_output_folder(self):
        """Create default output folder based on filename"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            folder_name = f"{self.filename}_cropped"
            self.output_folder = os.path.join(script_dir, folder_name)
            
            # Create folder if it doesn't exist
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)
                
            self.folder_label.config(text=f"Output folder: {self.output_folder}")
            print(f"Created output folder: {self.output_folder}")
            
        except Exception as e:
            # Fallback to script directory
            self.output_folder = os.path.dirname(os.path.abspath(__file__))
            self.folder_label.config(text=f"Output folder: {self.output_folder} (fallback)")
            print(f"Warning: Could not create folder, using script directory: {e}")
    
    def display_page(self):
        """Display the current page"""
        if not self.document:
            return
            
        try:
            # Get the current page
            page = self.document[self.current_page]
            
            # Create transformation matrix for zoom
            mat = fitz.Matrix(self.zoom_level, self.zoom_level)
            
            # Render page to image
            pix = page.get_pixmap(matrix=mat)
            img_data = pix.tobytes("ppm")
            
            # Convert to PIL Image and then to PhotoImage
            img = Image.open(BytesIO(img_data))
            self.photo = ImageTk.PhotoImage(img)
            
            # Clear canvas and display image
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            
            # Add visual indicator if this page is marked for cropping
            if self.crop_start_page is not None and self.current_page == self.crop_start_page:
                # Add green border for start page
                self.canvas.create_rectangle(2, 2, img.width-2, img.height-2, 
                                           outline="green", width=4)
                self.canvas.create_text(10, 10, text="START", fill="green", 
                                      font=("Arial", 12, "bold"), anchor="nw")
            
            # Update scroll region
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            
            # Update page label with zoom info and file type
            zoom_percent = int(self.zoom_level * 100)
            page_text = f"Page {self.current_page + 1} of {self.total_pages} ({zoom_percent}%) [{self.file_type.upper()}]"
            if self.is_cropping:
                page_text += f" | Cropping: {self.crop_start_page + 1} to ?"
            self.page_label.config(text=page_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display page: {str(e)}")
    
    def next_page(self):
        """Go to next page"""
        if self.document and self.current_page < self.total_pages - 1:
            self.current_page += 1
            # Auto-fit if we're at base zoom level
            if abs(self.zoom_level - self.base_zoom) < 0.1:
                self.base_zoom = self.calculate_fit_zoom()
                self.zoom_level = self.base_zoom
            self.display_page()
    
    def prev_page(self):
        """Go to previous page"""
        if self.document and self.current_page > 0:
            self.current_page -= 1
            # Auto-fit if we're at base zoom level
            if abs(self.zoom_level - self.base_zoom) < 0.1:
                self.base_zoom = self.calculate_fit_zoom()
                self.zoom_level = self.base_zoom
            self.display_page()
    
    def zoom_in(self):
        """Increase zoom level"""
        if self.document:
            self.zoom_level = min(self.zoom_level * 1.2, 5.0)  # Max zoom 5x
            self.display_page()
    
    def zoom_out(self):
        """Decrease zoom level"""
        if self.document:
            self.zoom_level = max(self.zoom_level / 1.2, 0.2)  # Min zoom 0.2x
            self.display_page()
    
    def cancel_crop(self):
        """Cancel current cropping selection"""
        if not self.is_cropping:
            return
            
        # Reset cropping variables
        self.crop_start_page = None
        self.crop_end_page = None
        self.is_cropping = False
        self.update_crop_status()
        self.display_page()  # Refresh to remove visual indicators
        
        # Show cancellation message
        messagebox.showinfo("Crop Cancelled", "Cropping selection has been cancelled.")
    
    def start_crop(self):
        """Start cropping from current page"""
        if not self.document:
            messagebox.showwarning("Warning", "Please open a PDF or EPUB file first!")
            return
            
        self.crop_start_page = self.current_page
        self.crop_end_page = None
        self.is_cropping = True
        self.update_crop_status()
        self.display_page()  # Refresh to show visual indicator
        
    def finish_crop(self):
        """Finish cropping at current page and save"""
        if not self.is_cropping or self.crop_start_page is None:
            messagebox.showwarning("Warning", "Please start cropping first by pressing 'B'!")
            return
            
        self.crop_end_page = self.current_page
        
        if self.crop_end_page < self.crop_start_page:
            messagebox.showerror("Error", "End page must be after start page!")
            return
        
        # Ask user for filename with automatic chapter naming
        self.ask_filename_and_save()
        
    def ask_filename_and_save(self):
        """Ask user for filename and save the cropped pages as PDF with automatic chapter naming"""
        # Get the next chapter number (ensures proper sequential order)
        next_chapter = self.get_next_chapter_number()
        default_name = f"Chapter {next_chapter}"
        
        while True:
            # Ask user for custom filename with chapter name pre-filled
            custom_name = simpledialog.askstring(
                "Save Cropped PDF",
                f"Enter filename for the cropped PDF:\n(Pages {self.crop_start_page+1} to {self.crop_end_page+1} from {self.file_type.upper()})\n\nPress Enter to use suggested name or modify as needed.\nWill be saved as PDF to:\n{self.output_folder}",
                initialvalue=default_name
            )
            
            if custom_name is None:  # User cancelled
                return
                
            if not custom_name.strip():  # Empty name - use default
                custom_name = default_name
                
            # Clean the filename (remove invalid characters)
            invalid_chars = '<>:"/\\|?*'
            for char in invalid_chars:
                custom_name = custom_name.replace(char, '_')
            
            # Add .pdf extension if not present
            if not custom_name.lower().endswith('.pdf'):
                custom_name += '.pdf'
            
            # Check if file already exists
            output_path = os.path.join(self.output_folder, custom_name)
            if os.path.exists(output_path):
                # Show error and ask for different name
                messagebox.showerror(
                    "File Already Exists", 
                    f"A file named '{custom_name}' already exists in the output folder.\n\nPlease choose a different filename."
                )
                # Set the existing name as default for next attempt, so user can modify it
                default_name = custom_name.replace('.pdf', '') if custom_name.endswith('.pdf') else custom_name
                continue
            else:
                # File doesn't exist, proceed with saving
                self.save_cropped_pdf(custom_name)
                # Update chapter counter for next use
                self.chapter_counter = self.get_next_chapter_number()
                self.update_chapter_counter_display()
                break
        
    def save_cropped_pdf(self, filename):
        """Save the selected pages as a new PDF with custom filename"""
        try:
            # Create new PDF document
            new_pdf = fitz.open()
            
            # Copy selected pages (this works for both PDF and EPUB)
            for page_num in range(self.crop_start_page, self.crop_end_page + 1):
                new_pdf.insert_pdf(self.document, from_page=page_num, to_page=page_num)
            
            # Use the set output folder
            output_path = os.path.join(self.output_folder, filename)
            
            # Save the new PDF
            new_pdf.save(output_path)
            new_pdf.close()
            
            # Show success message
            source_type = self.file_type.upper()
            messagebox.showinfo("Success", 
                              f"Cropped PDF saved successfully!\n\n"
                              f"Source: {source_type} file\n"
                              f"Pages {self.crop_start_page+1} to {self.crop_end_page+1}\n"
                              f"Saved as: {filename}\n"
                              f"Location: {self.output_folder}")
            
            # Reset cropping variables
            self.crop_start_page = None
            self.crop_end_page = None
            self.is_cropping = False
            self.update_crop_status()
            self.display_page()  # Refresh display
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save cropped PDF: {str(e)}")
    
    def update_crop_status(self):
        """Update the crop status label"""
        if not self.is_cropping:
            self.crop_status_label.config(text="Keys: 1=Previous, 2=Next, B=Start crop, N=Finish crop, ESC=Cancel crop", 
                                        foreground="blue")
        else:
            self.crop_status_label.config(text=f"Cropping started at page {self.crop_start_page+1}. Use 1/2 to navigate, press 'N' to finish or ESC to cancel.", 
                                        foreground="red")
    
    def on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    def on_key_press(self, event):
        """Handle keyboard shortcuts"""
        # Navigation with number keys
        if event.keysym == "1":
            self.prev_page()
        elif event.keysym == "2":
            self.next_page()
        # Keep old navigation for compatibility
        elif event.keysym == "Right" or event.keysym == "space":
            self.next_page()
        elif event.keysym == "Left":
            self.prev_page()
        # Zoom controls
        elif event.keysym == "plus" or event.keysym == "equal":
            self.zoom_in()
        elif event.keysym == "minus":
            self.zoom_out()
        elif event.keysym.lower() == "f":
            self.fit_to_window()
        # Cropping controls
        elif event.keysym.lower() == "b":
            self.start_crop()
        elif event.keysym.lower() == "n":
            self.finish_crop()
        elif event.keysym == "Escape":
            self.cancel_crop()

def get_user_choice():
    """Ask user how they want to provide the file path"""
    print("PDF & EPUB Viewer & Cropper")
    print("=" * 30)
    print("How would you like to provide the PDF or EPUB file?")
    print("1. Type the file path in terminal")
    print("2. Browse and select file")
    
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            return int(choice)
        print("Please enter 1 or 2")

def get_file_path_from_terminal():
    """Get file path from user input"""
    while True:
        file_path = input("\nEnter the full path to your PDF or EPUB file: ").strip().strip('"')
        
        if os.path.exists(file_path):
            file_ext = file_path.lower()
            if file_ext.endswith('.pdf') or file_ext.endswith('.epub'):
                return file_path
            else:
                print("Error: File must be a PDF or EPUB file!")
        else:
            print("Error: File not found!")
        
        retry = input("Try again? (y/n): ").strip().lower()
        if retry != 'y':
            return None

def get_file_path_from_dialog():
    """Get file path using file dialog"""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    file_path = filedialog.askopenfilename(
        title="Select PDF or EPUB file to open",
        filetypes=[
            ("PDF and EPUB files", "*.pdf;*.epub"),
            ("PDF files", "*.pdf"), 
            ("EPUB files", "*.epub"),
            ("All files", "*.*")
        ]
    )
    
    root.destroy()
    return file_path if file_path else None

def get_output_folder():
    """Ask user for output folder"""
    print("\nOutput folder options:")
    print("1. Select a custom output folder")
    print("2. Auto-create folder (based on file name)")
    
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == '1':
            root = tk.Tk()
            root.withdraw()
            folder = filedialog.askdirectory(title="Select Output Folder for Cropped PDFs")
            root.destroy()
            return folder if folder else None
        elif choice == '2':
            return None  # Will auto-create
        print("Please enter 1 or 2")

def main():
    print("PDF & EPUB Viewer & Cropper Starting...")
    
    # Get user choice for file input method
    choice = get_user_choice()
    
    # Get file path based on user choice
    if choice == 1:
        file_path = get_file_path_from_terminal()
    else:
        file_path = get_file_path_from_dialog()
    
    if not file_path:
        print("No file selected. Exiting...")
        return
    
    # Get output folder choice
    output_folder = get_output_folder()
    
    # Create and start the GUI
    root = tk.Tk()
    viewer = PDFEPUBViewer(root, output_folder)
    
    # Load the selected file
    viewer.load_file(file_path)
    
    print(f"\nFile loaded: {os.path.basename(file_path)}")
    print(f"Output folder: {viewer.output_folder}")
    print("\nGUI started. Use the application window for navigation and cropping.")
    print("Features:")
    print("- Supports both PDF and EPUB files")
    print("- Auto-fit pages to window size")
    print("- 'Fit' button to manually fit page")
    print("- Press 'F' key for quick fit")
    print("- Automatic chapter naming in sequential order")
    print("- Cropped pages always saved as PDF")
    print("- Better duplicate filename handling")
    print("- Reset counter button for starting over")
    
    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()