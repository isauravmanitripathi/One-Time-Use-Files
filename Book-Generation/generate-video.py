#!/usr/bin/env python3
"""
Audiobook Video Generator
Creates a synchronized video from CSV transcription data using Pillow + FFmpeg

Requirements:
- pip install pillow pandas
- ffmpeg installed and in PATH
- CSV file with columns: Start (s), End (s), Segment
"""

import os
import sys
import subprocess
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import textwrap
import shutil
from pathlib import Path

class AudiobookVideoGenerator:
    def __init__(self, csv_file, audio_file):
        self.csv_file = csv_file
        self.audio_file = audio_file
        
        # Create output file path next to audio file
        audio_path = Path(audio_file)
        audio_name = audio_path.stem  # filename without extension
        self.output_file = audio_path.parent / f"{audio_name}_video.mp4"
        
        # Video settings
        self.width = 1920
        self.height = 1080
        self.fps = 30
        
        # Text styling
        self.bg_color = (20, 20, 30)  # Dark blue background
        self.text_color = (255, 255, 255)  # White text
        self.highlight_color = (255, 255, 100)  # Yellow highlight
        self.font_size = 48
        self.line_spacing = 1.2
        self.margin = 100
        
        # Load font (will fallback to default if not found)
        self.font = self._load_font()
        
        # Fixed temporary directory for frames
        self.temp_dir = "/Volumes/hard-drive/miscellaneous-files/Book-Generation/temporary-images"
        
    def _load_font(self):
        """Load a nice font, fallback to default if not available"""
        font_paths = [
            "/System/Library/Fonts/Helvetica.ttc",  # macOS
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
            "C:/Windows/Fonts/arial.ttf",  # Windows
        ]
        
        for font_path in font_paths:
            try:
                if os.path.exists(font_path):
                    return ImageFont.truetype(font_path, self.font_size)
            except:
                continue
        
        # Fallback to default font
        try:
            return ImageFont.truetype("Arial.ttf", self.font_size)
        except:
            return ImageFont.load_default()
    
    def load_transcription(self):
        """Load the CSV transcription file"""
        try:
            df = pd.read_csv(self.csv_file)
            print(f"Loaded {len(df)} segments from {self.csv_file}")
            print(f"Total duration: {df['End (s)'].max():.2f} seconds")
            return df
        except Exception as e:
            print(f"Error loading CSV: {e}")
            sys.exit(1)
    
    def wrap_text(self, text, max_width):
        """Wrap text to fit within specified width"""
        # Calculate approximate characters per line based on font size
        avg_char_width = self.font_size * 0.6  # Rough estimate
        chars_per_line = int((max_width - 2 * self.margin) / avg_char_width)
        
        return textwrap.fill(text, width=chars_per_line)
    
    def create_text_frame(self, text, highlight=False):
        """Create a single frame with text"""
        # Create image
        img = Image.new('RGB', (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(img)
        
        # Wrap text
        wrapped_text = self.wrap_text(text, self.width)
        
        # Calculate text position (centered)
        lines = wrapped_text.split('\n')
        total_height = len(lines) * self.font_size * self.line_spacing
        
        start_y = (self.height - total_height) // 2
        
        # Draw each line
        for i, line in enumerate(lines):
            # Get text dimensions
            bbox = draw.textbbox((0, 0), line, font=self.font)
            text_width = bbox[2] - bbox[0]
            
            # Center horizontally
            x = (self.width - text_width) // 2
            y = start_y + i * self.font_size * self.line_spacing
            
            # Choose color
            color = self.highlight_color if highlight else self.text_color
            
            # Draw text
            draw.text((x, y), line, font=self.font, fill=color)
        
        return img
    
    def generate_frames(self, df):
        """Generate one frame per text segment with duration info"""
        print("Generating frames...")
        
        # Ensure temporary directory exists
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir, exist_ok=True)
            print(f"Created temporary directory: {self.temp_dir}")
        else:
            # Clean existing frames if any
            for file in os.listdir(self.temp_dir):
                if file.startswith("frame_") and file.endswith(".png"):
                    os.remove(os.path.join(self.temp_dir, file))
            print(f"Using temporary directory: {self.temp_dir}")
        
        print(f"Total segments to process: {len(df)}")
        
        # Create a list to store frame information
        frame_info = []
        
        # Generate one frame per segment
        for index, row in df.iterrows():
            start_time = row['Start (s)']
            end_time = row['End (s)']
            duration = end_time - start_time
            text = row['Segment']
            
            # Create frame with current segment text
            frame = self.create_text_frame(text)
            
            # Save frame
            frame_path = os.path.join(self.temp_dir, f"segment_{index:03d}.png")
            frame.save(frame_path)
            
            # Store frame info for FFmpeg
            frame_info.append({
                'frame_path': frame_path,
                'start_time': start_time,
                'end_time': end_time,
                'duration': duration
            })
            
            # Progress indicator
            if (index + 1) % 20 == 0:
                progress = ((index + 1) / len(df)) * 100
                print(f"Progress: {progress:.1f}% ({index + 1}/{len(df)} segments)")
        
        print(f"Generated {len(frame_info)} frames (one per segment)")
        return frame_info
    
    def create_video(self, frame_info):
        """Use FFmpeg to create video from frames with specific durations and combine with audio"""
        print("Creating video with FFmpeg...")
        
        # Create a temporary file list for FFmpeg concat
        concat_file = os.path.join(self.temp_dir, "concat_list.txt")
        video_only = os.path.join(self.temp_dir, "video_only.mp4")
        final_output = str(self.output_file)
        
        # Step 1: Create individual video clips for each segment and concatenate
        print("Step 1: Creating video segments...")
        
        # Create concat file content
        with open(concat_file, 'w') as f:
            for i, info in enumerate(frame_info):
                segment_video = os.path.join(self.temp_dir, f"segment_{i:03d}.mp4")
                
                # Create video segment from single frame with specific duration
                ffmpeg_cmd = [
                    'ffmpeg', '-y',
                    '-loop', '1',
                    '-i', info['frame_path'],
                    '-t', str(info['duration']),
                    '-c:v', 'libx264',
                    '-pix_fmt', 'yuv420p',
                    '-r', str(self.fps),
                    segment_video
                ]
                
                try:
                    subprocess.run(ffmpeg_cmd, check=True, capture_output=True)
                    f.write(f"file '{segment_video}'\n")
                except subprocess.CalledProcessError as e:
                    print(f"Error creating segment {i}: {e}")
                    return False
                
                # Progress indicator
                if (i + 1) % 20 == 0:
                    progress = ((i + 1) / len(frame_info)) * 100
                    print(f"Video segments progress: {progress:.1f}% ({i + 1}/{len(frame_info)})")
        
        # Step 2: Concatenate all segments
        print("Step 2: Concatenating video segments...")
        concat_cmd = [
            'ffmpeg', '-y',
            '-f', 'concat',
            '-safe', '0',
            '-i', concat_file,
            '-c', 'copy',
            video_only
        ]
        
        try:
            subprocess.run(concat_cmd, check=True, capture_output=True)
            print("✓ Video segments concatenated successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error concatenating video: {e}")
            print(f"FFmpeg output: {e.stderr.decode()}")
            return False
        
        # Step 3: Combine with audio
        print("Step 3: Adding audio...")
        ffmpeg_cmd_audio = [
            'ffmpeg', '-y',
            '-i', video_only,
            '-i', self.audio_file,
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-shortest',  # Match the shorter duration
            final_output
        ]
        
        try:
            subprocess.run(ffmpeg_cmd_audio, check=True, capture_output=True)
            print(f"✓ Final video created: {final_output}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error adding audio: {e}")
            print(f"FFmpeg output: {e.stderr.decode()}")
            return False
    
    def cleanup(self):
        """Clean up temporary files"""
        try:
            # Only clean frame files, keep the directory
            for file in os.listdir(self.temp_dir):
                file_path = os.path.join(self.temp_dir, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            print("✓ Temporary files cleaned up")
        except Exception as e:
            print(f"Warning: Could not clean up temporary files: {e}")
    
    def generate(self):
        """Main method to generate the complete video"""
        print("🎬 Starting Audiobook Video Generation")
        print("=" * 50)
        print(f"📄 CSV file: {self.csv_file}")
        print(f"🎵 Audio file: {self.audio_file}")
        print(f"📹 Output will be saved at: {self.output_file}")
        print(f"🗂️  Temporary frames: {self.temp_dir}")
        print("=" * 50)
        
        try:
            # Load transcription data
            df = self.load_transcription()
            
            # Generate frames (one per segment)
            frame_info = self.generate_frames(df)
            
            # Create video
            success = self.create_video(frame_info)
            
            if success:
                print("=" * 50)
                print("🎉 SUCCESS! Your audiobook video is ready!")
                print(f"📹 Output file: {self.output_file}")
                file_size = os.path.getsize(self.output_file) / (1024 * 1024)
                print(f"📁 File size: {file_size:.1f} MB")
            else:
                print("❌ Video generation failed")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            # Always cleanup
            self.cleanup()

def get_user_inputs():
    """Get CSV and audio file paths from user input"""
    print("🎬 Audiobook Video Generator")
    print("=" * 40)
    
    # Get CSV file path
    while True:
        csv_path = input("📄 Enter the path to your CSV transcription file: ").strip()
        csv_path = csv_path.strip('"\'')  # Remove quotes if present
        
        if os.path.exists(csv_path) and csv_path.endswith('.csv'):
            break
        else:
            print("❌ CSV file not found or invalid. Please try again.")
    
    # Get audio file path
    while True:
        audio_path = input("🎵 Enter the path to your audio file: ").strip()
        audio_path = audio_path.strip('"\'')  # Remove quotes if present
        
        if os.path.exists(audio_path):
            # Check if it's likely an audio file
            audio_extensions = ['.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg']
            if any(audio_path.lower().endswith(ext) for ext in audio_extensions):
                break
            else:
                print("⚠️  File doesn't appear to be an audio file, but continuing anyway...")
                break
        else:
            print("❌ Audio file not found. Please try again.")
    
    return csv_path, audio_path

# Usage example and main execution
if __name__ == "__main__":
    # Get user inputs
    csv_file, audio_file = get_user_inputs()
    
    # Create generator
    generator = AudiobookVideoGenerator(
        csv_file=csv_file,
        audio_file=audio_file
    )
    
    # Generate video
    generator.generate()