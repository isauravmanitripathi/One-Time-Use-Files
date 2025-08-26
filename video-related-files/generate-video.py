#!/usr/bin/env python3

import os
import subprocess
import shutil
from PIL import Image
import concurrent.futures
from pathlib import Path
import time
import random
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.panel import Panel

console = Console()

# YouTube 1080p dimensions
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FRAME_RATE = 30
SEGMENT_DURATION = 2  # seconds per segment
SEGMENTS_PER_IMAGE = 5  # 5 segments x 2 seconds = 10 seconds total per image

def is_valid_image_file(file_path):
    """Check if the file is a valid image file using PIL"""
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except Exception:
        return False

def get_valid_image_files(directory):
    """Get all valid image files from a directory"""
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
    valid_files = []
    
    with console.status("[bold yellow]Scanning directory for images..."):
        for file_path in Path(directory).rglob('*'):
            if (file_path.is_file() and 
                file_path.suffix.lower() in valid_extensions and 
                is_valid_image_file(file_path)):
                valid_files.append(str(file_path))
    
    return sorted(valid_files)

def create_canvas_image(image_path, output_path):
    """Place image on 1080p canvas without changing its size"""
    try:
        # Open and load image
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Create black canvas
            canvas = Image.new('RGB', (VIDEO_WIDTH, VIDEO_HEIGHT), (0, 0, 0))
            
            # Calculate centering position
            img_width, img_height = img.size
            
            # Handle images larger than canvas (with 20px margin)
            margin = 20
            available_width = VIDEO_WIDTH - (2 * margin)
            available_height = VIDEO_HEIGHT - (2 * margin)
            
            if img_width > available_width or img_height > available_height:
                # Calculate scale to fit within available space while maintaining aspect ratio
                scale_x = available_width / img_width
                scale_y = available_height / img_height
                scale = min(scale_x, scale_y)
                
                new_width = int(img_width * scale)
                new_height = int(img_height * scale)
                
                img = img.resize((new_width, new_height), Image.LANCZOS)
                
                x_offset = (VIDEO_WIDTH - new_width) // 2
                y_offset = (VIDEO_HEIGHT - new_height) // 2
            else:
                # Image fits within canvas, just center it
                x_offset = (VIDEO_WIDTH - img_width) // 2
                y_offset = (VIDEO_HEIGHT - img_height) // 2
            
            # Paste image onto canvas
            canvas.paste(img, (x_offset, y_offset))
            
            # Save canvas image
            canvas.save(output_path, 'PNG', quality=95)
            return True
            
    except Exception as e:
        console.print(f"[red]Error processing {image_path}: {e}[/red]")
        return False

def create_segment_video(canvas_image_path, video_output_path, duration=2):
    """Create a 2-second video segment from a single image using FFmpeg"""
    try:
        cmd = [
            'ffmpeg', '-y',
            '-loop', '1',                    # Loop the input image
            '-i', canvas_image_path,         # Input image
            '-t', str(duration),             # Duration (2 seconds)
            '-r', str(FRAME_RATE),           # Frame rate
            '-c:v', 'h264_videotoolbox',     # Hardware encoder (macOS)
            '-b:v', '5M',                    # Bitrate
            '-pix_fmt', 'yuv420p',           # Pixel format for compatibility
            '-movflags', '+faststart',       # Fast streaming
            video_output_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            console.print(f"[red]FFmpeg error for {video_output_path}:[/red]")
            console.print(result.stderr)
            return False
        
        return True
        
    except Exception as e:
        console.print(f"[red]Error creating video {video_output_path}: {e}[/red]")
        return False

def create_segments_for_image(canvas_path, segments_dir, image_index):
    """Create 5 segments of 2 seconds each for a single image"""
    segment_paths = []
    
    for segment_idx in range(SEGMENTS_PER_IMAGE):
        segment_filename = f"segment_{image_index:05d}_{segment_idx:02d}.mp4"
        segment_path = os.path.join(segments_dir, segment_filename)
        
        success = create_segment_video(canvas_path, segment_path, SEGMENT_DURATION)
        if success:
            segment_paths.append(segment_path)
        else:
            console.print(f"[red]Failed to create segment {segment_filename}[/red]")
    
    return segment_paths

def combine_videos_randomly(video_segments, output_path, temp_dir):
    """Randomly shuffle and combine all video segments"""
    try:
        # Shuffle the segments randomly
        shuffled_segments = video_segments.copy()
        random.shuffle(shuffled_segments)
        
        console.print(f"[cyan]Shuffling {len(shuffled_segments)} video segments randomly...[/cyan]")
        
        # Create concat file with shuffled order
        concat_file = os.path.join(temp_dir, 'random_concat_list.txt')
        with open(concat_file, 'w') as f:
            for video_file in shuffled_segments:
                # Use relative paths for concat file
                rel_path = os.path.relpath(video_file, temp_dir)
                f.write(f"file '{rel_path}'\n")
        
        # Combine videos using concat demuxer
        cmd = [
            'ffmpeg', '-y',
            '-f', 'concat',
            '-safe', '0',
            '-i', concat_file,
            '-c', 'copy',                    # Copy streams without re-encoding (FAST!)
            '-movflags', '+faststart',
            output_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=temp_dir)
        if result.returncode != 0:
            console.print("[red]Error combining videos:[/red]")
            console.print(result.stderr)
            return False
        
        return True
        
    except Exception as e:
        console.print(f"[red]Error combining videos: {e}[/red]")
        return False

def process_images_to_random_slideshow(input_directory):
    """Main function to process all images into a random slideshow video"""
    try:
        start_time = time.time()
        
        # Validate input directory
        if not os.path.isdir(input_directory):
            console.print(f"[red]Error: Directory not found: {input_directory}[/red]")
            return
        
        # Get all valid image files
        image_files = get_valid_image_files(input_directory)
        if not image_files:
            console.print("[red]No valid image files found in directory.[/red]")
            return
        
        console.print(f"Found [green]{len(image_files)}[/green] valid images")
        console.print(f"Each image will be split into [cyan]{SEGMENTS_PER_IMAGE}[/cyan] segments of [cyan]{SEGMENT_DURATION}[/cyan] seconds")
        console.print(f"Total segments to create: [yellow]{len(image_files) * SEGMENTS_PER_IMAGE}[/yellow]")
        
        # Create temp directory inside the input directory
        temp_dir = os.path.join(input_directory, 'random_slideshow_temp')
        canvas_dir = os.path.join(temp_dir, 'canvas_images')
        segments_dir = os.path.join(temp_dir, 'video_segments')
        
        # Clean up existing temp directory if it exists
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        
        os.makedirs(canvas_dir, exist_ok=True)
        os.makedirs(segments_dir, exist_ok=True)
        
        console.print(f"[cyan]Working directory:[/cyan] {temp_dir}")
        
        # Step 1: Create canvas images
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console
        ) as progress:
            
            task1 = progress.add_task("[cyan]Creating canvas images...", total=len(image_files))
            
            def process_image(idx_and_path):
                idx, image_path = idx_and_path
                canvas_filename = f"canvas_{idx:05d}.png"
                canvas_path = os.path.join(canvas_dir, canvas_filename)
                success = create_canvas_image(image_path, canvas_path)
                progress.update(task1, advance=1)
                return (idx, canvas_path, success)
            
            # Process images in parallel
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
                results = list(executor.map(process_image, enumerate(image_files)))
        
        # Filter successful canvas images
        successful_canvas = [(idx, path) for idx, path, success in results if success]
        console.print(f"Successfully created [green]{len(successful_canvas)}[/green] canvas images")
        
        if not successful_canvas:
            console.print("[red]No canvas images were created successfully.[/red]")
            return
        
        # Step 2: Create video segments for each image
        all_segments = []
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TaskProgressColumn(),
            TimeRemainingColumn(),
            console=console
        ) as progress:
            
            task2 = progress.add_task("[cyan]Creating video segments...", total=len(successful_canvas))
            
            def create_segments(idx_and_canvas):
                idx, canvas_path = idx_and_canvas
                segments = create_segments_for_image(canvas_path, segments_dir, idx)
                progress.update(task2, advance=1)
                return segments
            
            # Create segments in parallel (but limit workers to avoid overload)
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                segment_results = list(executor.map(create_segments, successful_canvas))
        
        # Flatten the list of segments
        for segments in segment_results:
            all_segments.extend(segments)
        
        console.print(f"Successfully created [green]{len(all_segments)}[/green] video segments")
        
        if not all_segments:
            console.print("[red]No video segments were created successfully.[/red]")
            return
        
        # Step 3: Randomly combine all segments
        output_filename = f"random_slideshow_{int(time.time())}.mp4"
        final_output_path = os.path.join(input_directory, output_filename)
        
        with console.status("[bold yellow]Randomly shuffling and combining all segments..."):
            success = combine_videos_randomly(all_segments, final_output_path, temp_dir)
        
        if success:
            # Calculate final statistics
            end_time = time.time()
            total_time = end_time - start_time
            total_video_duration = len(all_segments) * SEGMENT_DURATION
            total_image_time = len(successful_canvas) * SEGMENTS_PER_IMAGE * SEGMENT_DURATION
            
            # Show completion summary
            console.print("\n[bold green]Random Slideshow Creation Complete![/bold green]")
            
            summary_info = f"""[cyan]Images processed:[/cyan] {len(successful_canvas)}
[cyan]Total segments created:[/cyan] {len(all_segments)}
[cyan]Segment duration:[/cyan] {SEGMENT_DURATION} seconds each
[cyan]Total video duration:[/cyan] {total_video_duration} seconds ({total_video_duration//60}m {total_video_duration%60}s)
[cyan]Each image appears for:[/cyan] {SEGMENTS_PER_IMAGE * SEGMENT_DURATION} seconds total (in {SEGMENT_DURATION}s chunks)
[cyan]Processing time:[/cyan] {total_time:.1f} seconds
[cyan]Output file:[/cyan] {final_output_path}
[cyan]Temp directory:[/cyan] {temp_dir}"""
            
            console.print(Panel(summary_info, title="Summary"))
            
            # Show random order preview
            console.print(f"\n[yellow]Video structure:[/yellow] Images appear randomly every {SEGMENT_DURATION} seconds")
            console.print(f"[yellow]Each image gets exactly {SEGMENTS_PER_IMAGE * SEGMENT_DURATION} seconds of total screen time[/yellow]")
            
            # Ask user if they want to clean up temp files
            cleanup_choice = input("\nDo you want to keep temporary files? (y/n): ").strip().lower()
            if cleanup_choice in ['n', 'no']:
                with console.status("[bold yellow]Cleaning up temporary files..."):
                    shutil.rmtree(temp_dir)
                console.print("[green]Temporary files cleaned up.[/green]")
            else:
                console.print(f"[yellow]Temporary files kept in:[/yellow] {temp_dir}")
        
        else:
            console.print("[red]Failed to combine video segments into final slideshow.[/red]")
            
    except Exception as e:
        console.print("[red bold]Error during slideshow creation:[/red bold]")
        console.print(f"[red]{str(e)}[/red]")
        raise

def main():
    """Main entry point"""
    console.print("[bold cyan]Random Segment Slideshow Video Generator[/bold cyan]")
    console.print("Creates a slideshow where each image appears in random 2-second segments\n")
    console.print(f"[yellow]Configuration:[/yellow]")
    console.print(f"- Each image split into [cyan]{SEGMENTS_PER_IMAGE}[/cyan] segments of [cyan]{SEGMENT_DURATION}[/cyan] seconds")
    console.print(f"- Segments are randomly shuffled for dynamic viewing")
    console.print(f"- Each image still gets [cyan]{SEGMENTS_PER_IMAGE * SEGMENT_DURATION}[/cyan] seconds total screen time\n")
    
    # Get input directory from user
    while True:
        try:
            input_dir = input("Enter the path to the folder containing images: ").strip().replace('\r', '').replace('\n', '')
            if input_dir.startswith('"') and input_dir.endswith('"'):
                input_dir = input_dir[1:-1]  # Remove quotes
            
            # Handle empty input
            if not input_dir:
                console.print("[red]Error: Please enter a valid path.[/red]")
                continue
            
            if not os.path.exists(input_dir):
                console.print(f"[red]Error: Directory not found: {input_dir}[/red]")
                continue
            if not os.path.isdir(input_dir):
                console.print(f"[red]Error: Path is not a directory: {input_dir}[/red]")
                continue
            break
            
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Operation cancelled by user.[/yellow]")
            return 1
        except Exception as e:
            console.print(f"[red]Input error: {e}[/red]")
            continue
    
    # Process the images
    try:
        process_images_to_random_slideshow(input_dir)
    except Exception as e:
        console.print(f"[red bold]Processing failed: {e}[/red bold]")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())