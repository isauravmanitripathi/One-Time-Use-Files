#!/usr/bin/env python3
"""
Enhanced Local Marker PDF Parser CLI Tool - Complete Implementation with Skip Logic and Retry System
Features:
- Session management and tracking
- Smart batch processing with parallel uploads/downloads
- Configurable storage and retention policies
- Real-time monitoring dashboard
- Download tracking and auto-cleanup integration
- Resume capability for interrupted processing
- Smart skip logic for already processed files
- Failed job retry system

Usage Examples:
  # Basic processing
  python enhanced_marker_cli.py document.pdf
  
  # Custom retention and storage
  python enhanced_marker_cli.py document.pdf --retention 7d --storage-path /project/outputs
  
  # Smart batch processing
  python enhanced_marker_cli.py --folder ./pdfs --auto --retention immediate
  
  # Real-time monitoring
  python enhanced_marker_cli.py --monitor
  
  # Session management
  python enhanced_marker_cli.py --folder ./pdfs --auto --session-cleanup
"""

import os
import sys
import time
import json
import argparse
import requests
import threading
import signal
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import concurrent.futures
from dataclasses import dataclass
import tempfile
import zipfile

@dataclass
class JobInfo:
    """Data class for tracking job information"""
    job_id: str
    pdf_path: Path
    status: str = "uploading"
    upload_time: Optional[datetime] = None
    completion_time: Optional[datetime] = None
    output_file: Optional[Path] = None
    error_message: Optional[str] = None
    pages_processed: Optional[int] = None
    processing_time: Optional[int] = None
    file_count: Optional[int] = None
    download_count: int = 0
    retry_count: int = 0
    failure_stage: Optional[str] = None  # 'upload', 'processing', 'download'

class EnhancedMarkerParser:
    def __init__(self, server_url="https://mbxsqv2e682vet-8888.proxy.runpod.net/"):
        self.server_url = server_url.rstrip('/')
        self.session_id = None
        self.active_jobs = {}  # job_id -> JobInfo
        self.completed_jobs = {}  # job_id -> JobInfo
        self.failed_jobs = {}  # job_id -> JobInfo
        self.skipped_jobs = {}  # pdf_path -> reason for skip
        
        # API endpoints
        self.upload_url = f"{self.server_url}/upload"
        self.status_url = f"{self.server_url}/status"
        self.download_url = f"{self.server_url}/download"
        self.session_url = f"{self.server_url}/session"
        self.queue_url = f"{self.server_url}/queue"
        self.workers_url = f"{self.server_url}/workers/status"
        self.storage_url = f"{self.server_url}/storage/stats"
        
        # Configuration
        self.max_concurrent_uploads = 3
        self.max_concurrent_downloads = 5
        self.poll_interval = 3  # seconds
        self.dashboard_refresh = 5  # seconds
        self.max_retries = 2  # Maximum retry attempts per file
        
        # Session state file for resume capability
        self.state_file = Path.cwd() / ".marker_cli_session.json"
        
        print(f"🔗 Enhanced Marker CLI initialized")
        print(f"📡 Server: {self.server_url}")
    
    def check_already_processed(self, pdf_path: Path, output_format: str, download_all: bool) -> Tuple[bool, str]:
        """
        Enhanced check for already processed files
        Returns: (is_processed, reason)
        """
        pdf_name = pdf_path.stem
        pdf_parent = pdf_path.parent
        
        if download_all:
            # Check for output folder
            output_folder = pdf_parent / pdf_name
            if output_folder.exists() and output_folder.is_dir():
                # Check if folder has content (not just empty)
                contents = list(output_folder.iterdir())
                if contents:
                    return True, f"Output folder exists: {output_folder.name}/ ({len(contents)} files)"
        
        # Check for single format output
        if output_format == "markdown":
            output_file = pdf_path.with_suffix('.md')
        elif output_format == "json":
            output_file = pdf_path.with_suffix('.json')
        else:
            output_file = pdf_path.with_suffix(f'.{output_format}')
        
        if output_file.exists():
            file_size = output_file.stat().st_size
            if file_size > 0:  # Ensure file is not empty
                return True, f"Output file exists: {output_file.name} ({file_size/1024:.1f} KB)"
        
        return False, ""
    
    def scan_and_categorize_pdfs(self, folder: Path, output_format: str, download_all: bool) -> Dict[str, List[Path]]:
        """
        Scan folder and categorize PDFs into processed, unprocessed, and invalid
        """
        print(f"🔍 Scanning folder: {folder}")
        
        # Find all PDF files
        pdf_files = self._find_pdf_files(folder)
        
        if not pdf_files:
            return {
                'all_pdfs': [],
                'unprocessed': [],
                'already_processed': [],
                'invalid': []
            }
        
        print(f"📄 Found {len(pdf_files)} PDF file(s)")
        print("🔍 Checking processing status...")
        
        unprocessed = []
        already_processed = []
        invalid = []
        
        for pdf_path in pdf_files:
            try:
                # Check if file is readable
                if not pdf_path.exists() or pdf_path.stat().st_size == 0:
                    invalid.append(pdf_path)
                    continue
                
                # Check if already processed
                is_processed, reason = self.check_already_processed(pdf_path, output_format, download_all)
                
                if is_processed:
                    already_processed.append(pdf_path)
                    self.skipped_jobs[str(pdf_path)] = reason
                    print(f"   ⏭️  SKIP: {pdf_path.name} - {reason}")
                else:
                    unprocessed.append(pdf_path)
                    print(f"   📝 TODO: {pdf_path.name} ({pdf_path.stat().st_size / (1024*1024):.1f} MB)")
                    
            except Exception as e:
                print(f"   ❌ ERROR checking {pdf_path.name}: {e}")
                invalid.append(pdf_path)
        
        return {
            'all_pdfs': pdf_files,
            'unprocessed': unprocessed,
            'already_processed': already_processed,
            'invalid': invalid
        }
    
    def start_session(self) -> str:
        """Start a new server session"""
        try:
            if self.session_id:
                return self.session_id
            
            response = requests.post(f"{self.session_url}/start", timeout=30)
            if response.status_code == 200:
                result = response.json()
                self.session_id = result['session_id']
                print(f"🎯 Session started: {self.session_id}")
                self._save_session_state()
                return self.session_id
            else:
                print(f"⚠️  Failed to start session: HTTP {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error starting session: {e}")
            return None
    
    def _save_session_state(self):
        """Save current session state for resume capability"""
        try:
            state = {
                'session_id': self.session_id,
                'active_jobs': {jid: {
                    'job_id': job.job_id,
                    'pdf_path': str(job.pdf_path),
                    'status': job.status,
                    'upload_time': job.upload_time.isoformat() if job.upload_time else None,
                    'retry_count': job.retry_count,
                    'failure_stage': job.failure_stage
                } for jid, job in self.active_jobs.items()},
                'failed_jobs': {jid: {
                    'job_id': job.job_id,
                    'pdf_path': str(job.pdf_path),
                    'status': job.status,
                    'error_message': job.error_message,
                    'retry_count': job.retry_count,
                    'failure_stage': job.failure_stage
                } for jid, job in self.failed_jobs.items()},
                'last_update': datetime.now().isoformat()
            }
            
            with open(self.state_file, 'w') as f:
                json.dump(state, f, indent=2)
        except Exception:
            pass  # Silently fail if can't save state
    
    def _load_session_state(self) -> bool:
        """Load previous session state for resume"""
        try:
            if not self.state_file.exists():
                return False
            
            with open(self.state_file, 'r') as f:
                state = json.load(f)
            
            # Check if state is recent (within 24 hours)
            last_update = datetime.fromisoformat(state['last_update'])
            if datetime.now() - last_update > timedelta(hours=24):
                self.state_file.unlink(missing_ok=True)
                return False
            
            self.session_id = state.get('session_id')
            
            # Restore active jobs
            for job_data in state.get('active_jobs', {}).values():
                job = JobInfo(
                    job_id=job_data['job_id'],
                    pdf_path=Path(job_data['pdf_path']),
                    status=job_data['status'],
                    upload_time=datetime.fromisoformat(job_data['upload_time']) if job_data['upload_time'] else None,
                    retry_count=job_data.get('retry_count', 0),
                    failure_stage=job_data.get('failure_stage')
                )
                self.active_jobs[job.job_id] = job
            
            # Restore failed jobs
            for job_data in state.get('failed_jobs', {}).values():
                job = JobInfo(
                    job_id=job_data['job_id'],
                    pdf_path=Path(job_data['pdf_path']),
                    status=job_data['status'],
                    error_message=job_data.get('error_message'),
                    retry_count=job_data.get('retry_count', 0),
                    failure_stage=job_data.get('failure_stage')
                )
                self.failed_jobs[job.job_id] = job
            
            if self.active_jobs or self.failed_jobs:
                print(f"📋 Resumed session {self.session_id} with {len(self.active_jobs)} active and {len(self.failed_jobs)} failed jobs")
                return True
            
            return False
        except Exception:
            return False
    
    def test_connection(self) -> bool:
        """Test server connection and show server info"""
        try:
            print(f"🔗 Testing connection to: {self.server_url}")
            response = requests.get(f"{self.server_url}/", timeout=10)
            
            if response.status_code == 200:
                info = response.json()
                print("✅ Server connection successful!")
                print(f"   📊 Version: {info.get('version', 'Unknown')}")
                print(f"   🔧 Workers: {info.get('workers', {}).get('max_threads', 'Unknown')}")
                print(f"   🎮 GPU slots: {info.get('workers', {}).get('max_gpu_concurrent', 'Unknown')}")
                print(f"   📈 Queue: {info.get('queue', {}).get('queued', 0)} queued, {info.get('queue', {}).get('processing', 0)} processing")
                return True
            else:
                print(f"⚠️  Server responded with status {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Cannot connect to server: {e}")
            print("Make sure your Enhanced Marker server is running!")
            return False
    
    def upload_pdf(self, pdf_path: Path, output_format: str = "markdown", 
                   use_ocr: bool = False, storage_path: str = None,
                   retention: str = "24h", max_downloads: int = 3,
                   download_all: bool = False, keep_alive: bool = False) -> Optional[str]:
        """Upload PDF with enhanced parameters"""
        
        if not self.session_id:
            self.start_session()
        
        try:
            print(f"📤 Uploading: {pdf_path.name}")
            print(f"   📊 Size: {pdf_path.stat().st_size / 1024 / 1024:.1f} MB")
            print(f"   🔧 Format: {output_format}")
            print(f"   👁️  OCR: {'Yes' if use_ocr else 'No'}")
            print(f"   📁 Storage: {storage_path or 'default'}")
            print(f"   🗂️  Retention: {retention}")
            print(f"   📥 Max downloads: {max_downloads}")
            
            with open(pdf_path, 'rb') as f:
                files = {'file': (pdf_path.name, f, 'application/pdf')}
                data = {
                    'format': output_format,
                    'ocr': str(use_ocr).lower(),
                    'session_id': self.session_id,
                    'storage_path': storage_path or '',
                    'retention': retention,
                    'max_downloads': max_downloads
                }
                
                response = requests.post(self.upload_url, files=files, data=data, timeout=120)
                
                if response.status_code == 200:
                    result = response.json()
                    job_id = result.get('job_id')
                    
                    # Create job tracking
                    job = JobInfo(
                        job_id=job_id,
                        pdf_path=pdf_path,
                        status="queued",
                        upload_time=datetime.now()
                    )
                    self.active_jobs[job_id] = job
                    self._save_session_state()
                    
                    print(f"✅ Upload successful! Job ID: {job_id}")
                    print(f"📊 Queue position: {result.get('queue_position', 'Unknown')}")
                    
                    return job_id
                else:
                    print(f"❌ Upload failed: HTTP {response.status_code}")
                    if response.text:
                        print(f"   Error: {response.text}")
                    return None
                    
        except Exception as e:
            print(f"❌ Upload error: {e}")
            return None
    
    def check_job_status(self, job_id: str, detailed: bool = False) -> Optional[Dict]:
        """Check job status with optional detailed information"""
        try:
            endpoint = f"{self.status_url}/{job_id}/detailed" if detailed else f"{self.status_url}/{job_id}"
            response = requests.get(endpoint, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print(f"❌ Job {job_id} not found")
                return None
            else:
                print(f"⚠️  Status check failed: HTTP {response.status_code}")
                return None
                
        except Exception as e:
            print(f"⚠️  Error checking status: {e}")
            return None
    
    def download_job_result(self, job_id: str, original_pdf_path: Path, 
                           output_format: str = "markdown", download_all: bool = False,
                           keep_alive: bool = False) -> Optional[Path]:
        """Download job result with tracking"""
        
        try:
            file_type = "all" if download_all else output_format
            
            # Add query parameters for download tracking
            params = {
                'mark_downloaded': 'true',
                'trigger_cleanup': 'false' if keep_alive else 'true'
            }
            
            print(f"📥 Downloading {file_type} for job {job_id}...")
            
            download_response = requests.get(
                f"{self.download_url}/{job_id}/{file_type}",
                params=params,
                timeout=300
            )
            
            if download_response.status_code == 200:
                if download_all:
                    return self._save_zip_and_extract(download_response.content, original_pdf_path)
                else:
                    return self._save_single_file(download_response.content, original_pdf_path, output_format)
            else:
                print(f"❌ Download failed: HTTP {download_response.status_code}")
                if download_response.text:
                    print(f"   Error: {download_response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Download error: {e}")
            return None
    
    def _save_single_file(self, content: bytes, original_pdf_path: Path, output_format: str) -> Path:
        """Save single file download"""
        if output_format == "markdown":
            output_file = original_pdf_path.with_suffix('.md')
        elif output_format == "json":
            output_file = original_pdf_path.with_suffix('.json')
        else:
            output_file = original_pdf_path.with_suffix(f'.{output_format}')
        
        with open(output_file, 'wb') as f:
            f.write(content)
        
        file_size = len(content) / 1024
        print(f"✅ Saved: {output_file} ({file_size:.1f} KB)")
        return output_file
    
    def _save_zip_and_extract(self, content: bytes, original_pdf_path: Path) -> Path:
        """Save and extract ZIP download to organized folder"""
        
        # Create folder with same name as PDF
        pdf_stem = original_pdf_path.stem
        output_folder = original_pdf_path.parent / pdf_stem
        
        # If folder exists, add number
        counter = 1
        while output_folder.exists():
            output_folder = original_pdf_path.parent / f"{pdf_stem}_{counter}"
            counter += 1
        
        output_folder.mkdir(exist_ok=True)
        print(f"📁 Created folder: {output_folder}")
        
        # Save ZIP temporarily and extract
        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as temp_zip:
            temp_zip.write(content)
            temp_zip_path = temp_zip.name
        
        try:
            extracted_files = []
            with zipfile.ZipFile(temp_zip_path, 'r') as zip_ref:
                for file_info in zip_ref.filelist:
                    if not file_info.is_dir():
                        zip_ref.extract(file_info, output_folder)
                        extracted_file = output_folder / file_info.filename
                        extracted_files.append(extracted_file)
                        
                        # Show extracted file info
                        file_size = extracted_file.stat().st_size / 1024
                        if extracted_file.suffix == '.md':
                            print(f"   📄 Extracted: {file_info.filename} ({file_size:.1f} KB)")
                        elif extracted_file.suffix == '.json':
                            print(f"   🗂️  Extracted: {file_info.filename} ({file_size:.1f} KB)")
                        elif extracted_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                            print(f"   🖼️  Extracted: {file_info.filename} ({file_size:.1f} KB)")
                        else:
                            print(f"   📎 Extracted: {file_info.filename} ({file_size:.1f} KB)")
            
            total_size = sum(f.stat().st_size for f in extracted_files if f.exists()) / 1024
            print(f"✅ Extracted {len(extracted_files)} files to: {output_folder}")
            print(f"📊 Total size: {total_size:.1f} KB")
            
            return output_folder
            
        finally:
            # Clean up temporary ZIP
            os.unlink(temp_zip_path)
    
    def process_single_pdf(self, pdf_path: str, **kwargs) -> Optional[Path]:
        """Process a single PDF with full workflow"""
        
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        if not pdf_path.suffix.lower() == '.pdf':
            raise ValueError("File must be a PDF")
        
        print(f"\n{'='*60}")
        print(f"📄 PROCESSING: {pdf_path.name}")
        print(f"{'='*60}")
        
        # Check if already processed
        is_processed, reason = self.check_already_processed(
            pdf_path, 
            kwargs.get('output_format', 'markdown'), 
            kwargs.get('download_all', False)
        )
        
        if is_processed:
            print(f"⏭️  SKIPPED: {reason}")
            return None
        
        try:
            # Step 1: Upload
            job_id = self.upload_pdf(pdf_path, **kwargs)
            if not job_id:
                return None
            
            # Step 2: Monitor until completion
            if not self.wait_for_completion(job_id):
                return None
            
            # Step 3: Download result
            output_file = self.download_job_result(
                job_id, pdf_path, 
                kwargs.get('output_format', 'markdown'),
                kwargs.get('download_all', False),
                kwargs.get('keep_alive', False)
            )
            
            if output_file:
                # Update job tracking
                if job_id in self.active_jobs:
                    job = self.active_jobs[job_id]
                    job.status = "completed"
                    job.completion_time = datetime.now()
                    job.output_file = output_file
                    self.completed_jobs[job_id] = job
                    del self.active_jobs[job_id]
                
                print(f"\n🎉 SUCCESS! Output: {output_file}")
                return output_file
            else:
                return None
                
        except Exception as e:
            print(f"❌ Error processing {pdf_path.name}: {e}")
            return None
    
    def wait_for_completion(self, job_id: str, max_wait_time: int = 3600) -> bool:
        """Wait for job completion with enhanced status display"""
        
        start_time = time.time()
        last_status = None
        last_detailed_update = 0
        
        while True:
            try:
                # Get basic status
                status_data = self.check_job_status(job_id)
                if not status_data:
                    time.sleep(self.poll_interval)
                    continue
                
                current_status = status_data.get('status')
                
                # Show status changes
                if current_status != last_status:
                    if current_status == 'queued':
                        queue_pos = status_data.get('queue_position', 'Unknown')
                        print(f"⏸️  Status: Queued (position: {queue_pos})")
                    elif current_status == 'processing':
                        thread_id = status_data.get('thread_id', 'Unknown')
                        gpu_slot = status_data.get('gpu_slot', 'Unknown')
                        print(f"🔄 Status: Processing (Thread {thread_id}, GPU slot {gpu_slot})")
                    elif current_status == 'completed':
                        pages = status_data.get('pages_processed', 'Unknown')
                        processing_time = status_data.get('processing_time_seconds', 'Unknown')
                        file_count = status_data.get('file_count', 'Unknown')
                        storage_size = status_data.get('storage_size_mb', 'Unknown')
                        downloads_remaining = status_data.get('downloads_remaining', 'Unknown')
                        
                        print(f"✅ Status: Completed!")
                        print(f"   📊 {pages} pages processed in {processing_time}s")
                        print(f"   📁 {file_count} files created ({storage_size} MB)")
                        print(f"   📥 Downloads remaining: {downloads_remaining}")
                        return True
                    elif current_status == 'failed':
                        error_msg = status_data.get('error_message', 'Unknown error')
                        print(f"❌ Status: Failed - {error_msg}")
                        return False
                    
                    last_status = current_status
                
                # Show detailed progress every 30 seconds for processing jobs
                elapsed = time.time() - start_time
                if (current_status == 'processing' and 
                    elapsed - last_detailed_update > 30):
                    
                    detailed = self.check_job_status(job_id, detailed=True)
                    if detailed:
                        processing_info = detailed.get('processing_info', {})
                        elapsed_processing = processing_info.get('elapsed_seconds', 0)
                        print(f"🔄 Still processing... ({elapsed_processing}s elapsed, thread {detailed.get('worker_info', {}).get('thread_id', '?')})")
                    
                    last_detailed_update = elapsed
                
                # Check timeout
                if elapsed > max_wait_time:
                    print(f"⏰ Timeout: Processing took longer than {max_wait_time/60:.1f} minutes")
                    return False
                
                time.sleep(self.poll_interval)
                
            except KeyboardInterrupt:
                print(f"\n❌ Process interrupted by user")
                return False
            except Exception as e:
                print(f"⚠️  Error checking status: {e}")
                time.sleep(self.poll_interval * 2)
    
    def process_folder_smart_with_retry(self, folder_path: str, auto_mode: bool = False, **kwargs):
        """Smart batch processing with retry system for failed jobs"""
        
        folder = Path(folder_path)
        if not folder.exists() or not folder.is_dir():
            raise ValueError(f"Invalid folder: {folder_path}")
        
        # Step 1: Scan and categorize PDFs
        categorized = self.scan_and_categorize_pdfs(
            folder, 
            kwargs.get('output_format', 'markdown'), 
            kwargs.get('download_all', False)
        )
        
        unprocessed_files = categorized['unprocessed']
        already_processed = categorized['already_processed']
        invalid_files = categorized['invalid']
        
        # Show scan results
        print(f"\n📊 SCAN RESULTS:")
        print(f"   📄 Total PDFs found: {len(categorized['all_pdfs'])}")
        print(f"   ✅ Already processed: {len(already_processed)}")
        print(f"   📝 Need processing: {len(unprocessed_files)}")
        print(f"   ❌ Invalid/unreadable: {len(invalid_files)}")
        
        if invalid_files:
            print(f"\n❌ Invalid files found:")
            for pdf_path in invalid_files[:5]:
                print(f"   ❌ {pdf_path.name}")
            if len(invalid_files) > 5:
                print(f"   ... and {len(invalid_files) - 5} more")
        
        if not unprocessed_files:
            print(f"\n🎉 All valid PDFs have already been processed!")
            return
        
        # Ask for processing mode if not auto
        if not auto_mode:
            auto_mode = self._ask_processing_mode()
        
        if auto_mode:
            print(f"\n⚡ AUTOMATIC BATCH PROCESSING WITH RETRY SYSTEM")
            print(f"🚀 Processing {len(unprocessed_files)} PDFs with smart batching...")
            print("="*60)
        
        try:
            # Step 2: Process unprocessed files with smart batching
            failed_pdfs = self._smart_batch_process_with_retry(unprocessed_files, auto_mode, **kwargs)
            
            # Step 3: Retry failed PDFs if any
            if failed_pdfs:
                self._retry_failed_pdfs(failed_pdfs, **kwargs)
            
            # Step 4: Final comprehensive summary
            self._show_comprehensive_summary(categorized, invalid_files)
            
        except KeyboardInterrupt:
            print(f"\n❌ Batch processing interrupted by user")
            self._show_comprehensive_summary(categorized, invalid_files)
    
    def _smart_batch_process_with_retry(self, pdf_files: List[Path], auto_mode: bool, **kwargs) -> List[Path]:
        """Process PDFs with intelligent sequential batching and collect failed ones"""
        
        print(f"📊 Processing strategy: Sequential batches of 3 PDFs")
        print(f"   📝 Strategy: Upload 3 → Wait for completion → Download → Repeat")
        print("=" * 60)
        
        batch_size = 3
        total_files = len(pdf_files)
        completed_count = 0
        failed_pdfs = []  # Collect failed PDFs for retry
        
        # Process files in batches of 3
        for batch_start in range(0, total_files, batch_size):
            batch_end = min(batch_start + batch_size, total_files)
            current_batch = pdf_files[batch_start:batch_end]
            batch_num = (batch_start // batch_size) + 1
            total_batches = (total_files + batch_size - 1) // batch_size
            
            print(f"\n🚀 BATCH {batch_num}/{total_batches}: Processing {len(current_batch)} PDFs")
            print("-" * 50)
            
            # Phase 1: Upload current batch
            print(f"📤 Uploading batch {batch_num}...")
            uploaded_jobs = []
            upload_failed_pdfs = []
            
            for i, pdf_path in enumerate(current_batch, 1):
                size_mb = pdf_path.stat().st_size / (1024 * 1024)
                print(f"   📤 [{i}/{len(current_batch)}] Uploading: {pdf_path.name} ({size_mb:.1f} MB)")
                
                job_id = self.upload_pdf(pdf_path, **kwargs)
                if job_id:
                    uploaded_jobs.append(job_id)
                    print(f"      ✅ Job created: {job_id}")
                else:
                    print(f"      ❌ Upload failed")
                    upload_failed_pdfs.append(pdf_path)
                    # Mark as failed with upload stage
                    fake_job_id = f"upload_failed_{int(time.time())}_{i}"
                    job = JobInfo(
                        job_id=fake_job_id,
                        pdf_path=pdf_path,
                        status="failed",
                        error_message="Upload failed",
                        failure_stage="upload"
                    )
                    self.failed_jobs[fake_job_id] = job
                
                # Small delay between uploads to prevent overwhelming server
                if i < len(current_batch):
                    time.sleep(1)
            
            # Add upload failed PDFs to main failed list
            failed_pdfs.extend(upload_failed_pdfs)
            
            if not uploaded_jobs:
                print(f"❌ No files uploaded successfully in batch {batch_num}")
                continue
            
            print(f"✅ Batch {batch_num}: {len(uploaded_jobs)}/{len(current_batch)} files uploaded successfully")
            
            # Phase 2: Wait for all jobs in this batch to complete
            print(f"⏳ Waiting for batch {batch_num} to complete...")
            batch_failed_pdfs = self._wait_for_batch_completion_with_tracking(uploaded_jobs)
            failed_pdfs.extend(batch_failed_pdfs)
            
            # Phase 3: Download all completed jobs in this batch
            print(f"📥 Downloading batch {batch_num} results...")
            download_failed_pdfs = self._download_batch_results(uploaded_jobs, **kwargs)
            failed_pdfs.extend(download_failed_pdfs)
            
            # Count completed jobs
            batch_completed = len([job_id for job_id in uploaded_jobs if job_id in self.completed_jobs])
            completed_count += batch_completed
            
            # Show batch summary
            batch_failed = len(current_batch) - batch_completed
            print(f"📊 Batch {batch_num} summary: {batch_completed} completed, {batch_failed} failed")
            
            # Brief pause before next batch (except for last batch)
            if batch_end < total_files:
                print(f"⏸️  Pausing 3 seconds before next batch...")
                time.sleep(3)
        
        # Initial processing summary
        total_failed = len(failed_pdfs)
        print(f"\n{'='*60}")
        print("📊 INITIAL PROCESSING SUMMARY")
        print(f"{'='*60}")
        print(f"📄 Total PDFs processed: {total_files}")
        print(f"✅ Successfully completed: {completed_count}")
        print(f"❌ Failed (will retry): {total_failed}")
        print(f"📊 Success rate: {(completed_count/total_files)*100:.1f}%")
        
        if failed_pdfs:
            print(f"\n❌ Failed files (will be retried):")
            for pdf_path in failed_pdfs[:10]:
                print(f"   ❌ {pdf_path.name}")
            if len(failed_pdfs) > 10:
                print(f"   ... and {len(failed_pdfs) - 10} more")
        
        print(f"{'='*60}")
        
        return failed_pdfs
    
    def _wait_for_batch_completion_with_tracking(self, job_ids: List[str]) -> List[Path]:
        """Wait for all jobs in a batch to complete and track failed ones"""
        
        pending_jobs = set(job_ids)
        completed_jobs = set()
        failed_pdfs = []
        
        print(f"   👁️  Monitoring {len(pending_jobs)} jobs in this batch...")
        
        last_status_update = time.time()
        
        while pending_jobs:
            try:
                # Check status of each pending job
                for job_id in list(pending_jobs):
                    status = self.check_job_status(job_id)
                    if not status:
                        continue
                    
                    job_status = status.get('status')
                    
                    if job_status == 'completed':
                        pending_jobs.remove(job_id)
                        completed_jobs.add(job_id)
                        if job_id in self.active_jobs:
                            job_info = self.active_jobs[job_id]
                            pages = status.get('pages_processed', '?')
                            processing_time = status.get('processing_time_seconds', '?')
                            print(f"      ✅ {job_info.pdf_path.name} completed ({pages} pages, {processing_time}s)")
                    
                    elif job_status == 'failed':
                        pending_jobs.remove(job_id)
                        if job_id in self.active_jobs:
                            job_info = self.active_jobs[job_id]
                            error_msg = status.get('error_message', 'Unknown error')
                            print(f"      ❌ {job_info.pdf_path.name} failed: {error_msg}")
                            
                            # Mark for retry
                            failed_pdfs.append(job_info.pdf_path)
                            job_info.status = "failed"
                            job_info.error_message = error_msg
                            job_info.failure_stage = "processing"
                            self.failed_jobs[job_id] = job_info
                            del self.active_jobs[job_id]
                
                # Show progress update every 15 seconds
                current_time = time.time()
                if current_time - last_status_update > 15:
                    if pending_jobs:
                        print(f"      🔄 Still processing {len(pending_jobs)} jobs in this batch...")
                        
                        # Show which jobs are still processing
                        for job_id in list(pending_jobs)[:3]:  # Show first 3
                            if job_id in self.active_jobs:
                                job_info = self.active_jobs[job_id]
                                status = self.check_job_status(job_id)
                                if status:
                                    current_status = status.get('status', 'unknown')
                                    if current_status == 'processing':
                                        thread_id = status.get('thread_id', '?')
                                        print(f"         🔄 {job_info.pdf_path.name} (thread {thread_id})")
                                    elif current_status == 'queued':
                                        queue_pos = status.get('queue_position', '?')
                                        print(f"         ⏳ {job_info.pdf_path.name} (queue pos: {queue_pos})")
                        
                        if len(pending_jobs) > 3:
                            print(f"         ... and {len(pending_jobs) - 3} more")
                    
                    last_status_update = current_time
                
                time.sleep(self.poll_interval)
                
            except KeyboardInterrupt:
                print(f"\n❌ Batch monitoring interrupted by user")
                break
        
        print(f"   ✅ Batch completed: {len(completed_jobs)} successful, {len(failed_pdfs)} failed")
        return failed_pdfs
    
    def _download_batch_results(self, job_ids: List[str], **kwargs) -> List[Path]:
        """Download results for completed jobs and track download failures"""
        
        download_failed_pdfs = []
        
        for job_id in job_ids:
            if job_id in self.active_jobs:
                job_info = self.active_jobs[job_id]
                
                # Check if job completed successfully
                status = self.check_job_status(job_id)
                if status and status.get('status') == 'completed':
                    print(f"   📥 Downloading: {job_info.pdf_path.name}")
                    
                    output_file = self.download_job_result(
                        job_id, job_info.pdf_path,
                        kwargs.get('output_format', 'markdown'),
                        kwargs.get('download_all', False),
                        kwargs.get('keep_alive', False)
                    )
                    
                    if output_file:
                        job_info.status = "completed"
                        job_info.completion_time = datetime.now()
                        job_info.output_file = output_file
                        self.completed_jobs[job_id] = job_info
                        del self.active_jobs[job_id]
                        print(f"      ✅ Completed: {job_info.pdf_path.name}")
                    else:
                        print(f"      ❌ Download failed: {job_info.pdf_path.name}")
                        download_failed_pdfs.append(job_info.pdf_path)
                        job_info.status = "failed"
                        job_info.error_message = "Download failed"
                        job_info.failure_stage = "download"
                        self.failed_jobs[job_id] = job_info
                        del self.active_jobs[job_id]
        
        return download_failed_pdfs
    
    def _retry_failed_pdfs(self, failed_pdfs: List[Path], **kwargs):
        """Retry processing failed PDFs one by one"""
        
        if not failed_pdfs:
            return
        
        print(f"\n🔄 RETRY PHASE: Processing {len(failed_pdfs)} failed PDFs")
        print("="*60)
        print("📝 Strategy: Process failed PDFs one by one with detailed monitoring")
        print("="*60)
        
        retry_completed = 0
        retry_still_failed = 0
        
        for i, pdf_path in enumerate(failed_pdfs, 1):
            print(f"\n🔄 RETRY {i}/{len(failed_pdfs)}: {pdf_path.name}")
            print("-" * 40)
            
            # Check if it was processed successfully since the failure (edge case)
            is_processed, reason = self.check_already_processed(
                pdf_path, 
                kwargs.get('output_format', 'markdown'), 
                kwargs.get('download_all', False)
            )
            
            if is_processed:
                print(f"   ✅ Already processed: {reason}")
                retry_completed += 1
                continue
            
            try:
                # Find the existing failed job info for retry count
                existing_job = None
                for job_id, job_info in self.failed_jobs.items():
                    if job_info.pdf_path == pdf_path:
                        existing_job = job_info
                        break
                
                retry_count = existing_job.retry_count + 1 if existing_job else 1
                max_retries = self.max_retries
                
                print(f"   🔄 Retry attempt {retry_count}/{max_retries}")
                if existing_job and existing_job.failure_stage:
                    print(f"   ❌ Previous failure at: {existing_job.failure_stage}")
                if existing_job and existing_job.error_message:
                    print(f"   💬 Previous error: {existing_job.error_message}")
                
                # Process with detailed monitoring
                result = self._process_single_pdf_with_retry_tracking(pdf_path, retry_count, **kwargs)
                
                if result:
                    retry_completed += 1
                    print(f"   🎉 RETRY SUCCESS: {pdf_path.name}")
                    
                    # Remove from failed jobs if it was there
                    if existing_job:
                        for job_id in list(self.failed_jobs.keys()):
                            if self.failed_jobs[job_id].pdf_path == pdf_path:
                                del self.failed_jobs[job_id]
                                break
                else:
                    retry_still_failed += 1
                    print(f"   ❌ RETRY FAILED: {pdf_path.name}")
                    
                    # Update retry count
                    if existing_job:
                        existing_job.retry_count = retry_count
                
            except Exception as e:
                retry_still_failed += 1
                print(f"   ❌ RETRY ERROR: {pdf_path.name} - {e}")
            
            # Brief pause between retries
            if i < len(failed_pdfs):
                print(f"   ⏸️  Brief pause before next retry...")
                time.sleep(2)
        
        # Retry summary
        print(f"\n{'='*60}")
        print("📊 RETRY PHASE SUMMARY")
        print(f"{'='*60}")
        print(f"🔄 Total retries attempted: {len(failed_pdfs)}")
        print(f"✅ Successfully recovered: {retry_completed}")
        print(f"❌ Still failed: {retry_still_failed}")
        if failed_pdfs:
            print(f"📊 Retry success rate: {(retry_completed/len(failed_pdfs))*100:.1f}%")
        print(f"{'='*60}")
    
    def _process_single_pdf_with_retry_tracking(self, pdf_path: Path, retry_count: int, **kwargs) -> Optional[Path]:
        """Process a single PDF with retry tracking"""
        
        try:
            print(f"      📤 Uploading...")
            job_id = self.upload_pdf(pdf_path, **kwargs)
            if not job_id:
                return None
            
            print(f"      ⏳ Monitoring processing...")
            if not self.wait_for_completion(job_id):
                return None
            
            print(f"      📥 Downloading...")
            output_file = self.download_job_result(
                job_id, pdf_path, 
                kwargs.get('output_format', 'markdown'),
                kwargs.get('download_all', False),
                kwargs.get('keep_alive', False)
            )
            
            if output_file:
                # Update job tracking
                if job_id in self.active_jobs:
                    job = self.active_jobs[job_id]
                    job.status = "completed"
                    job.completion_time = datetime.now()
                    job.output_file = output_file
                    job.retry_count = retry_count
                    self.completed_jobs[job_id] = job
                    del self.active_jobs[job_id]
                
                return output_file
            else:
                return None
                
        except Exception as e:
            print(f"      ❌ Exception during retry: {e}")
            return None
    
    def _show_comprehensive_summary(self, categorized: Dict, invalid_files: List[Path]):
        """Show comprehensive final summary"""
        
        total_pdfs = len(categorized['all_pdfs'])
        already_processed = len(categorized['already_processed'])
        total_completed = len(self.completed_jobs)
        total_failed = len(self.failed_jobs)
        total_invalid = len(invalid_files)
        total_skipped = already_processed
        
        print(f"\n{'='*70}")
        print("📊 COMPREHENSIVE PROCESSING SUMMARY")
        print(f"{'='*70}")
        print(f"📄 Total PDFs found: {total_pdfs}")
        print(f"✅ Already processed (skipped): {total_skipped}")
        print(f"❌ Invalid/unreadable: {total_invalid}")
        print(f"📝 Attempted processing: {total_pdfs - total_skipped - total_invalid}")
        print("")
        print(f"🎉 Successfully completed: {total_completed}")
        print(f"❌ Finally failed: {total_failed}")
        
        if total_pdfs - total_skipped - total_invalid > 0:
            success_rate = (total_completed / (total_pdfs - total_skipped - total_invalid)) * 100
            print(f"📊 Processing success rate: {success_rate:.1f}%")
        
        # Show skipped files summary
        if self.skipped_jobs:
            print(f"\n⏭️  SKIPPED FILES ({len(self.skipped_jobs)}):")
            for pdf_path, reason in list(self.skipped_jobs.items())[:5]:
                filename = Path(pdf_path).name
                print(f"   ⏭️  {filename} - {reason}")
            if len(self.skipped_jobs) > 5:
                print(f"   ... and {len(self.skipped_jobs) - 5} more")
        
        # Show completed files
        if self.completed_jobs:
            print(f"\n✅ COMPLETED FILES ({len(self.completed_jobs)}):")
            for job_id, job in list(self.completed_jobs.items())[:10]:
                if job.output_file:
                    processing_time = ""
                    if job.upload_time and job.completion_time:
                        total_time = (job.completion_time - job.upload_time).total_seconds()
                        processing_time = f" ({total_time:.0f}s total)"
                    
                    retry_info = f" [retry #{job.retry_count}]" if job.retry_count > 0 else ""
                    print(f"   ✅ {job.pdf_path.name} → {job.output_file.name}{processing_time}{retry_info}")
            
            if len(self.completed_jobs) > 10:
                print(f"   ... and {len(self.completed_jobs) - 10} more")
        
        # Show finally failed files
        if self.failed_jobs:
            print(f"\n❌ FINALLY FAILED FILES ({len(self.failed_jobs)}):")
            for job_id, job in list(self.failed_jobs.items())[:10]:
                retry_info = f" [tried {job.retry_count + 1} times]" if job.retry_count > 0 else ""
                failure_info = f" at {job.failure_stage}" if job.failure_stage else ""
                error_info = f": {job.error_message}" if job.error_message else ""
                print(f"   ❌ {job.pdf_path.name}{retry_info} - Failed{failure_info}{error_info}")
            
            if len(self.failed_jobs) > 10:
                print(f"   ... and {len(self.failed_jobs) - 10} more")
        
        # Show invalid files
        if invalid_files:
            print(f"\n🚫 INVALID FILES ({len(invalid_files)}):")
            for pdf_path in invalid_files[:5]:
                print(f"   🚫 {pdf_path.name}")
            if len(invalid_files) > 5:
                print(f"   ... and {len(invalid_files) - 5} more")
        
        print(f"{'='*70}")
    
    def monitor_dashboard(self):
        """Real-time monitoring dashboard"""
        
        print("🔥 MARKER SERVER DASHBOARD")
        print("Press Ctrl+C to exit")
        print("=" * 60)
        
        try:
            while True:
                # Clear screen
                os.system('clear' if os.name == 'posix' else 'cls')
                
                print("🔥 ENHANCED MARKER SERVER DASHBOARD")
                print("=" * 60)
                print(f"🕐 Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"📡 Server: {self.server_url}")
                if self.session_id:
                    print(f"🎯 Session: {self.session_id}")
                print("=" * 60)
                
                try:
                    # Get server statistics
                    queue_response = requests.get(self.queue_url, timeout=10)
                    if queue_response.status_code == 200:
                        queue_stats = queue_response.json()
                        
                        print("📊 QUEUE STATUS:")
                        print(f"   ⏳ Queued: {queue_stats['queue']['queued']}")
                        print(f"   🔄 Processing: {queue_stats['queue']['processing']}")
                        print(f"   ✅ Completed today: {queue_stats['queue']['completed_today']}")
                        print(f"   ❌ Failed today: {queue_stats['queue']['failed_today']}")
                    
                    # Get worker information
                    workers_response = requests.get(self.workers_url, timeout=10)
                    if workers_response.status_code == 200:
                        workers_stats = workers_response.json()
                        
                        print(f"\n🔧 WORKER STATUS:")
                        print(f"   🎮 GPU slots available: {workers_stats['gpu_coordination']['available_slots']}/{workers_stats['gpu_coordination']['max_concurrent']}")
                        
                        for worker_id, worker_info in workers_stats['workers'].items():
                            status_icon = "🔄" if worker_info['status'] == 'active' else "💤"
                            print(f"   {status_icon} {worker_id}: {worker_info['status']} ({worker_info['active_jobs']} jobs)")
                    
                    # Get storage information
                    storage_response = requests.get(self.storage_url, timeout=10)
                    if storage_response.status_code == 200:
                        storage_stats = storage_response.json()
                        
                        print(f"\n💾 STORAGE STATUS:")
                        print(f"   📁 Total size: {storage_stats['totals']['total_size_mb']:.1f} MB")
                        print(f"   📄 Total files: {storage_stats['totals']['total_files']}")
                        print(f"   📥 Uploads: {storage_stats['directories']['uploads']['file_count']} files ({storage_stats['directories']['uploads']['size_mb']:.1f} MB)")
                        print(f"   ✅ Completed: {storage_stats['directories']['completed']['file_count']} files ({storage_stats['directories']['completed']['size_mb']:.1f} MB)")
                    
                    # Show session jobs if available
                    if self.session_id:
                        session_response = requests.get(f"{self.session_url}/{self.session_id}/jobs", timeout=10)
                        if session_response.status_code == 200:
                            session_data = session_response.json()
                            jobs = session_data.get('jobs', [])
                            
                            print(f"\n🎯 YOUR SESSION JOBS ({len(jobs)}):")
                            if jobs:
                                for job in jobs[:10]:  # Show first 10
                                    status_icon = {
                                        'queued': '⏳',
                                        'processing': '🔄',
                                        'completed': '✅',
                                        'failed': '❌'
                                    }.get(job['status'], '❓')
                                    
                                    filename = job['original_filename'][:30] + "..." if len(job['original_filename']) > 30 else job['original_filename']
                                    print(f"   {status_icon} {filename} | {job['status']}")
                                    
                                    if job['status'] == 'processing':
                                        thread_id = job.get('thread_id', '?')
                                        print(f"      🔧 Worker thread {thread_id}")
                                    elif job['status'] == 'completed':
                                        downloads = job.get('download_count', 0)
                                        remaining = job.get('downloads_remaining', 0)
                                        print(f"      📥 Downloads: {downloads} (remaining: {remaining})")
                                
                                if len(jobs) > 10:
                                    print(f"   ... and {len(jobs) - 10} more jobs")
                            else:
                                print("   (No jobs in this session)")
                
                except requests.RequestException as e:
                    print(f"⚠️  Connection error: {e}")
                except Exception as e:
                    print(f"❌ Dashboard error: {e}")
                
                print(f"\n💡 Press Ctrl+C to exit dashboard")
                print("=" * 60)
                
                time.sleep(self.dashboard_refresh)
                
        except KeyboardInterrupt:
            print(f"\n👋 Dashboard closed")
    
    def cleanup_session(self) -> bool:
        """Cleanup current session on server"""
        if not self.session_id:
            print("⚠️  No active session to cleanup")
            return False
        
        try:
            print(f"🧹 Cleaning up session {self.session_id}...")
            response = requests.delete(f"{self.session_url}/{self.session_id}", timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                jobs_cleaned = result.get('jobs_cleaned', 0)
                print(f"✅ Session cleanup completed. {jobs_cleaned} jobs cleaned from server.")
                
                # Clean up local state
                self.session_id = None
                self.active_jobs.clear()
                if self.state_file.exists():
                    self.state_file.unlink()
                
                return True
            else:
                print(f"⚠️  Session cleanup failed: HTTP {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Session cleanup error: {e}")
            return False
    
    def extend_job_retention(self, job_id: str, days: int = 7) -> bool:
        """Extend retention period for a specific job"""
        try:
            response = requests.post(
                f"{self.server_url}/jobs/{job_id}/extend-retention",
                params={'days': days},
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Extended retention for job {job_id} to {days} days")
                return True
            else:
                print(f"❌ Failed to extend retention: HTTP {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error extending retention: {e}")
            return False
    
    def download_existing_job(self, job_id: str, output_format: str = "markdown", 
                             download_all: bool = False) -> bool:
        """Download an existing job by ID"""
        
        print(f"📥 Downloading existing job: {job_id}")
        
        # Check job status first
        status = self.check_job_status(job_id, detailed=True)
        if not status:
            return False
        
        if status['status'] != 'completed':
            print(f"❌ Job is not completed (status: {status['status']})")
            return False
        
        # Get original filename for output path
        original_filename = status['original_filename']
        output_path = Path.cwd() / original_filename
        
        # Download the file
        result = self.download_job_result(
            job_id, output_path, output_format, download_all
        )
        
        if result:
            print(f"✅ Successfully downloaded: {result}")
            return True
        else:
            print(f"❌ Download failed")
            return False
    
    def _find_pdf_files(self, folder: Path) -> List[Path]:
        """Find all PDF files in folder"""
        pdf_files = list(folder.glob("*.pdf")) + list(folder.glob("*.PDF"))
        return sorted(list(set(pdf_files)))
    
    def _is_already_processed(self, pdf_path: Path, output_format: str, download_all: bool) -> bool:
        """Legacy method - use check_already_processed instead"""
        is_processed, _ = self.check_already_processed(pdf_path, output_format, download_all)
        return is_processed
    
    def _ask_processing_mode(self) -> bool:
        """Ask user for processing mode"""
        print("\n🤖 PROCESSING MODE SELECTION")
        print("=" * 50)
        print("Choose processing mode:")
        print("1. ⚡ Automatic - Process all unprocessed PDFs without asking")
        print("2. 🎛️  Interactive - Ask for confirmation for each PDF")
        print("=" * 50)
        
        while True:
            choice = input("\nSelect mode (1 for automatic, 2 for interactive): ").strip()
            
            if choice == '1':
                return True  # Automatic mode
            elif choice == '2':
                return False  # Interactive mode
            else:
                print("❌ Invalid choice. Please enter '1' or '2'")
    
    def _ask_user_confirmation(self, pdf_path: Path, current_index: int, total_count: int) -> str:
        """Ask user whether to process this PDF"""
        print(f"\n{'='*60}")
        print(f"📋 PDF {current_index}/{total_count}")
        print(f"📄 File: {pdf_path.name}")
        print(f"📂 Location: {pdf_path.parent}")
        print(f"📊 Size: {pdf_path.stat().st_size / 1024 / 1024:.1f} MB")
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
    
    def process_folder_interactive(self, folder_path: str, **kwargs):
        """Interactive folder processing with enhanced skip logic"""
        
        folder = Path(folder_path)
        
        # Scan and categorize PDFs
        categorized = self.scan_and_categorize_pdfs(
            folder, 
            kwargs.get('output_format', 'markdown'), 
            kwargs.get('download_all', False)
        )
        
        unprocessed_files = categorized['unprocessed']
        
        if not unprocessed_files:
            print("🎉 All PDFs have already been processed!")
            self._show_comprehensive_summary(categorized, categorized['invalid'])
            return
        
        print(f"\n🎛️  INTERACTIVE PROCESSING MODE")
        print(f"📋 Will process {len(unprocessed_files)} unprocessed PDF(s)")
        print("=" * 60)
        
        processed_count = 0
        skipped_count = 0
        failed_count = 0
        skip_all_remaining = False
        failed_pdfs = []
        
        for i, pdf_path in enumerate(unprocessed_files, 1):
            try:
                if skip_all_remaining:
                    print(f"⏭️  Skipping {pdf_path.name} (skip all remaining)")
                    skipped_count += 1
                    continue
                
                # Ask user for confirmation
                user_choice = self._ask_user_confirmation(pdf_path, i, len(unprocessed_files))
                
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
                    print(f"\n🚀 Processing {pdf_path.name}...")
                    
                    result = self.process_single_pdf(str(pdf_path), **kwargs)
                    
                    if result:
                        processed_count += 1
                        print(f"✅ Successfully processed: {pdf_path.name}")
                    else:
                        failed_count += 1
                        failed_pdfs.append(pdf_path)
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
                failed_pdfs.append(pdf_path)
                
                # Ask if user wants to continue
                while True:
                    continue_choice = input("\n🤔 Continue with next PDF? (y)es / (n)o: ").lower().strip()
                    if continue_choice in ['y', 'yes']:
                        break
                    elif continue_choice in ['n', 'no']:
                        print("👋 Exiting...")
                        return
                    else:
                        print("❌ Invalid choice. Please enter 'y' or 'n'")
        
        # Retry failed PDFs if any
        if failed_pdfs:
            print(f"\n🔄 Found {len(failed_pdfs)} failed PDFs. Would you like to retry them?")
            while True:
                retry_choice = input("🤔 Retry failed PDFs? (y)es / (n)o: ").lower().strip()
                if retry_choice in ['y', 'yes']:
                    self._retry_failed_pdfs(failed_pdfs, **kwargs)
                    break
                elif retry_choice in ['n', 'no']:
                    print("⏭️  Skipping retry phase")
                    break
                else:
                    print("❌ Invalid choice. Please enter 'y' or 'n'")
        
        # Final summary
        print(f"\n{'='*60}")
        print("📊 INTERACTIVE PROCESSING SUMMARY")
        print(f"{'='*60}")
        print(f"📄 Total PDFs found: {len(categorized['all_pdfs'])}")
        print(f"✅ Already processed: {len(categorized['already_processed'])}")
        print(f"📝 Attempted: {len(unprocessed_files)}")
        print(f"🎉 Successfully processed: {processed_count}")
        print(f"⏭️  Manually skipped: {skipped_count}")
        print(f"❌ Failed: {failed_count}")
        print(f"{'='*60}")
        
        self._show_comprehensive_summary(categorized, categorized['invalid'])

def setup_signal_handlers(parser_instance):
    """Setup signal handlers for graceful shutdown"""
    def signal_handler(signum, frame):
        print(f"\n🛑 Received signal {signum}. Performing graceful shutdown...")
        
        if parser_instance.session_id and hasattr(parser_instance, '_should_cleanup_session'):
            if parser_instance._should_cleanup_session:
                print("🧹 Cleaning up session...")
                parser_instance.cleanup_session()
        
        print("👋 Goodbye!")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

def main():
    parser = argparse.ArgumentParser(
        description="Enhanced Marker PDF Parser CLI with smart skip logic and retry system",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Enhanced Examples:
  # Basic processing with auto-skip
  python enhanced_marker_cli.py document.pdf
  
  # Custom retention and storage
  python enhanced_marker_cli.py document.pdf --retention 7d --storage-path /project/outputs
  
  # Keep files on server permanently
  python enhanced_marker_cli.py document.pdf --retention never
  
  # Smart batch processing with skip logic and retry
  python enhanced_marker_cli.py --folder ./pdfs --auto --retention immediate
  
  # Batch with session cleanup at end
  python enhanced_marker_cli.py --folder ./pdfs --auto --session-cleanup
  
  # Real-time monitoring dashboard
  python enhanced_marker_cli.py --monitor
  
  # Download existing job
  python enhanced_marker_cli.py --download-only abc12345 --all
  
  # Resume interrupted session
  python enhanced_marker_cli.py --resume
  
  # Interactive folder processing with smart skip
  python enhanced_marker_cli.py --folder ./pdfs --interactive
        """
    )
    
    # Main action group
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument('pdf_path', nargs='?', help='Path to a single PDF file to parse')
    action_group.add_argument('--folder', help='Path to folder containing PDF files to process')
    action_group.add_argument('--monitor', action='store_true', help='Launch real-time monitoring dashboard')
    action_group.add_argument('--download-only', help='Download existing job by ID')
    action_group.add_argument('--resume', action='store_true', help='Resume previous interrupted session')
    
    # Processing mode (for folder processing)
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('--auto', action='store_true', help='Automatic processing (folder mode)')
    mode_group.add_argument('--interactive', action='store_true', help='Interactive processing (folder mode)')
    
    # Server and format options
    parser.add_argument('--server', default='https://mbxsqv2e682vet-8888.proxy.runpod.net/',
                       help='Enhanced Marker server URL')
    parser.add_argument('--format', default='markdown', choices=['markdown', 'json'],
                       help='Output format: markdown or json')
    parser.add_argument('--ocr', action='store_true', help='Force OCR on all pages')
    parser.add_argument('--all', action='store_true', 
                       help='Download complete organized folders with all content')
    
    # Enhanced server options
    parser.add_argument('--storage-path', help='Custom storage location on server')
    parser.add_argument('--retention', choices=['immediate', '24h', '7d', 'never'], 
                       default='24h', help='File retention policy after download')
    parser.add_argument('--max-downloads', type=int, default=3,
                       help='Maximum download attempts before cleanup')
    parser.add_argument('--keep-alive', action='store_true',
                       help='Prevent automatic cleanup after download')
    
    # Session management
    parser.add_argument('--session-cleanup', action='store_true',
                       help='Cleanup session on server when finished')
    parser.add_argument('--extend-retention', type=int, metavar='DAYS',
                       help='Extend retention for download-only job (days)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.auto and not args.folder:
        print("❌ Error: --auto flag can only be used with --folder")
        sys.exit(1)
    
    if args.interactive and not args.folder:
        print("❌ Error: --interactive flag can only be used with --folder")
        sys.exit(1)
    
    if args.session_cleanup and not args.folder:
        print("❌ Error: --session-cleanup flag can only be used with --folder")
        sys.exit(1)
    
    try:
        # Initialize enhanced parser
        pdf_parser = EnhancedMarkerParser(args.server)
        
        # Setup signal handlers
        setup_signal_handlers(pdf_parser)
        pdf_parser._should_cleanup_session = args.session_cleanup
        
        # Test server connection
        if not pdf_parser.test_connection():
            sys.exit(1)
        
        # Handle different modes
        if args.monitor:
            # Real-time monitoring dashboard
            print(f"\n🔥 LAUNCHING MONITORING DASHBOARD")
            print("=" * 50)
            pdf_parser.monitor_dashboard()
            
        elif args.download_only:
            # Download existing job
            print(f"\n📥 DOWNLOAD EXISTING JOB MODE")
            print("=" * 50)
            success = pdf_parser.download_existing_job(
                args.download_only, 
                args.format, 
                args.all
            )
            
            # Extend retention if requested
            if args.extend_retention:
                pdf_parser.extend_job_retention(args.download_only, args.extend_retention)
            
            sys.exit(0 if success else 1)
            
        elif args.resume:
            # Resume previous session
            print(f"\n🔄 RESUME SESSION MODE")
            print("=" * 50)
            
            if pdf_parser._load_session_state():
                print("📊 Monitoring resumed jobs...")
                
                if pdf_parser.active_jobs:
                    job_ids = list(pdf_parser.active_jobs.keys())
                    pdf_parser._monitor_and_download_parallel(job_ids, 
                        output_format=args.format, download_all=args.all, keep_alive=args.keep_alive)
                else:
                    print("✅ No active jobs to resume")
            else:
                print("❌ No session to resume or session expired")
            
        else:
            # Start new session
            pdf_parser.start_session()
            
            # Common processing arguments
            process_kwargs = {
                'output_format': args.format,
                'use_ocr': args.ocr,
                'download_all': args.all,
                'storage_path': args.storage_path,
                'retention': args.retention,
                'max_downloads': args.max_downloads,
                'keep_alive': args.keep_alive
            }
            
            if args.folder:
                # Folder processing mode
                mode_text = ""
                if args.auto:
                    mode_text = " (AUTOMATIC)"
                elif args.interactive:
                    mode_text = " (INTERACTIVE)"
                else:
                    mode_text = " (AUTO-DETECT MODE)"
                
                download_text = " + COMPLETE FOLDERS" if args.all else ""
                print(f"\n🗂️  FOLDER PROCESSING{mode_text}{download_text}")
                print("=" * 60)
                
                if args.interactive:
                    pdf_parser.process_folder_interactive(args.folder, **process_kwargs)
                else:
                    pdf_parser.process_folder_smart_with_retry(args.folder, auto_mode=args.auto, **process_kwargs)
                    
            else:
                # Single file processing mode
                download_text = " + COMPLETE FOLDER" if args.all else ""
                print(f"\n📄 SINGLE FILE PROCESSING ({args.format.upper()}{download_text})")
                print("=" * 60)
                
                output_file = pdf_parser.process_single_pdf(args.pdf_path, **process_kwargs)
                if not output_file:
                    print(f"\n❌ Processing failed!")
                    sys.exit(1)
            
            # Session cleanup if requested
            if args.session_cleanup:
                print(f"\n🧹 Performing session cleanup...")
                pdf_parser.cleanup_session()
        
    except KeyboardInterrupt:
        print("\n❌ Process interrupted by user")
        if 'pdf_parser' in locals() and pdf_parser.session_id and args.session_cleanup:
            print("🧹 Cleaning up session...")
            pdf_parser.cleanup_session()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()