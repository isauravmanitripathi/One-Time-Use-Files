#!/usr/bin/env python3
"""
Local Marker PDF Parser CLI Tool - Complete Version
Processes PDFs using your self-hosted Marker server

Usage: 
  python complete_local_marker_cli.py <pdf_path>                    # Process single PDF
  python complete_local_marker_cli.py --folder <folder_path>        # Process folder of PDFs
  python complete_local_marker_cli.py --folder <folder_path> --auto # Process folder automatically
  python complete_local_marker_cli.py --folder <folder_path> --all  # Download complete folders with images
"""

import os
import sys
import time
import json
import argparse
import requests
from pathlib import Path
import glob

class LocalMarkerParser:
    def __init__(self, server_url="https://bfveyzbbejjao9-8888.proxy.runpod.net/"):
        self.server_url = server_url.rstrip('/')
        self.upload_url = f"{self.server_url}/upload"
        self.status_url = f"{self.server_url}/status"
        self.download_url = f"{self.server_url}/download"
    
    def parse_pdf(self, pdf_path, output_format="markdown", use_ocr=False, download_all=False):
        """
        Parse a PDF file using your local Marker server
        
        Args:
            pdf_path (str): Path to the PDF file
            output_format (str): Output format ("markdown" or "json")
            use_ocr (bool): Force OCR on all pages
            download_all (bool): Download complete folder with images as ZIP
        """
        
        # Validate PDF file
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        if pdf_path.suffix.lower() != '.pdf':
            raise ValueError("File must be a PDF")
        
        print(f"📄 Processing PDF: {pdf_path.name}")
        print(f"📁 Location: {pdf_path.parent}")
        print(f"📊 Size: {pdf_path.stat().st_size / 1024 / 1024:.1f} MB")
        print(f"🔧 Output format: {output_format}")
        print(f"👁️  Force OCR: {'Yes' if use_ocr else 'No'}")
        print(f"📦 Download all: {'Yes (organized folder)' if download_all else 'No (single file)'}")
        print("-" * 50)
        
        try:
            # Step 1: Upload PDF
            print("🚀 Uploading PDF to server...")
            job_id = self._upload_pdf(pdf_path, output_format, use_ocr)
            
            if not job_id:
                raise Exception("Failed to upload PDF - no job ID received")
            
            print(f"✅ Upload successful! Job ID: {job_id}")
            
            # Step 2: Wait for processing
            print("⏳ Waiting for processing to complete...")
            if not self._wait_for_completion(job_id):
                raise Exception("Processing failed or timed out")
            
            # Step 3: Download result
            if download_all:
                print("📥 Downloading and organizing complete folder...")
                output_file = self._download_folder(job_id, pdf_path)
            else:
                print(f"📥 Downloading {output_format} file...")
                output_file = self._download_result(job_id, pdf_path, output_format)
            
            if output_file:
                print(f"✅ Successfully saved: {output_file}")
                return output_file
            else:
                raise Exception("Failed to download result")
                
        except Exception as e:
            print(f"❌ Error processing {pdf_path.name}: {e}")
            raise
    
    def _upload_pdf(self, pdf_path, output_format, use_ocr):
        """Upload PDF to server and get job ID"""
        try:
            with open(pdf_path, 'rb') as f:
                files = {'file': (pdf_path.name, f, 'application/pdf')}
                data = {
                    'format': output_format,
                    'ocr': str(use_ocr).lower()
                }
                
                response = requests.post(self.upload_url, files=files, data=data, timeout=60)
                
                if response.status_code == 200:
                    result = response.json()
                    return result.get('job_id')
                else:
                    print(f"❌ Upload failed: HTTP {response.status_code}")
                    print(f"Response: {response.text}")
                    return None
                    
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error during upload: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error during upload: {e}")
            return None
    
    def _wait_for_completion(self, job_id, max_wait_time=1800):  # 30 minutes max
        """Wait for job to complete, polling every few seconds"""
        start_time = time.time()
        poll_interval = 5  # seconds
        last_status = None
        
        while True:
            try:
                # Check status
                response = requests.get(f"{self.status_url}/{job_id}", timeout=30)
                
                if response.status_code == 200:
                    status_data = response.json()
                    current_status = status_data.get('status')
                    
                    # Only print status updates when they change
                    if current_status != last_status:
                        if current_status == 'queued':
                            queue_pos = status_data.get('queue_position', 'Unknown')
                            print(f"⏸️  Status: Queued (position: {queue_pos})")
                        elif current_status == 'processing':
                            print(f"🔄 Status: Processing...")
                        elif current_status == 'completed':
                            pages = status_data.get('pages_processed', 'Unknown')
                            processing_time = status_data.get('processing_time_seconds', 'Unknown')
                            print(f"✅ Status: Completed! ({pages} pages, {processing_time}s)")
                            return True
                        elif current_status == 'failed':
                            error_msg = status_data.get('error_message', 'Unknown error')
                            print(f"❌ Status: Failed - {error_msg}")
                            return False
                        
                        last_status = current_status
                    
                    # Show progress every 30 seconds for long jobs
                    elapsed = time.time() - start_time
                    if elapsed % 30 < poll_interval and current_status == 'processing':
                        print(f"🔄 Still processing... ({int(elapsed)}s elapsed)")
                
                elif response.status_code == 404:
                    print(f"❌ Job {job_id} not found")
                    return False
                else:
                    print(f"❌ Status check failed: HTTP {response.status_code}")
                
                # Check timeout
                if time.time() - start_time > max_wait_time:
                    print(f"⏰ Timeout: Processing took longer than {max_wait_time/60:.1f} minutes")
                    return False
                
                time.sleep(poll_interval)
                
            except requests.exceptions.RequestException as e:
                print(f"⚠️  Network error checking status: {e}")
                time.sleep(poll_interval * 2)  # Wait longer on network errors
                continue
            except KeyboardInterrupt:
                print(f"\n❌ Process interrupted by user")
                return False
            except Exception as e:
                print(f"⚠️  Unexpected error checking status: {e}")
                time.sleep(poll_interval)
                continue
    
    def _download_folder(self, job_id, original_pdf_path):
        """Download the complete folder as ZIP and extract to folder with same name as PDF"""
        try:
            # Download the complete folder as ZIP
            download_response = requests.get(
                f"{self.download_url}/{job_id}/folder", 
                timeout=120
            )
            
            if download_response.status_code == 200:
                # Create folder with same name as PDF
                pdf_stem = original_pdf_path.stem
                output_folder = original_pdf_path.parent / pdf_stem
                
                # If folder already exists, add number
                counter = 1
                while output_folder.exists():
                    output_folder = original_pdf_path.parent / f"{pdf_stem}_{counter}"
                    counter += 1
                
                # Create the output folder
                output_folder.mkdir(exist_ok=True)
                print(f"📁 Created folder: {output_folder}")
                
                # Save ZIP temporarily
                import tempfile
                import zipfile
                
                temp_zip = tempfile.NamedTemporaryFile(delete=False, suffix='.zip')
                with open(temp_zip.name, 'wb') as f:
                    f.write(download_response.content)
                
                # Extract ZIP contents to the folder
                extracted_files = []
                with zipfile.ZipFile(temp_zip.name, 'r') as zip_ref:
                    for file_info in zip_ref.filelist:
                        if not file_info.is_dir():
                            # Extract file
                            zip_ref.extract(file_info, output_folder)
                            extracted_file = output_folder / file_info.filename
                            extracted_files.append(extracted_file)
                            
                            # Show what was extracted
                            file_size = extracted_file.stat().st_size / 1024  # KB
                            if extracted_file.suffix == '.md':
                                print(f"   📄 Extracted: {file_info.filename} ({file_size:.1f} KB)")
                            elif extracted_file.suffix == '.json':
                                print(f"   🗂️  Extracted: {file_info.filename} ({file_size:.1f} KB)")
                            elif extracted_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                                print(f"   🖼️  Extracted: {file_info.filename} ({file_size:.1f} KB)")
                            else:
                                print(f"   📎 Extracted: {file_info.filename} ({file_size:.1f} KB)")
                
                # Clean up temporary ZIP file
                import os
                os.unlink(temp_zip.name)
                
                # Show summary
                total_size = sum(f.stat().st_size for f in extracted_files if f.exists()) / 1024  # KB
                print(f"✅ Extracted {len(extracted_files)} files to folder: {output_folder}")
                print(f"📊 Total size: {total_size:.1f} KB")
                
                return output_folder
            else:
                print(f"❌ Folder download failed: HTTP {download_response.status_code}")
                print(f"Response: {download_response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error during folder download: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error during folder download: {e}")
            return None
    
    def _download_result(self, job_id, original_pdf_path, output_format):
        """Download the processed file and save it next to the original PDF"""
        try:
            # Download the file
            download_response = requests.get(
                f"{self.download_url}/{job_id}/{output_format}", 
                timeout=120
            )
            
            if download_response.status_code == 200:
                # Determine output filename (same location as PDF, different extension)
                if output_format == "markdown":
                    output_file = original_pdf_path.with_suffix('.md')
                elif output_format == "json":
                    output_file = original_pdf_path.with_suffix('.json')
                else:
                    output_file = original_pdf_path.with_suffix(f'.{output_format}')
                
                # Save the file
                with open(output_file, 'wb') as f:
                    f.write(download_response.content)
                
                # Show file size
                file_size = len(download_response.content) / 1024  # KB
                print(f"💾 Saved: {output_file} ({file_size:.1f} KB)")
                
                return output_file
            else:
                print(f"❌ Download failed: HTTP {download_response.status_code}")
                print(f"Response: {download_response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error during download: {e}")
            return None
        except Exception as e:
            print(f"❌ Unexpected error during download: {e}")
            return None

def find_pdf_files(folder_path):
    """Find all PDF files in the given folder"""
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    if not folder.is_dir():
        raise ValueError(f"Path is not a directory: {folder_path}")
    
    # Find all PDF files (case insensitive)
    pdf_files = list(folder.glob("*.pdf")) + list(folder.glob("*.PDF"))
    
    # Remove duplicates and sort
    pdf_files = sorted(list(set(pdf_files)))
    
    return pdf_files

def is_already_processed(pdf_path, output_format="markdown", download_all=False):
    """Check if PDF has already been processed by looking for output file or folder"""
    if download_all:
        # Check for folder with same name as PDF
        output_folder = pdf_path.parent / pdf_path.stem
        return output_folder.exists() and output_folder.is_dir()
    elif output_format == "markdown":
        output_file = pdf_path.with_suffix('.md')
    elif output_format == "json":
        output_file = pdf_path.with_suffix('.json')
    else:
        output_file = pdf_path.with_suffix(f'.{output_format}')
    
    return output_file.exists()

def ask_user_confirmation(pdf_path, current_index, total_count, download_all=False):
    """Ask user whether to process this PDF"""
    print(f"\n{'='*60}")
    print(f"📋 PDF {current_index}/{total_count}")
    print(f"📄 File: {pdf_path.name}")
    print(f"📂 Location: {pdf_path.parent}")
    print(f"📊 Size: {pdf_path.stat().st_size / 1024 / 1024:.1f} MB")
    
    # Check if already processed
    if is_already_processed(pdf_path, download_all=download_all):
        if download_all:
            print(f"✅ Already processed (folder '{pdf_path.stem}/' exists)")
        else:
            print(f"✅ Already processed (output file exists)")
    
    print(f"{'='*60}")
    
    while True:
        choice = input("\n🤔 Process this PDF? (y)es / (n)o / (s)kip all remaining / (q)uit: ").lower().strip()
        
        if choice in ['y', 'yes']:
            return 'process'
        elif choice in ['n', 'no']:
            return 'skip'
        elif choice in ['s', 'skip']:
            return 'skip_all'
        elif choice in ['q', 'quit']:
            return 'quit'
        else:
            print("❌ Invalid choice. Please enter 'y', 'n', 's', or 'q'")

def ask_automatic_mode():
    """Ask user if they want to process all PDFs automatically"""
    print("\n🤖 PROCESSING MODE SELECTION")
    print("="*50)
    print("Choose processing mode:")
    print("1. ⚡ Automatic - Process all unprocessed PDFs without asking")
    print("2. 🎛️  Interactive - Ask for confirmation for each PDF")
    print("="*50)
    
    while True:
        choice = input("\nSelect mode (1 for automatic, 2 for interactive): ").strip()
        
        if choice == '1':
            return True  # Automatic mode
        elif choice == '2':
            return False  # Interactive mode
        else:
            print("❌ Invalid choice. Please enter '1' or '2'")

def process_folder(parser_instance, folder_path, auto_mode=False, **kwargs):
    """Process all PDF files in a folder"""
    
    # Find all PDF files
    print(f"🔍 Scanning folder: {folder_path}")
    pdf_files = find_pdf_files(folder_path)
    
    if not pdf_files:
        print("❌ No PDF files found in the specified folder.")
        return
    
    print(f"✅ Found {len(pdf_files)} PDF file(s)")
    
    # Check which files are already processed
    download_all = kwargs.get('download_all', False)
    unprocessed_files = []
    already_processed = []
    
    for pdf_path in pdf_files:
        if is_already_processed(pdf_path, kwargs.get('output_format', 'markdown'), download_all):
            already_processed.append(pdf_path)
        else:
            unprocessed_files.append(pdf_path)
    
    # Show processing status
    output_type = "organized folders" if download_all else f"{kwargs.get('output_format', 'markdown')} files"
    print(f"📊 Status: {len(unprocessed_files)} unprocessed, {len(already_processed)} already processed ({output_type})")
    
    if already_processed:
        print(f"\n📁 Already processed (will skip):")
        for pdf_path in already_processed:
            if download_all:
                print(f"   ⏭️  {pdf_path.name} → folder '{pdf_path.stem}/' exists")
            else:
                print(f"   ⏭️  {pdf_path.name}")
    
    if not unprocessed_files:
        print(f"\n🎉 All PDFs in this folder have already been processed!")
        return
    
    print(f"\n📋 Will process {len(unprocessed_files)} PDF(s)")
    
    # If not in auto mode from command line, ask user
    if not auto_mode:
        auto_mode = ask_automatic_mode()
    
    if auto_mode:
        print(f"\n⚡ AUTOMATIC MODE ENABLED")
        print(f"🚀 Processing {len(unprocessed_files)} unprocessed PDF(s) automatically...")
        if download_all:
            print(f"📁 Will create organized folders: PDF_NAME/ (markdown + images + metadata)")
        print("="*60)
    
    # Process each unprocessed PDF
    processed_count = 0
    skipped_count = len(already_processed)
    failed_count = 0
    skip_all_remaining = False
    
    for i, pdf_path in enumerate(unprocessed_files, 1):
        try:
            if auto_mode:
                # Automatic mode - just process
                print(f"\n🚀 [{i}/{len(unprocessed_files)}] Processing: {pdf_path.name}")
                print("-" * 40)
                
                # Process the PDF
                output_file = parser_instance.parse_pdf(str(pdf_path), **kwargs)
                
                if output_file:
                    processed_count += 1
                    print(f"✅ Successfully processed: {pdf_path.name}")
                else:
                    failed_count += 1
                    print(f"❌ Failed to process: {pdf_path.name}")
                
            else:
                # Interactive mode - ask for confirmation
                if skip_all_remaining:
                    print(f"⏭️  Skipping {pdf_path.name} (skip all remaining)")
                    skipped_count += 1
                    continue
                
                # Ask user for confirmation
                user_choice = ask_user_confirmation(pdf_path, i, len(unprocessed_files), download_all)
                
                if user_choice == 'quit':
                    print("\n👋 User requested to quit. Exiting...")
                    break
                elif user_choice == 'skip_all':
                    print(f"\n⏭️  Skipping {pdf_path.name} and all remaining PDFs...")
                    skip_all_remaining = True
                    skipped_count += 1
                    continue
                elif user_choice == 'skip':
                    print(f"⏭️  Skipping {pdf_path.name}")
                    skipped_count += 1
                    continue
                elif user_choice == 'process':
                    print(f"\n🚀 Starting to process {pdf_path.name}...")
                    
                    # Process the PDF
                    output_file = parser_instance.parse_pdf(str(pdf_path), **kwargs)
                    
                    if output_file:
                        processed_count += 1
                        print(f"✅ Successfully processed: {pdf_path.name}")
                    else:
                        failed_count += 1
                        print(f"❌ Failed to process: {pdf_path.name}")
                    
                    print(f"\n{'='*30}")
                    print("Moving to next PDF...")
                    print(f"{'='*30}")
                
        except KeyboardInterrupt:
            print(f"\n❌ Process interrupted by user")
            break
        except Exception as e:
            print(f"\n❌ Failed to process {pdf_path.name}: {e}")
            failed_count += 1
            
            if not auto_mode:
                # Ask if user wants to continue after an error
                while True:
                    continue_choice = input("\n🤔 Continue with next PDF? (y)es / (n)o: ").lower().strip()
                    if continue_choice in ['y', 'yes']:
                        break
                    elif continue_choice in ['n', 'no']:
                        print("👋 Exiting...")
                        return
                    else:
                        print("❌ Invalid choice. Please enter 'y' or 'n'")
            else:
                print("⏭️  Continuing with next PDF...")
    
    # Final summary
    print(f"\n{'='*60}")
    print("📊 BATCH PROCESSING SUMMARY")
    print(f"{'='*60}")
    print(f"📄 Total PDFs found: {len(pdf_files)}")
    print(f"✅ Successfully processed: {processed_count}")
    print(f"⏭️  Skipped (including already processed): {skipped_count}")
    print(f"❌ Failed: {failed_count}")
    if download_all:
        print(f"📁 Output type: Organized folders (each PDF gets its own folder)")
    else:
        print(f"📝 Output type: {kwargs.get('output_format', 'markdown').upper()} files")
    print(f"{'='*60}")

def main():
    parser = argparse.ArgumentParser(
        description="Parse PDF files using your local Marker server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process single PDF
  python complete_local_marker_cli.py document.pdf
  python complete_local_marker_cli.py document.pdf --format json --ocr
  python complete_local_marker_cli.py document.pdf --all  # Create organized folder with all content
  
  # Process folder of PDFs (interactive mode)
  python complete_local_marker_cli.py --folder ./my_pdfs/
  python complete_local_marker_cli.py --folder /path/to/pdfs --format json
  
  # Process folder of PDFs (automatic mode)  
  python complete_local_marker_cli.py --folder ./my_pdfs/ --auto
  python complete_local_marker_cli.py --folder /path/to/pdfs --auto --ocr
  
  # Process folder and create organized folders for each PDF
  python complete_local_marker_cli.py --folder ./my_pdfs/ --auto --all
        """
    )
    
    # Mutually exclusive group for single file vs folder
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('pdf_path', nargs='?', help='Path to a single PDF file to parse')
    input_group.add_argument('--folder', help='Path to folder containing PDF files to process')
    
    parser.add_argument('--server', 
                       default='https://bfveyzbbejjao9-8888.proxy.runpod.net/',
                       help='Marker server URL (default: your RunPod server)')
    parser.add_argument('--format', 
                       default='markdown',
                       choices=['markdown', 'json'],
                       help='Output format: markdown or json (default: markdown)')
    parser.add_argument('--ocr', 
                       action='store_true',
                       help='Force OCR on all pages (slower)')
    parser.add_argument('--all',
                       action='store_true',
                       help='Create organized folders with all content (markdown, metadata, images) instead of single files')
    parser.add_argument('--auto',
                       action='store_true',
                       help='Automatically process all unprocessed PDFs without asking (folder mode only)')
    
    args = parser.parse_args()
    
    # Validate --auto flag usage
    if args.auto and not args.folder:
        print("❌ Error: --auto flag can only be used with --folder option")
        sys.exit(1)
    
    try:
        # Initialize parser
        pdf_parser = LocalMarkerParser(args.server)
        
        # Test server connection
        print(f"🔗 Testing connection to server: {args.server}")
        try:
            response = requests.get(f"{args.server}/", timeout=10)
            if response.status_code == 200:
                print("✅ Server connection successful!")
            else:
                print(f"⚠️  Server responded with status {response.status_code}")
        except Exception as e:
            print(f"❌ Cannot connect to server: {e}")
            print("Make sure your Marker server is running!")
            sys.exit(1)
        
        # Common processing arguments
        process_kwargs = {
            'output_format': args.format,
            'use_ocr': args.ocr,
            'download_all': args.all
        }
        
        if args.folder:
            # Process folder mode
            mode_text = "AUTOMATIC" if args.auto else "INTERACTIVE"
            download_text = " + COMPLETE FOLDERS" if args.all else ""
            print(f"\n🗂️  FOLDER PROCESSING MODE ({mode_text}{download_text})")
            print("="*50)
            process_folder(pdf_parser, args.folder, auto_mode=args.auto, **process_kwargs)
        else:
            # Process single file mode
            download_text = " + COMPLETE FOLDER" if args.all else ""
            print(f"\n📄 SINGLE FILE PROCESSING MODE ({args.format.upper()}{download_text})")
            print("="*50)
            output_file = pdf_parser.parse_pdf(pdf_path=args.pdf_path, **process_kwargs)
            if output_file:
                print(f"\n🎉 Success! Output saved as: {output_file}")
            else:
                print(f"\n❌ Processing failed!")
                sys.exit(1)
        
    except KeyboardInterrupt:
        print("\n❌ Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()