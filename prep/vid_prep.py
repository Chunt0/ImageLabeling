import yt_dlp
import os
import re
import subprocess
import json
from pathlib import Path

# Define paths
url_file_path = './prep/url.txt'
vids_dir = './prep/vids/'

# Ensure output directory exists
os.makedirs(vids_dir, exist_ok=True)

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

def clip_video(vids_dir: str = "./prep/vids",
                           output_root: str = "./static/target",
                           height: int = 720,
                           crf: int = 18,
                           clip_duration: int = 4):
    for video in os.listdir(vids_dir):
        if not video.lower().endswith(".mp4"):
            continue

        base, ext = os.path.splitext(video)
        inp_path = os.path.join(vids_dir, video)
        tgt_dir = os.path.join(output_root, base)
        os.makedirs(tgt_dir, exist_ok=True)
        os.makedirs(f"./static/completed/{base}", exist_ok=True)

        # Get total duration of the video
        cmd_probe = [
            "ffprobe", "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            inp_path
        ]
        result = subprocess.run(cmd_probe, stdout=subprocess.PIPE, text=True, check=True)
        info = json.loads(result.stdout)
        total_duration = float(info["format"]["duration"])

        # Calculate number of segments
        n_segments = int(total_duration // clip_duration) + (1 if total_duration % clip_duration else 0)

        # Create clips
        out_template = os.path.join(tgt_dir, "%03d.mp4")

        ffmpeg_cmd = [
            "ffmpeg", "-hide_banner",
            "-i", inp_path,
            "-vf", f"scale=-2:{height}",
            "-c:v", "libx264", "-crf", str(crf),
            "-y",  # overwrite
            "-f", "segment",
            "-segment_time", str(clip_duration),
            "-reset_timestamps", "1",
            "-segment_format", "mp4",
            out_template
        ]

        print("Running:", " ".join(ffmpeg_cmd))
        subprocess.run(ffmpeg_cmd, check=True)

        # Create empty txt files for each clip
        for filename in os.listdir(tgt_dir):
            if filename.endswith('.mp4'):
                txt_path = os.path.join(tgt_dir, filename.replace('.mp4', '.txt'))
                if not os.path.exists(txt_path):
                    with open(txt_path, 'w') as f:
                        pass  # or write default info if needed

if __name__ == "__main__":
    print("Starting video downloads...")
    #download_videos()
    clip_video()
    print("\nDownload process completed!")
