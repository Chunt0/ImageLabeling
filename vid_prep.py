import yt_dlp
import os
import subprocess
from pathlib import Path

# Define paths
url_file_path = './prep/url.txt'
vids_dir = './prep/vids/'
clips_dir = './prep/clips'

# Ensure output directory exists
os.makedirs(vids_dir, exist_ok=True)
os.makedirs(clips_dir, exist_ok=True)

# Configure yt-dlp options
ydl_opts = {
    'format': 'best',  # Download best quality
    'outtmpl': os.path.join(vids_dir, '%(title)s.%(ext)s'),  # Output template
    'ignoreerrors': True,  # Skip videos that fail
    'no_warnings': True,  # Don't print warnings
}

def download_videos():
    # Read URLs from file
    try:
        with open(url_file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File not found at {url_file_path}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    if not urls:
        print("No URLs found in the file")
        return

    # Initialize yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Download each video
        for i, url in enumerate(urls, 1):
            try:
                print(f"\nDownloading video {i} of {len(urls)}")
                print(f"URL: {url}")
                ydl.download([url])
            except Exception as e:
                print(f"Error downloading {url}: {e}")

def clip_video()
for video in os.listdir(input_dir):
    if video.endswith('.mp4'):
        # Get the base name of the video file without extension
        base_name = os.path.splitext(video)[0]
        
        # Construct the input and output file paths
        input_path = os.path.join(input_dir, video)
        output_path = os.path.join(output_dir, f"{base_name}_clip_%03d.mp4")

        # Use ffmpeg to split the video into 4-second clips, no audio, scaled to 720p height
        subprocess.run([
            'ffmpeg', '-i', input_path, '-vf', 'scale=-1:720', '-an', '-c:v', 'libx264', '-crf', '18',
            '-f', 'segment', '-segment_time', '4', '-reset_timestamps', '1', output_path
        ])


if __name__ == "__main__":
    print("Starting video downloads...")
    download_videos()
    print("\nDownload process completed!")
