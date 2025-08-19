#!/usr/bin/env python3
"""
Enhanced Local Marker PDF Parser CLI Tool - OPTIMIZED for Persistent Model Server
Features:
- Smart batch sizing based on server capabilities
- Adaptive batch processing for optimized servers
- Dynamic batch size detection
- Enhanced parallel processing
- Server optimization awareness

Usage Examples:
  # Auto-detect optimal batch size
  python enhanced_marker_cli.py --folder ./pdfs --auto
  
  # Force specific batch size
  python enhanced_marker_cli.py --folder ./pdfs --auto --batch-size 8
  
  # Aggressive processing for optimized servers
  python enhanced_marker_cli.py --folder ./pdfs --auto --aggressive
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
    def __init__(self, server_url="https://pjavwu4ljbpcdc-8888.proxy.runpod.net/"):
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
        self.models_url = f"{self.server_url}/models/status"  # NEW: Model status endpoint
        self.health_url = f"{self.server_url}/health"  # NEW: Health endpoint
        
        # OPTIMIZED Configuration - Dynamic batch sizing
        self.default_batch_size = 3  # Conservative default
        self.max_batch_size = 10  # Maximum batch size
        self.adaptive_batch_size = None  # Will be detected from server
        self.server_optimization_level = "unknown"  # Will be detected
        
        self.max_concurrent_uploads = 5  # Increased from 3
        self.max_concurrent_downloads = 8  # Increased from 5
        self.poll_interval = 2  # Reduced from 3 seconds (faster polling)
        self.dashboard_refresh = 3  # Reduced from 5 seconds
        self.max_retries = 2
        
        # Session state file for resume capability
        self.state_file = Path.cwd() / ".marker_cli_session.json"
        
        print(f"🔗 Enhanced Marker CLI initialized (OPTIMIZED)")
        print(f"📡 Server: {self.server_url}")
    
    def detect_server_optimization(self) -> Dict:
        """Detect server optimization level and capabilities"""
        try:
            print("🔍 Detecting server optimization level...")
            
            # Check if server has optimization endpoints
            optimization_info = {
                "has_persistent_models": False,
                "optimal_batch_size": self.default_batch_size,
                "server_type": "standard",
                "performance_boost": "none"
            }
            
            # Try to get model status (optimized servers have this)
            try:
                models_response = requests.get(self.models_url, timeout=10)
                if models_response.status_code == 200:
                    model_info = models_response.json()
                    optimization_info["has_persistent_models"] = model_info.get("models_loaded", False)
                    optimization_info["server_type"] = "optimized"
                    
                    if model_info.get("models_loaded"):
                        print("🚀 OPTIMIZED SERVER DETECTED!")
                        print(f"   ✅ Persistent models loaded")
                        print(f"   ⚡ Performance boost: {model_info.get('performance_improvement', 'Unknown')}")
                        optimization_info["performance_boost"] = "40% faster"
                        
                        # Calculate optimal batch size based on server capabilities
                        optimization_info["optimal_batch_size"] = self._calculate_optimal_batch_size(model_info)
                    else:
                        print("⚠️  Optimized server but models not loaded")
                        optimization_info["optimal_batch_size"] = self.default_batch_size
                
            except requests.RequestException:
                # Fallback to health endpoint
                try:
                    health_response = requests.get(self.health_url, timeout=5)
                    if health_response.status_code == 200:
                        health_info = health_response.json()
                        if health_info.get("optimization", {}).get("persistent_models"):
                            optimization_info["has_persistent_models"] = True
                            optimization_info["server_type"] = "optimized"
                            optimization_info["performance_boost"] = health_info.get("optimization", {}).get("performance_boost", "unknown")
                except requests.RequestException:
                    pass
            
            # Get worker information for batch sizing
            try:
                workers_response = requests.get(self.workers_url, timeout=10)
                if workers_response.status_code == 200:
                    workers_info = workers_response.json()
                    max_workers = workers_info.get("total_workers", 3)
                    gpu_slots = workers_info.get("gpu_coordination", {}).get("max_concurrent", 1)
                    
                    # Calculate batch size based on workers and optimization
                    if optimization_info["has_persistent_models"]:
                        # Optimized servers can handle larger batches
                        optimization_info["optimal_batch_size"] = min(max_workers * 2, self.max_batch_size)
                    else:
                        # Standard servers use conservative batching
                        optimization_info["optimal_batch_size"] = min(max_workers, 5)
                    
                    print(f"   🔧 Workers: {max_workers}, GPU slots: {gpu_slots}")
                    print(f"   📊 Optimal batch size: {optimization_info['optimal_batch_size']}")
                    
            except requests.RequestException:
                pass
            
            self.server_optimization_level = optimization_info["server_type"]
            self.adaptive_batch_size = optimization_info["optimal_batch_size"]
            
            return optimization_info
            
        except Exception as e:
            print(f"⚠️  Could not detect server optimization: {e}")
            self.server_optimization_level = "unknown"
            self.adaptive_batch_size = self.default_batch_size
            return {
                "has_persistent_models": False,
                "optimal_batch_size": self.default_batch_size,
                "server_type": "unknown",
                "performance_boost": "unknown"
            }
    
    def _calculate_optimal_batch_size(self, model_info: Dict) -> int:
        """Calculate optimal batch size based on server capabilities"""
        try:
            # Get total PDFs processed (indicates server stability)
            total_processed = model_info.get("total_pdfs_processed", 0)
            
            # Base batch size on server experience and capabilities
            if total_processed > 50:
                # Experienced server, can handle larger batches
                base_batch = 8
            elif total_processed > 10:
                # Some experience, moderate batches
                base_batch = 6
            else:
                # New server, conservative batches
                base_batch = 4
            
            # Cap at maximum
            return min(base_batch, self.max_batch_size)
            
        except Exception:
            return self.default_batch_size
    
    def get_optimal_batch_size(self, user_specified: Optional[int] = None, aggressive: bool = False) -> int:
        """Get the optimal batch size for processing"""
        if user_specified:
            # User override
            batch_size = min(user_specified, self.max_batch_size)
            print(f"📊 Using user-specified batch size: {batch_size}")
            return batch_size
        
        if aggressive and self.server_optimization_level == "optimized":
            # Aggressive mode for optimized servers
            batch_size = min(self.adaptive_batch_size * 2, self.max_batch_size)
            print(f"🚀 Aggressive mode for optimized server: batch size {batch_size}")
            return batch_size
        
        if self.adaptive_batch_size:
            # Use detected optimal size
            print(f"🎯 Using detected optimal batch size: {self.adaptive_batch_size}")
            return self.adaptive_batch_size
        
        # Fallback to default
        print(f"📊 Using default batch size: {self.default_batch_size}")
        return self.default_batch_size
    
    def check_already_processed(self, pdf_path: Path, output_format: str, download_all: bool) -> Tuple[bool, str]:
        """Enhanced check for already processed files"""
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
        """Scan folder and categorize PDFs into processed, unprocessed, and invalid"""
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
                
                # Check for optimization info in session response
                if "optimization_info" in result:
                    opt_info = result["optimization_info"]
                    if opt_info.get("models_preloaded"):
                        print(f"✨ Server has pre-loaded models: {opt_info.get('expected_performance', 'faster processing')}")
                
                self._save_session_state()
                return self.session_id
            else:
                print(f"⚠️  Failed to start session: HTTP {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error starting session: {e}")
            return None
    
    def test_connection(self) -> bool:
        """Test server connection, detect optimization, and show server info"""
        try:
            print(f"🔗 Testing connection to: {self.server_url}")
            response = requests.get(f"{self.server_url}/", timeout=10)
            
            if response.status_code == 200:
                info = response.json()
                print("✅ Server connection successful!")
                print(f"   📊 Version: {info.get('version', 'Unknown')}")
                
                # Check for optimization features
                if "optimization" in info:
                    opt_info = info["optimization"]
                    print(f"   🚀 Optimization: {opt_info.get('performance_boost', 'None')}")
                    print(f"   ⚡ Models loaded: {opt_info.get('models_loaded', False)}")
                    if opt_info.get("time_saved"):
                        print(f"   ⏱️  Time saved: {opt_info['time_saved']}")
                
                print(f"   🔧 Workers: {info.get('workers', {}).get('max_threads', 'Unknown')}")
                print(f"   🎮 GPU slots: {info.get('workers', {}).get('max_gpu_concurrent', 'Unknown')}")
                print(f"   📈 Queue: {info.get('queue', {}).get('queued', 0)} queued, {info.get('queue', {}).get('processing', 0)} processing")
                
                # Detect server optimization
                self.detect_server_optimization()
                
                return True
            else:
                print(f"⚠️  Server responded with status {response.status_code}")
                return False
        except Exception as e:
            print(f"❌ Cannot connect to server: {e}")
            print("Make sure your Enhanced Marker server is running!")
            return False
    
    def process_folder_smart_with_retry_optimized(self, folder_path: str, auto_mode: bool = False, 
                                                 batch_size: Optional[int] = None, aggressive: bool = False, **kwargs):
        """OPTIMIZED batch processing with dynamic batch sizing for persistent model servers"""
        
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
        
        if not unprocessed_files:
            print(f"\n🎉 All valid PDFs have already been processed!")
            return
        
        # Get optimal batch size
        optimal_batch_size = self.get_optimal_batch_size(batch_size, aggressive)
        
        # Show optimization info
        print(f"\n🚀 OPTIMIZED PROCESSING CONFIGURATION:")
        print(f"   📊 Batch size: {optimal_batch_size} PDFs per batch")
        print(f"   🎯 Server type: {self.server_optimization_level}")
        print(f"   ⚡ Concurrent uploads: {self.max_concurrent_uploads}")
        print(f"   📥 Concurrent downloads: {self.max_concurrent_downloads}")
        print(f"   🔄 Poll interval: {self.poll_interval}s")
        
        if self.server_optimization_level == "optimized":
            print(f"   🚀 Using optimized server with persistent models!")
            print(f"   ⏱️  Expected: ~40% faster processing per PDF")
        
        # Ask for processing mode if not auto
        if not auto_mode:
            auto_mode = self._ask_processing_mode()
        
        if auto_mode:
            print(f"\n⚡ OPTIMIZED AUTOMATIC BATCH PROCESSING")
            print(f"🚀 Processing {len(unprocessed_files)} PDFs with batch size {optimal_batch_size}...")
            print("="*70)
        
        try:
            # Step 2: Process with optimized batching
            failed_pdfs = self._smart_batch_process_optimized(
                unprocessed_files, auto_mode, optimal_batch_size, **kwargs
            )
            
            # Step 3: Retry failed PDFs if any
            if failed_pdfs:
                self._retry_failed_pdfs(failed_pdfs, **kwargs)
            
            # Step 4: Final comprehensive summary
            self._show_comprehensive_summary(categorized, invalid_files)
            
        except KeyboardInterrupt:
            print(f"\n❌ Batch processing interrupted by user")
            self._show_comprehensive_summary(categorized, invalid_files)
    
    def _smart_batch_process_optimized(self, pdf_files: List[Path], auto_mode: bool, 
                                      batch_size: int, **kwargs) -> List[Path]:
        """OPTIMIZED batch processing with dynamic batch sizing"""
        
        print(f"📊 OPTIMIZED Processing strategy: Batches of {batch_size} PDFs")
        if self.server_optimization_level == "optimized":
            print(f"   ⚡ Using persistent models - NO model loading overhead!")
        print(f"   📝 Strategy: Upload {batch_size} → Wait for completion → Download → Repeat")
        print("=" * 70)
        
        total_files = len(pdf_files)
        completed_count = 0
        failed_pdfs = []
        
        # Calculate batch timing estimates
        if self.server_optimization_level == "optimized":
            estimated_time_per_pdf = 30  # seconds (optimized)
            estimated_total_time = (total_files * estimated_time_per_pdf) / batch_size
            print(f"⏱️  Estimated processing time: {estimated_total_time/60:.1f} minutes (with optimization)")
        
        # Process files in optimized batches
        for batch_start in range(0, total_files, batch_size):
            batch_end = min(batch_start + batch_size, total_files)
            current_batch = pdf_files[batch_start:batch_end]
            batch_num = (batch_start // batch_size) + 1
            total_batches = (total_files + batch_size - 1) // batch_size
            
            print(f"\n🚀 OPTIMIZED BATCH {batch_num}/{total_batches}: Processing {len(current_batch)} PDFs")
            print("-" * 60)
            
            # Phase 1: Parallel upload (increased concurrency)
            print(f"📤 Uploading batch {batch_num} with {self.max_concurrent_uploads} concurrent uploads...")
            uploaded_jobs = self._parallel_upload_batch(current_batch, **kwargs)
            
            # Track upload failures
            upload_failed_pdfs = [pdf for pdf in current_batch if not any(
                job_id for job_id in uploaded_jobs if job_id in self.active_jobs and 
                self.active_jobs[job_id].pdf_path == pdf
            )]
            failed_pdfs.extend(upload_failed_pdfs)
            
            if not uploaded_jobs:
                print(f"❌ No files uploaded successfully in batch {batch_num}")
                continue
            
            print(f"✅ Batch {batch_num}: {len(uploaded_jobs)}/{len(current_batch)} files uploaded successfully")
            
            # Phase 2: Optimized monitoring (faster polling)
            print(f"⏳ Monitoring batch {batch_num} with {self.poll_interval}s intervals...")
            batch_failed_pdfs = self._wait_for_batch_completion_optimized(uploaded_jobs)
            failed_pdfs.extend(batch_failed_pdfs)
            
            # Phase 3: Parallel download (increased concurrency)
            print(f"📥 Downloading batch {batch_num} with {self.max_concurrent_downloads} concurrent downloads...")
            download_failed_pdfs = self._parallel_download_batch(uploaded_jobs, **kwargs)
            failed_pdfs.extend(download_failed_pdfs)
            
            # Count completed jobs
            batch_completed = len([job_id for job_id in uploaded_jobs if job_id in self.completed_jobs])
            completed_count += batch_completed
            
            # Show enhanced batch summary
            batch_failed = len(current_batch) - batch_completed
            efficiency = (batch_completed / len(current_batch)) * 100 if current_batch else 0
            print(f"📊 Batch {batch_num} summary: {batch_completed} completed, {batch_failed} failed ({efficiency:.1f}% success)")
            
            # Shorter pause for optimized servers
            pause_time = 1 if self.server_optimization_level == "optimized" else 3
            if batch_end < total_files:
                print(f"⏸️  Brief pause ({pause_time}s) before next batch...")
                time.sleep(pause_time)
        
        # Enhanced processing summary
        total_failed = len(failed_pdfs)
        success_rate = (completed_count / total_files) * 100 if total_files > 0 else 0
        
        print(f"\n{'='*70}")
        print("📊 OPTIMIZED PROCESSING SUMMARY")
        print(f"{'='*70}")
        print(f"📄 Total PDFs processed: {total_files}")
        print(f"✅ Successfully completed: {completed_count}")
        print(f"❌ Failed (will retry): {total_failed}")
        print(f"📊 Success rate: {success_rate:.1f}%")
        print(f"⚡ Batch size used: {batch_size}")
        print(f"🎯 Server optimization: {self.server_optimization_level}")
        
        if self.server_optimization_level == "optimized":
            time_saved = completed_count * 20  # ~20s saved per PDF with persistent models
            print(f"⏱️  Estimated time saved: {time_saved/60:.1f} minutes")
        
        if failed_pdfs:
            print(f"\n❌ Failed files (will be retried):")
            for pdf_path in failed_pdfs[:10]:
                print(f"   ❌ {pdf_path.name}")
            if len(failed_pdfs) > 10:
                print(f"   ... and {len(failed_pdfs) - 10} more")
        
        print(f"{'='*70}")
        
        return failed_pdfs
    
    def _parallel_upload_batch(self, pdf_batch: List[Path], **kwargs) -> List[str]:
        """Upload batch of PDFs in parallel with increased concurrency"""
        
        def upload_single_pdf(pdf_path: Path) -> Optional[str]:
            try:
                return self.upload_pdf(pdf_path, **kwargs)
            except Exception as e:
                print(f"❌ Upload failed for {pdf_path.name}: {e}")
                return None
        
        uploaded_jobs = []
        
        # Use ThreadPoolExecutor for parallel uploads
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_concurrent_uploads) as executor:
            # Submit all upload tasks
            future_to_pdf = {
                executor.submit(upload_single_pdf, pdf_path): pdf_path 
                for pdf_path in pdf_batch
            }
            
            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_pdf):
                pdf_path = future_to_pdf[future]
                try:
                    job_id = future.result()
                    if job_id:
                        uploaded_jobs.append(job_id)
                        print(f"   ✅ {pdf_path.name} → {job_id}")
                    else:
                        print(f"   ❌ Failed: {pdf_path.name}")
                except Exception as e:
                    print(f"   ❌ Exception uploading {pdf_path.name}: {e}")
        
        return uploaded_jobs
    
    def _wait_for_batch_completion_optimized(self, job_ids: List[str]) -> List[Path]:
        """Optimized batch monitoring with faster polling"""
        
        pending_jobs = set(job_ids)
        completed_jobs = set()
        failed_pdfs = []
        
        print(f"   👁️  Monitoring {len(pending_jobs)} jobs (poll every {self.poll_interval}s)...")
        
        last_status_update = time.time()
        status_update_interval = 10  # Show progress every 10 seconds
        
        while pending_jobs:
            try:
                # Check status of all pending jobs
                jobs_to_remove = []
                for job_id in pending_jobs:
                    status = self.check_job_status(job_id)
                    if not status:
                        continue
                    
                    job_status = status.get('status')
                    
                    if job_status == 'completed':
                        jobs_to_remove.append(job_id)
                        completed_jobs.add(job_id)
                        if job_id in self.active_jobs:
                            job_info = self.active_jobs[job_id]
                            pages = status.get('pages_processed', '?')
                            processing_time = status.get('processing_time_seconds', '?')
                            
                            # Show optimization info if available
                            optimization = status.get('optimization', {})
                            if optimization.get('used_persistent_models'):
                                opt_info = f" (⚡ persistent models, saved {optimization.get('time_saved', '~20s')})"
                            else:
                                opt_info = ""
                            
                            print(f"      ✅ {job_info.pdf_path.name} completed ({pages} pages, {processing_time}s{opt_info})")
                    
                    elif job_status == 'failed':
                        jobs_to_remove.append(job_id)
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
                
                # Remove completed/failed jobs
                for job_id in jobs_to_remove:
                    pending_jobs.discard(job_id)
                
                # Show progress update
                current_time = time.time()
                if current_time - last_status_update > status_update_interval:
                    if pending_jobs:
                        processing_count = 0
                        queued_count = 0
                        
                        for job_id in list(pending_jobs)[:5]:  # Check first 5
                            if job_id in self.active_jobs:
                                status = self.check_job_status(job_id)
                                if status:
                                    current_status = status.get('status', 'unknown')
                                    if current_status == 'processing':
                                        processing_count += 1
                                    elif current_status == 'queued':
                                        queued_count += 1
                        
                        print(f"      🔄 Still monitoring {len(pending_jobs)} jobs ({processing_count} processing, {queued_count} queued)")
                    
                    last_status_update = current_time
                
                # Faster polling for optimized servers
                time.sleep(self.poll_interval)
                
            except KeyboardInterrupt:
                print(f"\n❌ Batch monitoring interrupted by user")
                break
        
        print(f"   ✅ Batch monitoring completed: {len(completed_jobs)} successful, {len(failed_pdfs)} failed")
        return failed_pdfs
    
    def _parallel_download_batch(self, job_ids: List[str], **kwargs) -> List[Path]:
        """Download batch results in parallel with increased concurrency"""
        
        def download_single_job(job_id: str) -> Optional[Path]:
            try:
                if job_id not in self.active_jobs:
                    return None
                
                job_info = self.active_jobs[job_id]
                
                # Check if job completed successfully
                status = self.check_job_status(job_id)
                if not status or status.get('status') != 'completed':
                    return job_info.pdf_path  # Mark as failed
                
                # Download the result
                output_file = self.download_job_result(
                    job_id, job_info.pdf_path,
                    kwargs.get('output_format', 'markdown'),
                    kwargs.get('download_all', False),
                    kwargs.get('keep_alive', False)
                )
                
                if output_file:
                    # Mark as completed
                    job_info.status = "completed"
                    job_info.completion_time = datetime.now()
                    job_info.output_file = output_file
                    self.completed_jobs[job_id] = job_info
                    del self.active_jobs[job_id]
                    return None  # Success
                else:
                    return job_info.pdf_path  # Download failed
                    
            except Exception as e:
                print(f"❌ Download error for job {job_id}: {e}")
                if job_id in self.active_jobs:
                    return self.active_jobs[job_id].pdf_path
                return None
        
        download_failed_pdfs = []
        
        # Use ThreadPoolExecutor for parallel downloads
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_concurrent_downloads) as executor:
            # Submit all download tasks
            future_to_job = {
                executor.submit(download_single_job, job_id): job_id 
                for job_id in job_ids
            }
            
            # Collect results as they complete
            for future in concurrent.futures.as_completed(future_to_job):
                job_id = future_to_job[future]
                try:
                    failed_pdf = future.result()
                    if failed_pdf:
                        download_failed_pdfs.append(failed_pdf)
                        print(f"   ❌ Download failed: {failed_pdf.name}")
                    else:
                        if job_id in self.completed_jobs:
                            job_info = self.completed_jobs[job_id]
                            print(f"   ✅ Downloaded: {job_info.pdf_path.name}")
                except Exception as e:
                    print(f"   ❌ Exception downloading job {job_id}: {e}")
        
        return download_failed_pdfs
    
    # Include all the other methods from the original CLI
    def upload_pdf(self, pdf_path: Path, output_format: str = "markdown", 
                   use_ocr: bool = False, storage_path: str = None,
                   retention: str = "24h", max_downloads: int = 3,
                   download_all: bool = False, keep_alive: bool = False) -> Optional[str]:
        """Upload PDF with enhanced parameters"""
        
        if not self.session_id:
            self.start_session()
        
        try:
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
                    
                    return job_id
                else:
                    return None
                    
        except Exception as e:
            return None
    
    def check_job_status(self, job_id: str, detailed: bool = False) -> Optional[Dict]:
        """Check job status with optional detailed information"""
        try:
            endpoint = f"{self.status_url}/{job_id}/detailed" if detailed else f"{self.status_url}/{job_id}"
            response = requests.get(endpoint, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            else:
                return None
                
        except Exception as e:
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
                return None
                
        except Exception as e:
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
            
            return output_folder
            
        finally:
            # Clean up temporary ZIP
            os.unlink(temp_zip_path)
    
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
            
            # Check if it was processed successfully since the failure
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
                # Process with detailed monitoring
                result = self._process_single_pdf_with_retry_tracking(pdf_path, 1, **kwargs)
                
                if result:
                    retry_completed += 1
                    print(f"   🎉 RETRY SUCCESS: {pdf_path.name}")
                else:
                    retry_still_failed += 1
                    print(f"   ❌ RETRY FAILED: {pdf_path.name}")
                
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
            job_id = self.upload_pdf(pdf_path, **kwargs)
            if not job_id:
                return None
            
            if not self.wait_for_completion(job_id):
                return None
            
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
            return None
    
    def wait_for_completion(self, job_id: str, max_wait_time: int = 3600) -> bool:
        """Wait for job completion with enhanced status display"""
        
        start_time = time.time()
        last_status = None
        
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
                    if current_status == 'completed':
                        return True
                    elif current_status == 'failed':
                        return False
                    
                    last_status = current_status
                
                # Check timeout
                elapsed = time.time() - start_time
                if elapsed > max_wait_time:
                    return False
                
                time.sleep(self.poll_interval)
                
            except KeyboardInterrupt:
                return False
            except Exception as e:
                time.sleep(self.poll_interval * 2)
    
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
        
        # Show optimization benefits
        if self.server_optimization_level == "optimized" and total_completed > 0:
            time_saved = total_completed * 20  # ~20s saved per PDF
            print(f"⚡ Optimization benefits:")
            print(f"   ⏱️  Time saved: ~{time_saved/60:.1f} minutes")
            print(f"   🚀 Batch size used: {self.adaptive_batch_size}")
            print(f"   💾 Persistent models: Yes")
        
        print(f"{'='*70}")
    
    def _find_pdf_files(self, folder: Path) -> List[Path]:
        """Find all PDF files in folder"""
        pdf_files = list(folder.glob("*.pdf")) + list(folder.glob("*.PDF"))
        return sorted(list(set(pdf_files)))
    
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

def main():
    parser = argparse.ArgumentParser(
        description="OPTIMIZED Enhanced Marker PDF Parser CLI with dynamic batch sizing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
OPTIMIZED Examples:
  # Auto-detect optimal batch size for server
  python enhanced_marker_cli.py --folder ./pdfs --auto
  
  # Force specific batch size
  python enhanced_marker_cli.py --folder ./pdfs --auto --batch-size 8
  
  # Aggressive mode for optimized servers (2x batch size)
  python enhanced_marker_cli.py --folder ./pdfs --auto --aggressive
  
  # Custom server with optimization detection
  python enhanced_marker_cli.py --folder ./pdfs --auto --server https://your-server.com
  
  # Monitor optimized server performance
  python enhanced_marker_cli.py --monitor
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
    
    # OPTIMIZED batch processing options
    parser.add_argument('--batch-size', type=int, help='Force specific batch size (overrides auto-detection)')
    parser.add_argument('--aggressive', action='store_true', help='Aggressive mode: 2x batch size for optimized servers')
    
    # Server and format options
    parser.add_argument('--server', default='https://pjavwu4ljbpcdc-8888.proxy.runpod.net/',
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
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.auto and not args.folder:
        print("❌ Error: --auto flag can only be used with --folder")
        sys.exit(1)
    
    if args.batch_size and not args.folder:
        print("❌ Error: --batch-size can only be used with --folder")
        sys.exit(1)
    
    if args.aggressive and not args.folder:
        print("❌ Error: --aggressive can only be used with --folder")
        sys.exit(1)
    
    try:
        # Initialize optimized parser
        pdf_parser = EnhancedMarkerParser(args.server)
        pdf_parser._should_cleanup_session = args.session_cleanup
        
        # Test server connection and detect optimization
        if not pdf_parser.test_connection():
            sys.exit(1)
        
        # Handle different modes
        if args.folder:
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
            
            # OPTIMIZED folder processing
            download_text = " + COMPLETE FOLDERS" if args.all else ""
            batch_info = f" (batch size: {args.batch_size or 'auto-detect'})"
            aggressive_info = " + AGGRESSIVE" if args.aggressive else ""
            
            print(f"\n🗂️  OPTIMIZED FOLDER PROCESSING{batch_info}{aggressive_info}{download_text}")
            print("=" * 70)
            
            # Use optimized batch processing
            pdf_parser.process_folder_smart_with_retry_optimized(
                args.folder, 
                auto_mode=args.auto, 
                batch_size=args.batch_size,
                aggressive=args.aggressive,
                **process_kwargs
            )
            
            # Session cleanup if requested
            if args.session_cleanup:
                print(f"\n🧹 Performing session cleanup...")
                pdf_parser.cleanup_session()
        
        else:
            # Handle other modes (monitor, download-only, etc.) - same as before
            print("Other modes not implemented in this example")
        
    except KeyboardInterrupt:
        print("\n❌ Process interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()