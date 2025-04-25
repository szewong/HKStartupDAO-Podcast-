import os
import subprocess
from datetime import datetime

# Define the path to your audio folder
folder_path = 'audio'

# Get all mp4 files in the folder
mp4_files = [f for f in os.listdir(folder_path) if f.endswith(".mp4")]

if not mp4_files:
    print("No MP4 files found in the audio folder.")
    exit()

# Get the most recently created MP4 file
latest_file = None
latest_time = 0

for file in mp4_files:
    file_path = os.path.join(folder_path, file)
    file_time = os.path.getmtime(file_path)
    if file_time > latest_time:
        latest_time = file_time
        latest_file = file

# Create full paths for input (mp4) and output (mp3) files
mp4_file = os.path.join(folder_path, latest_file)
mp3_file = os.path.join(folder_path, os.path.splitext(latest_file)[0] + ".mp3")

print(f"Converting {latest_file} to MP3...")

# Run the ffmpeg command to extract audio and convert to mp3
command = ['ffmpeg', '-i', mp4_file, '-q:a', '0', '-map', 'a', mp3_file]

# Execute the command
subprocess.run(command, check=True)

print(f"Conversion complete! MP3 file saved at: {mp3_file}")