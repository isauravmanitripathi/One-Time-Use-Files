#!/usr/bin/env python3
import os
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
import json

def run_ffmpeg_command(command, description=""):
    """Run FFmpeg command and handle errors"""
    print(f"Running: {description}")
    print(f"Command: {' '.join(command)}")
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("✓ Success")
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"✗ Error: {e}")
        print(f"FFmpeg stderr: {e.stderr}")
        return False, None

def get_duration(file_path):
    """Get duration of video/audio file in seconds"""
    command = [
        'ffprobe', '-v', 'quiet', '-print_format', 'json', 
        '-show_format', file_path
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        duration = float(data['format']['duration'])
        return duration
    except Exception as e:
        print(f"Error getting duration for {file_path}: {e}")
        return None

def create_concat_file(video_paths, temp_dir):
    """Create concat file for FFmpeg"""
    concat_file = os.path.join(temp_dir, 'concat_list.txt')
    
    with open(concat_file, 'w') as f:
        for path in video_paths:
            # Use absolute paths and escape single quotes
            abs_path = os.path.abspath(path)
            f.write(f"file '{abs_path}'\n")
    
    return concat_file

def concat_videos(video_paths, output_path, temp_dir):
    """Concatenate videos using FFmpeg concat demuxer"""
    print(f"\n=== Step 1: Concatenating {len(video_paths)} videos ===")
    
    # Create concat file
    concat_file = create_concat_file(video_paths, temp_dir)
    
    # FFmpeg concat command
    command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', concat_file,
        '-c', 'copy', output_path, '-y'
    ]
    
    success, _ = run_ffmpeg_command(command, "Concatenating videos")
    return success

def extract_audio(video_path, audio_path):
    """Extract audio from video"""
    print(f"\n=== Step 2: Extracting audio ===")
    
    command = [
        'ffmpeg', '-i', video_path, '-vn', '-acodec', 'copy', 
        audio_path, '-y'
    ]
    
    success, _ = run_ffmpeg_command(command, "Extracting audio from combined video")
    return success

def adjust_video_speed(input_video, output_video, speed_factor):
    """Adjust video speed to match audio duration"""
    print(f"\n=== Step 3: Adjusting video speed (factor: {speed_factor:.4f}) ===")
    
    if abs(speed_factor - 1.0) < 0.001:
        print("Speed adjustment not needed (factor ~1.0)")
        shutil.copy2(input_video, output_video)
        return True
    
    # Use setpts filter for video speed adjustment
    video_filter = f"setpts={1/speed_factor:.6f}*PTS"
    audio_filter = f"atempo={speed_factor:.6f}" if speed_factor <= 2.0 else f"atempo=2.0,atempo={speed_factor/2.0:.6f}"
    
    command = [
        'ffmpeg', '-i', input_video,
        '-filter:v', video_filter,
        '-filter:a', audio_filter,
        '-c:v', 'libx264', '-c:a', 'aac',
        output_video, '-y'
    ]
    
    success, _ = run_ffmpeg_command(command, f"Adjusting video speed by {speed_factor:.4f}x")
    return success

def combine_video_audio(video_path, audio_path, output_path):
    """Combine adjusted video with separate audio"""
    print(f"\n=== Step 4: Combining video with audio ===")
    
    command = [
        'ffmpeg', '-i', video_path, '-i', audio_path,
        '-c:v', 'copy', '-c:a', 'aac', '-map', '0:v:0', '-map', '1:a:0',
        output_path, '-y'
    ]
    
    success, _ = run_ffmpeg_command(command, "Combining adjusted video with audio")
    return success

def get_video_paths():
    """Get video paths from user input"""
    print("Enter video paths (press Enter after each path, empty line to finish):")
    video_paths = []
    
    while True:
        path = input(f"Video {len(video_paths) + 1} (or press Enter to finish): ").strip()
        
        if not path:
            break
            
        if not os.path.exists(path):
            print(f"Warning: Path '{path}' does not exist.")
            continue
            
        if not os.path.isfile(path):
            print(f"Warning: '{path}' is not a file.")
            continue
        
        video_paths.append(path)
        print(f"✓ Added: {os.path.basename(path)}")
    
    return video_paths

def get_audio_path():
    """Get audio file path from user"""
    while True:
        audio_path = input("\nEnter audio file path: ").strip()
        
        if not audio_path:
            print("Please enter a valid audio path.")
            continue
            
        if not os.path.exists(audio_path):
            print(f"Audio file '{audio_path}' does not exist.")
            continue
            
        if not os.path.isfile(audio_path):
            print(f"'{audio_path}' is not a file.")
            continue
        
        return audio_path

def main():
    print("=== FFmpeg Video-Audio Combiner with Speed Matching ===\n")
    
    # Check if ffmpeg is available
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        subprocess.run(['ffprobe', '-version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: FFmpeg or FFprobe not found. Please install FFmpeg.")
        print("On macOS with Homebrew: brew install ffmpeg")
        sys.exit(1)
    
    # Get input files
    video_paths = get_video_paths()
    if len(video_paths) < 1:
        print("Error: Need at least 1 video file.")
        sys.exit(1)
    
    audio_path = get_audio_path()
    
    # Get output path
    output_path = input("\nEnter output video path (e.g., final_video.mp4): ").strip()
    if not output_path:
        output_path = "final_combined_video.mp4"
    
    # Add .mp4 extension if not present
    if not Path(output_path).suffix:
        output_path += '.mp4'
    
    print(f"\nProcessing:")
    print(f"- Videos: {len(video_paths)} files")
    print(f"- Audio: {os.path.basename(audio_path)}")
    print(f"- Output: {output_path}")
    
    # Create temporary directory
    temp_dir = tempfile.mkdtemp(prefix='video_combiner_')
    print(f"- Temp directory: {temp_dir}")
    
    try:
        # Step 1: Concatenate videos (if more than one)
        if len(video_paths) > 1:
            combined_video = os.path.join(temp_dir, 'combined_video.mp4')
            if not concat_videos(video_paths, combined_video, temp_dir):
                print("Failed to concatenate videos")
                sys.exit(1)
        else:
            combined_video = video_paths[0]
            print(f"\nUsing single video: {os.path.basename(combined_video)}")
        
        # Step 2: Get durations
        print(f"\n=== Analyzing durations ===")
        video_duration = get_duration(combined_video)
        audio_duration = get_duration(audio_path)
        
        if video_duration is None or audio_duration is None:
            print("Failed to get file durations")
            sys.exit(1)
        
        print(f"Video duration: {video_duration:.2f} seconds")
        print(f"Audio duration: {audio_duration:.2f} seconds")
        
        # Calculate speed adjustment needed
        speed_factor = video_duration / audio_duration
        print(f"Speed adjustment factor: {speed_factor:.4f}")
        
        if speed_factor > 1:
            print(f"Video will be sped up by {speed_factor:.2f}x to match audio")
        elif speed_factor < 1:
            print(f"Video will be slowed down by {1/speed_factor:.2f}x to match audio")
        else:
            print("Video and audio durations match!")
        
        # Step 3: Adjust video speed if needed
        adjusted_video = os.path.join(temp_dir, 'speed_adjusted_video.mp4')
        
        if abs(speed_factor - 1.0) > 0.001:  # Only adjust if significant difference
            if not adjust_video_speed(combined_video, adjusted_video, speed_factor):
                print("Failed to adjust video speed")
                sys.exit(1)
        else:
            # No adjustment needed, use original
            adjusted_video = combined_video
        
        # Step 4: Combine adjusted video with audio
        if not combine_video_audio(adjusted_video, audio_path, output_path):
            print("Failed to combine video and audio")
            sys.exit(1)
        
        # Verify final result
        final_duration = get_duration(output_path)
        print(f"\n=== Final Result ===")
        print(f"✓ Successfully created: {output_path}")
        print(f"Final video duration: {final_duration:.2f} seconds")
        print(f"Target audio duration: {audio_duration:.2f} seconds")
        
        if abs(final_duration - audio_duration) < 0.1:
            print("✓ Durations match perfectly!")
        else:
            print(f"⚠ Duration difference: {abs(final_duration - audio_duration):.2f} seconds")
    
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
    
    finally:
        # Clean up temporary files
        print(f"\nCleaning up temporary files...")
        shutil.rmtree(temp_dir, ignore_errors=True)
        print("✓ Cleanup complete")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(1)