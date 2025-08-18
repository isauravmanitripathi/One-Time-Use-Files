#!/usr/bin/env python3
"""
Enhanced Local Marker PDF Parser CLI Tool with Parallel Processing
Processes PDFs using your self-hosted Marker server with parallel batch processing

Features:
- Single PDF processing (unchanged)
- Parallel batch processing (new)
- Retry mechanisms for failed jobs
- State persistence and crash recovery
- Real-time progress monitoring
- Backward compatible with all existing functionality

Usage Examples:
  # Single PDF (existing functionality - unchanged)
  python enhanced_cli.py document.pdf
  python enhanced_cli.py document.pdf --format json --ocr
  python enhanced_cli.py document.pdf --all  # Download complete folder
  
  # Folder processing (existing functionality - unchanged)
  python enhanced_cli.py --folder ./pdfs --auto
  python enhanced_cli.py --folder ./pdfs --auto --all
  
  # NEW: Parallel processing (3x faster)
  python enhanced_cli.py --folder ./pdfs --parallel --auto
  python enhanced_cli.py --folder ./pdfs --parallel --workers 5 --auto
  python enhanced_cli.py --folder ./pdfs --parallel --retry --auto
  python enhanced_cli.py --folder ./pdfs --parallel --all --auto
"""

import os
import sys
import time
import json
import argparse
import requests
import asyncio
import threading
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import glob

@dataclass
class JobInfo:
    """Track individual job information"""
    job_id: str
    pdf_path: str
    original_filename: str
    upload_time: str
    status: str = "uploading"
    retry_count: int = 0
    error_message: str = ""
    worker_id: Optional[int] = None
    download_completed: bool = False

@dataclass
class BatchState:
    """Track overall batch processing state"""
    folder_path: str
    processing_mode: str
    total_pdfs: int
    completed: List[str]
    failed: List[str]
    retry_queue: List[str]
    pending: List[str]
    active_jobs: Dict[str, JobInfo]
    start_time: str
    phase: str = "parallel"  # "parallel" or "retry"
    
    def to_dict(self):
        return {
            **asdict(self),
            'active_jobs': {k: asdict(v) for k, v in self.active_jobs.items()}
        }
    
    @classmethod
    def from_dict(cls, data):
        active_jobs = {k: JobInfo(**v) for k, v in data.pop('active_jobs', {}).items()}
        state = cls(**data)
        state.active_jobs = active_jobs
        return state

class EnhancedMarkerParser:
    def __init__(self, server_url="https://ueig4rheybsvxk-8888.proxy.runpod.net/"):
        self.server_url = server_url.rstrip('/')
        self.upload_url = f"{self.server_url}/upload"
        self.status_url = f"{self.server_url}/status"
        self.download_url = f"{self.server_url}/download"
        self.queue_url = f"{self.server_url}/queue"
        self.workers_url = f"{self.server_url}/workers"
        
        # Parallel processing settings
        self.max_workers = 3
        self.max_retries = 3
        self.polling_interval = 5
        self.retry_delay = 10
        
        # State management
        self.state_file = None
        self.batch_state = None
        self.stop_monitoring = False
        
    def test_connection(self):
        """Test server connection and get capabilities"""
        try:
            response = requests.get(f"{self.server_url}/", timeout=10)
            if response.status_code == 200:
                server_info = response.json()
                parallel_info = server_info.get('parallel_processing', {})
                print("✅ Server connection successful!")
                print(f"🏭 Server supports {parallel_info.get('max_concurrent_jobs', 'unknown')} parallel jobs")
                print(f"🔧 Currently {parallel_info.get('active_workers', 0)} active, {parallel_info.get('available_workers', 'unknown')} available")
                return True
            else:
                print(f"⚠️  Server responded with status {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Cannot connect to server: {e}")
            return False
    
    def get_server_status(self):
        """Get current server status"""
        try:
            response = requests.get(self.queue_url, timeout=10)
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return {}
    
    # EXISTING SINGLE PDF PROCESSING (UNCHANGED)
    def parse_pdf(self, pdf_path, output_format="markdown", use_ocr=False, download_all=False):
        """
        Parse a PDF file using your local Marker server (EXISTING FUNCTIONALITY)
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
    
    def _wait_for_completion(self, job_id, max_wait_time=1800):
        """Wait for job to complete, polling every few seconds"""
        start_time = time.time()
        poll_interval = self.polling_interval
        last_status = None
        
        while True:
            try:
                response = requests.get(f"{self.status_url}/{job_id}", timeout=30)
                
                if response.status_code == 200:
                    status_data = response.json()
                    current_status = status_data.get('status')
                    
                    if current_status != last_status:
                        if current_status == 'queued':
                            queue_pos = status_data.get('queue_position', 'Unknown')
                            system_status = status_data.get('system_status', {})
                            available = system_status.get('available_workers', 'Unknown')
                            print(f"⏸️  Status: Queued (position: {queue_pos}, {available} workers available)")
                        elif current_status == 'processing':
                            worker_info = status_data.get('worker_info', {})
                            worker_id = worker_info.get('worker_id', 'Unknown')
                            elapsed = worker_info.get('elapsed_formatted', 'Unknown')
                            print(f"🔄 Status: Processing by Worker {worker_id} ({elapsed})")
                        elif current_status == 'completed':
                            pages = status_data.get('pages_processed', 'Unknown')
                            processing_time = status_data.get('processing_time_seconds', 'Unknown')
                            worker_id = status_data.get('worker_id', 'Unknown')
                            print(f"✅ Status: Completed by Worker {worker_id}! ({pages} pages, {processing_time}s)")
                            return True
                        elif current_status == 'failed':
                            error_msg = status_data.get('error_message', 'Unknown error')
                            worker_id = status_data.get('worker_id', 'Unknown')
                            print(f"❌ Status: Failed on Worker {worker_id} - {error_msg}")
                            return False
                        elif current_status == 'timeout':
                            error_msg = status_data.get('error_message', 'Unknown error')
                            worker_id = status_data.get('worker_id', 'Unknown')
                            print(f"⏰ Status: Timed out on Worker {worker_id} - {error_msg}")
                            return False
                        
                        last_status = current_status
                    
                    # Show progress every 30 seconds for long jobs
                    elapsed = time.time() - start_time
                    if elapsed % 30 < poll_interval and current_status == 'processing':
                        worker_info = status_data.get('worker_info', {})
                        worker_id = worker_info.get('worker_id', 'Unknown')
                        elapsed_formatted = worker_info.get('elapsed_formatted', f"{int(elapsed)}s")
                        print(f"🔄 Still processing on Worker {worker_id}... ({elapsed_formatted})")
                
                elif response.status_code == 404:
                    print(f"❌ Job {job_id} not found")
                    return False
                else:
                    print(f"❌ Status check failed: HTTP {response.status_code}")
                
                if time.time() - start_time > max_wait_time:
                    print(f"⏰ Timeout: Processing took longer than {max_wait_time/60:.1f} minutes")
                    return False
                
                time.sleep(poll_interval)
                
            except requests.exceptions.RequestException as e:
                print(f"⚠️  Network error checking status: {e}")
                time.sleep(poll_interval * 2)
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
            download_response = requests.get(
                f"{self.download_url}/{job_id}/folder", 
                timeout=120
            )
            
            if download_response.status_code == 200:
                pdf_stem = original_pdf_path.stem
                output_folder = original_pdf_path.parent / pdf_stem
                
                counter = 1
                while output_folder.exists():
                    output_folder = original_pdf_path.parent / f"{pdf_stem}_{counter}"
                    counter += 1
                
                output_folder.mkdir(exist_ok=True)
                print(f"📁 Created folder: {output_folder}")
                
                import tempfile
                import zipfile
                
                temp_zip = tempfile.NamedTemporaryFile(delete=False, suffix='.zip')
                with open(temp_zip.name, 'wb') as f:
                    f.write(download_response.content)
                
                extracted_files = []
                with zipfile.ZipFile(temp_zip.name, 'r') as zip_ref:
                    for file_info in zip_ref.filelist:
                        if not file_info.is_dir():
                            zip_ref.extract(file_info, output_folder)
                            extracted_file = output_folder / file_info.filename
                            extracted_files.append(extracted_file)
                            
                            file_size = extracted_file.stat().st_size / 1024
                            if extracted_file.suffix == '.md':
                                print(f"   📄 Extracted: {file_info.filename} ({file_size:.1f} KB)")
                            elif extracted_file.suffix == '.json':
                                print(f"   🗂️  Extracted: {file_info.filename} ({file_size:.1f} KB)")
                            elif extracted_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                                print(f"   🖼️  Extracted: {file_info.filename} ({file_size:.1f} KB)")
                            else:
                                print(f"   📎 Extracted: {file_info.filename} ({file_size:.1f} KB)")
                
                import os
                os.unlink(temp_zip.name)
                
                total_size = sum(f.stat().st_size for f in extracted_files if f.exists()) / 1024
                print(f"✅ Extracted {len(extracted_files)} files to folder: {output_folder}")
                print(f"📊 Total size: {total_size:.1f} KB")
                
                return output_folder
            else:
                print(f"❌ Folder download failed: HTTP {download_response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error during folder download: {e}")
            return None
    
    def _download_result(self, job_id, original_pdf_path, output_format):
        """Download the processed file and save it next to the original PDF"""
        try:
            download_response = requests.get(
                f"{self.download_url}/{job_id}/{output_format}", 
                timeout=120
            )
            
            if download_response.status_code == 200:
                if output_format == "markdown":
                    output_file = original_pdf_path.with_suffix('.md')
                elif output_format == "json":
                    output_file = original_pdf_path.with_suffix('.json')
                else:
                    output_file = original_pdf_path.with_suffix(f'.{output_format}')
                
                with open(output_file, 'wb') as f:
                    f.write(download_response.content)
                
                file_size = len(download_response.content) / 1024
                print(f"💾 Saved: {output_file} ({file_size:.1f} KB)")
                
                return output_file
            else:
                print(f"❌ Download failed: HTTP {download_response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error during download: {e}")
            return None

    # NEW: PARALLEL PROCESSING METHODS
    
    def save_state(self):
        """Save current batch state to file for crash recovery"""
        if self.state_file and self.batch_state:
            try:
                with open(self.state_file, 'w') as f:
                    json.dump(self.batch_state.to_dict(), f, indent=2)
            except Exception as e:
                print(f"⚠️  Could not save state: {e}")
    
    def load_state(self, state_file):
        """Load previous batch state for crash recovery"""
        try:
            if Path(state_file).exists():
                with open(state_file, 'r') as f:
                    data = json.load(f)
                return BatchState.from_dict(data)
        except Exception as e:
            print(f"⚠️  Could not load state: {e}")
        return None
    
    def upload_pdf_parallel(self, pdf_path, output_format, use_ocr):
        """Upload PDF and return job info (for parallel processing)"""
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
                    job_id = result.get('job_id')
                    
                    if job_id:
                        job_info = JobInfo(
                            job_id=job_id,
                            pdf_path=str(pdf_path),
                            original_filename=pdf_path.name,
                            upload_time=datetime.now().isoformat(),
                            status="queued"
                        )
                        print(f"✅ Uploaded {pdf_path.name} → Job ID: {job_id}")
                        return job_info
                    
                else:
                    print(f"❌ Upload failed for {pdf_path.name}: HTTP {response.status_code}")
                    return None
                    
        except Exception as e:
            print(f"❌ Upload error for {pdf_path.name}: {e}")
            return None
    
    def check_job_status(self, job_info):
        """Check status of a single job and return updated job info"""
        try:
            response = requests.get(f"{self.status_url}/{job_info.job_id}", timeout=30)
            
            if response.status_code == 200:
                status_data = response.json()
                job_info.status = status_data.get('status')
                job_info.error_message = status_data.get('error_message', '')
                
                worker_info = status_data.get('worker_info', {})
                job_info.worker_id = worker_info.get('worker_id') or status_data.get('worker_id')
                
                return job_info
            else:
                job_info.status = 'failed'
                job_info.error_message = f"Status check failed: HTTP {response.status_code}"
                return job_info
                
        except Exception as e:
            job_info.status = 'failed'
            job_info.error_message = f"Status check error: {str(e)}"
            return job_info
    
    def download_completed_job(self, job_info, download_all=False, output_format="markdown"):
        """Download completed job result"""
        try:
            pdf_path = Path(job_info.pdf_path)
            
            if download_all:
                result = self._download_folder(job_info.job_id, pdf_path)
            else:
                result = self._download_result(job_info.job_id, pdf_path, output_format)
            
            if result:
                job_info.download_completed = True
                print(f"📥 Downloaded: {job_info.original_filename}")
                return True
            else:
                print(f"❌ Download failed: {job_info.original_filename}")
                return False
                
        except Exception as e:
            print(f"❌ Download error for {job_info.original_filename}: {e}")
            return False
    
    def monitor_jobs_parallel(self, active_jobs, download_all=False, output_format="markdown"):
        """Monitor multiple jobs in parallel and handle completions"""
        completed_jobs = []
        failed_jobs = []
        
        while active_jobs and not self.stop_monitoring:
            # Check status of all active jobs
            with ThreadPoolExecutor(max_workers=min(10, len(active_jobs))) as executor:
                # Submit status checks
                future_to_job = {
                    executor.submit(self.check_job_status, job_info): job_info 
                    for job_info in active_jobs.values()
                }
                
                # Process completed status checks
                for future in as_completed(future_to_job):
                    job_info = future_to_job[future]
                    try:
                        updated_job = future.result()
                        active_jobs[updated_job.job_id] = updated_job
                        
                        if updated_job.status == 'completed' and not updated_job.download_completed:
                            # Download the result
                            if self.download_completed_job(updated_job, download_all, output_format):
                                completed_jobs.append(updated_job)
                                del active_jobs[updated_job.job_id]
                        
                        elif updated_job.status in ['failed', 'timeout']:
                            failed_jobs.append(updated_job)
                            del active_jobs[updated_job.job_id]
                            
                    except Exception as e:
                        print(f"⚠️  Error processing job {job_info.job_id}: {e}")
            
            # Save state after each monitoring cycle
            if self.batch_state:
                self.save_state()
            
            if active_jobs and not self.stop_monitoring:
                time.sleep(self.polling_interval)
        
        return completed_jobs, failed_jobs
    
    def display_progress_parallel(self, state):
        """Display real-time progress for parallel processing"""
        def progress_thread():
            while not self.stop_monitoring:
                try:
                    # Get server status
                    server_status = self.get_server_status()
                    
                    # Clear screen and show progress
                    os.system('clear' if os.name == 'posix' else 'cls')
                    
                    print(f"🚀 PARALLEL PDF PROCESSING - {state.phase.upper()} PHASE")
                    print("=" * 60)
                    
                    # Overall progress
                    total_processed = len(state.completed) + len(state.failed)
                    progress_pct = (total_processed / state.total_pdfs) * 100 if state.total_pdfs > 0 else 0
                    
                    print(f"📊 Overall Progress: {total_processed}/{state.total_pdfs} ({progress_pct:.1f}%)")
                    print(f"✅ Completed: {len(state.completed)}")
                    print(f"❌ Failed: {len(state.failed)}")
                    print(f"🔄 Active Jobs: {len(state.active_jobs)}")
                    print(f"⏳ Pending: {len(state.pending)}")
                    if state.retry_queue:
                        print(f"🔁 Retry Queue: {len(state.retry_queue)}")
                    
                    print("\n🏭 Server Status:")
                    parallel_info = server_status.get('parallel_processing', {})
                    print(f"   Workers: {parallel_info.get('active_workers', 0)}/{parallel_info.get('max_concurrent_jobs', 'Unknown')} active")
                    print(f"   Queue: {server_status.get('queue_size', 0)} jobs waiting")
                    print(f"   Efficiency: {parallel_info.get('worker_efficiency', 'Unknown')}")
                    
                    # Show active jobs
                    if state.active_jobs:
                        print("\n🔄 Active Jobs:")
                        for job_info in state.active_jobs.values():
                            elapsed = (datetime.now() - datetime.fromisoformat(job_info.upload_time)).total_seconds()
                            worker_text = f"Worker {job_info.worker_id}" if job_info.worker_id else "Queued"
                            print(f"   📄 {job_info.original_filename} → {job_info.status} ({worker_text}, {int(elapsed)}s)")
                    
                    # Show recent completions
                    if state.completed:
                        recent_completed = state.completed[-3:] if len(state.completed) > 3 else state.completed
                        print(f"\n✅ Recent Completions: {', '.join(recent_completed)}")
                    
                    # Show failures
                    if state.failed:
                        recent_failed = state.failed[-3:] if len(state.failed) > 3 else state.failed
                        print(f"\n❌ Recent Failures: {', '.join(recent_failed)}")
                    
                    # Timing info
                    start_time = datetime.fromisoformat(state.start_time)
                    elapsed_total = datetime.now() - start_time
                    elapsed_str = f"{int(elapsed_total.total_seconds()//60)}m {int(elapsed_total.total_seconds()%60)}s"
                    
                    if total_processed > 0:
                        avg_time = elapsed_total.total_seconds() / total_processed
                        remaining_jobs = state.total_pdfs - total_processed
                        eta_seconds = remaining_jobs * avg_time
                        eta_str = f"{int(eta_seconds//60)}m {int(eta_seconds%60)}s"
                        print(f"\n⏱️  Elapsed: {elapsed_str} | ETA: {eta_str}")
                    else:
                        print(f"\n⏱️  Elapsed: {elapsed_str}")
                    
                    print("\n" + "=" * 60)
                    print("Press Ctrl+C to stop...")
                    
                    time.sleep(5)  # Update every 5 seconds
                    
                except Exception as e:
                    pass  # Ignore display errors
        
        # Start progress display in background thread
        progress_thread_obj = threading.Thread(target=progress_thread, daemon=True)
        progress_thread_obj.start()
        return progress_thread_obj
    
    def process_folder_parallel(self, folder_path, max_workers=None, enable_retry=True, 
                              auto_mode=True, output_format="markdown", use_ocr=False, 
                              download_all=False):
        """
        NEW: Process folder of PDFs with parallel processing and retry logic
        """
        
        # Set up parallel processing parameters
        if max_workers:
            self.max_workers = max_workers
        
        # Set up state file for crash recovery
        folder_name = Path(folder_path).name
        self.state_file = Path(folder_path) / f".marker_batch_state_{folder_name}.json"
        
        # Check for existing state (crash recovery)
        existing_state = self.load_state(self.state_file)
        if existing_state and not auto_mode:
            print(f"🔍 Found previous processing state for folder: {folder_path}")
            print(f"   Completed: {len(existing_state.completed)}")
            print(f"   Failed: {len(existing_state.failed)}")
            print(f"   Active: {len(existing_state.active_jobs)}")
            
            resume = input("\n🤔 Resume previous processing? (y/n): ").lower().strip() == 'y'
            if resume:
                self.batch_state = existing_state
                print("🔄 Resuming from previous state...")
            else:
                print("🆕 Starting fresh...")
                self.state_file.unlink(missing_ok=True)
                self.batch_state = None
        
        # Find all PDFs if starting fresh
        if not self.batch_state:
            print(f"🔍 Scanning folder: {folder_path}")
            pdf_files = self.find_pdf_files(folder_path)
            
            if not pdf_files:
                print("❌ No PDF files found in the specified folder.")
                return
            
            # Check which files are already processed
            unprocessed_files = []
            already_processed = []
            
            for pdf_path in pdf_files:
                if self.is_already_processed(pdf_path, output_format, download_all):
                    already_processed.append(pdf_path.name)
                else:
                    unprocessed_files.append(pdf_path)
            
            print(f"✅ Found {len(pdf_files)} PDF file(s)")
            print(f"📊 Status: {len(unprocessed_files)} unprocessed, {len(already_processed)} already processed")
            
            if not unprocessed_files:
                print(f"\n🎉 All PDFs in this folder have already been processed!")
                return
            
            # Initialize batch state
            self.batch_state = BatchState(
                folder_path=str(folder_path),
                processing_mode="parallel",
                total_pdfs=len(unprocessed_files),
                completed=already_processed.copy(),
                failed=[],
                retry_queue=[],
                pending=[str(pdf) for pdf in unprocessed_files],
                active_jobs={},
                start_time=datetime.now().isoformat(),
                phase="parallel"
            )
        
        print(f"\n🚀 STARTING PARALLEL PROCESSING")
        print(f"📁 Folder: {folder_path}")
        print(f"📄 Total PDFs to process: {len(self.batch_state.pending)}")
        print(f"🏭 Max parallel workers: {self.max_workers}")
        print(f"🔄 Retry enabled: {enable_retry}")
        print(f"📦 Download mode: {'Complete folders' if download_all else f'{output_format} files'}")
        print("=" * 60)
        
        # Start progress display
        progress_thread = self.display_progress_parallel(self.batch_state)
        
        try:
            # PHASE 1: PARALLEL PROCESSING
            print(f"\n🚀 PHASE 1: PARALLEL PROCESSING")
            self.batch_state.phase = "parallel"
            
            while self.batch_state.pending or self.batch_state.active_jobs:
                # Fill available worker slots
                while (len(self.batch_state.active_jobs) < self.max_workers and 
                       self.batch_state.pending):
                    
                    pdf_path_str = self.batch_state.pending.pop(0)
                    pdf_path = Path(pdf_path_str)
                    
                    # Upload PDF
                    job_info = self.upload_pdf_parallel(pdf_path, output_format, use_ocr)
                    if job_info:
                        self.batch_state.active_jobs[job_info.job_id] = job_info
                    else:
                        # Upload failed - add to retry queue
                        self.batch_state.failed.append(pdf_path.name)
                        self.batch_state.retry_queue.append(pdf_path_str)
                    
                    self.save_state()
                    time.sleep(1)  # Small delay between uploads
                
                # Monitor active jobs
                if self.batch_state.active_jobs:
                    completed, failed = self.monitor_jobs_parallel(
                        self.batch_state.active_jobs, download_all, output_format
                    )
                    
                    # Update state with results
                    for job in completed:
                        self.batch_state.completed.append(Path(job.pdf_path).name)
                    
                    for job in failed:
                        pdf_name = Path(job.pdf_path).name
                        if pdf_name not in self.batch_state.failed:
                            self.batch_state.failed.append(pdf_name)
                            if enable_retry:
                                self.batch_state.retry_queue.append(job.pdf_path)
                    
                    self.save_state()
                
                # Brief pause before next iteration
                if self.batch_state.pending or self.batch_state.active_jobs:
                    time.sleep(2)
            
            # PHASE 2: RETRY PROCESSING (if enabled and there are failures)
            if enable_retry and self.batch_state.retry_queue:
                print(f"\n🔄 PHASE 2: RETRY PROCESSING")
                print(f"📋 Retrying {len(self.batch_state.retry_queue)} failed PDF(s)")
                self.batch_state.phase = "retry"
                
                retry_pdfs = self.batch_state.retry_queue.copy()
                self.batch_state.retry_queue = []
                
                for pdf_path_str in retry_pdfs:
                    if self.stop_monitoring:
                        break
                    
                    pdf_path = Path(pdf_path_str)
                    pdf_name = pdf_path.name
                    
                    # Find existing retry count
                    retry_count = self.batch_state.failed.count(pdf_name)
                    
                    if retry_count >= self.max_retries:
                        print(f"❌ Max retries reached for {pdf_name}")
                        continue
                    
                    print(f"\n🔁 Retrying {pdf_name} (attempt {retry_count + 1}/{self.max_retries})")
                    
                    # Single-worker retry (safer for problematic PDFs)
                    job_info = self.upload_pdf_parallel(pdf_path, output_format, use_ocr)
                    
                    if job_info:
                        # Monitor this single job
                        active_jobs = {job_info.job_id: job_info}
                        completed, failed = self.monitor_jobs_parallel(
                            active_jobs, download_all, output_format
                        )
                        
                        if completed:
                            # Remove from failed list and add to completed
                            while pdf_name in self.batch_state.failed:
                                self.batch_state.failed.remove(pdf_name)
                            self.batch_state.completed.append(pdf_name)
                            print(f"✅ Retry successful: {pdf_name}")
                        else:
                            # Add back to retry queue if not at max retries
                            if retry_count + 1 < self.max_retries:
                                self.batch_state.retry_queue.append(pdf_path_str)
                            print(f"❌ Retry failed: {pdf_name}")
                        
                        self.save_state()
                    
                    # Delay between retry attempts
                    if retry_pdfs.index(pdf_path_str) < len(retry_pdfs) - 1:
                        time.sleep(self.retry_delay)
        
        except KeyboardInterrupt:
            print(f"\n❌ Processing interrupted by user")
            self.stop_monitoring = True
        
        finally:
            self.stop_monitoring = True
            time.sleep(1)  # Let progress thread finish
        
        # FINAL SUMMARY
        self.print_batch_summary()
        
        # Cleanup state file on successful completion
        if not self.batch_state.retry_queue and not self.batch_state.active_jobs:
            self.state_file.unlink(missing_ok=True)
    
    def print_batch_summary(self):
        """Print comprehensive batch processing summary"""
        if not self.batch_state:
            return
        
        # Clear screen for final summary
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print("=" * 70)
        print("📊 BATCH PROCESSING COMPLETE")
        print("=" * 70)
        
        # Calculate timing
        start_time = datetime.fromisoformat(self.batch_state.start_time)
        total_time = datetime.now() - start_time
        total_minutes = total_time.total_seconds() / 60
        
        # Results summary
        total_attempted = len(self.batch_state.completed) + len(self.batch_state.failed)
        success_rate = (len(self.batch_state.completed) / total_attempted * 100) if total_attempted > 0 else 0
        
        print(f"📄 Total PDFs: {self.batch_state.total_pdfs}")
        print(f"✅ Successfully processed: {len(self.batch_state.completed)}")
        print(f"❌ Failed (final): {len(set(self.batch_state.failed))}")  # Remove duplicates
        print(f"📈 Success rate: {success_rate:.1f}%")
        print(f"⏱️  Total time: {int(total_minutes)}m {int(total_time.total_seconds() % 60)}s")
        
        # Calculate speedup (estimate)
        if len(self.batch_state.completed) > 0:
            avg_time_per_pdf = total_time.total_seconds() / len(self.batch_state.completed)
            sequential_time = avg_time_per_pdf * len(self.batch_state.completed)
            speedup = sequential_time / total_time.total_seconds()
            print(f"🚀 Estimated speedup: {speedup:.1f}x faster than sequential")
        
        # Output format info
        download_type = "organized folders (markdown + images + metadata)" if self.batch_state.phase == "all" else f"{self.batch_state.processing_mode} files"
        print(f"📁 Output format: {download_type}")
        
        # Failed files details
        unique_failures = list(set(self.batch_state.failed))
        if unique_failures:
            print(f"\n❌ Failed Files ({len(unique_failures)}):")
            for filename in unique_failures:
                retry_count = self.batch_state.failed.count(filename)
                print(f"   📄 {filename} (failed {retry_count} times)")
        
        # Success files (if reasonable number)
        if len(self.batch_state.completed) <= 10:
            print(f"\n✅ Completed Files:")
            for filename in self.batch_state.completed:
                print(f"   📄 {filename}")
        elif len(self.batch_state.completed) > 10:
            print(f"\n✅ Completed Files: {len(self.batch_state.completed)} files processed successfully")
        
        print("=" * 70)
    
    def find_pdf_files(self, folder_path):
        """Find all PDF files in the given folder (existing method)"""
        folder = Path(folder_path)
        if not folder.exists():
            raise FileNotFoundError(f"Folder not found: {folder_path}")
        if not folder.is_dir():
            raise ValueError(f"Path is not a directory: {folder_path}")
        
        pdf_files = list(folder.glob("*.pdf")) + list(folder.glob("*.PDF"))
        pdf_files = sorted(list(set(pdf_files)))
        return pdf_files
    
    def is_already_processed(self, pdf_path, output_format="markdown", download_all=False):
        """Check if PDF has already been processed (existing method)"""
        if download_all:
            output_folder = pdf_path.parent / pdf_path.stem
            return output_folder.exists() and output_folder.is_dir()
        elif output_format == "markdown":
            output_file = pdf_path.with_suffix('.md')
        elif output_format == "json":
            output_file = pdf_path.with_suffix('.json')
        else:
            output_file = pdf_path.with_suffix(f'.{output_format}')
        
        return output_file.exists()

# EXISTING HELPER FUNCTIONS (UNCHANGED)

def ask_user_confirmation(pdf_path, current_index, total_count, download_all=False):
    """Ask user whether to process this PDF (existing function)"""
    print(f"\n{'='*60}")
    print(f"📋 PDF {current_index}/{total_count}")
    print(f"📄 File: {pdf_path.name}")
    print(f"📂 Location: {pdf_path.parent}")
    print(f"📊 Size: {pdf_path.stat().st_size / 1024 / 1024:.1f} MB")
    
    # Check if already processed
    parser = EnhancedMarkerParser()  # Temporary instance for checking
    if parser.is_already_processed(pdf_path, download_all=download_all):
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
    """Ask user if they want to process all PDFs automatically (existing function)"""
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

def process_folder_sequential(parser_instance, folder_path, auto_mode=False, **kwargs):
    """
    Process all PDF files in a folder sequentially (EXISTING FUNCTIONALITY - UNCHANGED)
    """
    
    # Find all PDF files
    print(f"🔍 Scanning folder: {folder_path}")
    pdf_files = parser_instance.find_pdf_files(folder_path)
    
    if not pdf_files:
        print("❌ No PDF files found in the specified folder.")
        return
    
    print(f"✅ Found {len(pdf_files)} PDF file(s)")
    
    # Check which files are already processed
    download_all = kwargs.get('download_all', False)
    unprocessed_files = []
    already_processed = []
    
    for pdf_path in pdf_files:
        if parser_instance.is_already_processed(pdf_path, kwargs.get('output_format', 'markdown'), download_all):
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
    print("📊 SEQUENTIAL PROCESSING SUMMARY")
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
        description="Enhanced PDF parser with parallel processing support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single PDF (existing functionality - unchanged)
  python enhanced_cli.py document.pdf
  python enhanced_cli.py document.pdf --format json --ocr
  python enhanced_cli.py document.pdf --all  # Create organized folder
  
  # Sequential folder processing (existing functionality - unchanged)  
  python enhanced_cli.py --folder ./pdfs/
  python enhanced_cli.py --folder ./pdfs --auto
  
  # NEW: Parallel processing (3x faster)
  python enhanced_cli.py --folder ./pdfs --parallel --auto
  python enhanced_cli.py --folder ./pdfs --parallel --workers 5 --auto
  python enhanced_cli.py --folder ./pdfs --parallel --retry --auto --all
        """
    )
    
    # Mutually exclusive group for single file vs folder
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('pdf_path', nargs='?', help='Path to a single PDF file to parse')
    input_group.add_argument('--folder', help='Path to folder containing PDF files to process')
    
    parser.add_argument('--server', 
                       default='https://ueig4rheybsvxk-8888.proxy.runpod.net/',
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
                       help='Create organized folders with all content (markdown, metadata, images)')
    parser.add_argument('--auto',
                       action='store_true',
                       help='Automatically process all unprocessed PDFs without asking (folder mode only)')
    
    # NEW: Parallel processing arguments
    parser.add_argument('--parallel',
                       action='store_true',
                       help='Enable parallel processing (folder mode only)')
    parser.add_argument('--workers',
                       type=int,
                       default=3,
                       help='Number of parallel workers (default: 3, max recommended: 5)')
    parser.add_argument('--retry',
                       action='store_true',
                       help='Enable retry mode for failed PDFs (parallel mode only)')
    
    args = parser.parse_args()
    
    # Validate argument combinations
    if args.parallel and not args.folder:
        print("❌ Error: --parallel can only be used with --folder option")
        sys.exit(1)
    
    if args.workers != 3 and not args.parallel:
        print("❌ Error: --workers can only be used with --parallel option")
        sys.exit(1)
    
    if args.retry and not args.parallel:
        print("❌ Error: --retry can only be used with --parallel option")
        sys.exit(1)
    
    if args.auto and not args.folder:
        print("❌ Error: --auto flag can only be used with --folder option")
        sys.exit(1)
    
    try:
        # Initialize parser
        pdf_parser = EnhancedMarkerParser(args.server)
        
        # Test server connection
        print(f"🔗 Testing connection to server: {args.server}")
        if not pdf_parser.test_connection():
            print("Make sure your Marker server is running!")
            sys.exit(1)
        
        # Common processing arguments
        process_kwargs = {
            'output_format': args.format,
            'use_ocr': args.ocr,
            'download_all': args.all
        }
        
        if args.folder:
            if args.parallel:
                # NEW: Parallel processing mode
                mode_text = "PARALLEL PROCESSING"
                if args.auto:
                    mode_text += " (AUTOMATIC)"
                download_text = " + COMPLETE FOLDERS" if args.all else ""
                
                print(f"\n🚀 {mode_text}{download_text}")
                print("="*50)
                print(f"🏭 Workers: {args.workers}")
                print(f"🔄 Retry enabled: {args.retry}")
                
                pdf_parser.process_folder_parallel(
                    args.folder, 
                    max_workers=args.workers,
                    enable_retry=args.retry,
                    auto_mode=args.auto,
                    **process_kwargs
                )
            else:
                # Existing sequential processing
                mode_text = "AUTOMATIC" if args.auto else "INTERACTIVE"
                download_text = " + COMPLETE FOLDERS" if args.all else ""
                print(f"\n🗂️  SEQUENTIAL FOLDER PROCESSING ({mode_text}{download_text})")
                print("="*50)
                process_folder_sequential(pdf_parser, args.folder, auto_mode=args.auto, **process_kwargs)
        else:
            # Process single file mode (unchanged)
            download_text = " + COMPLETE FOLDER" if args.all else ""
            print(f"\n📄 SINGLE FILE PROCESSING ({args.format.upper()}{download_text})")
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