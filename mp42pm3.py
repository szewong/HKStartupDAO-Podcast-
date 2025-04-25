import os
import subprocess

# Define the path to your folder
folder_path = '.'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".mp4"):
        # Create full paths for input (mp4) and output (mp3) files
        mp4_file = os.path.join(folder_path, filename)
        mp3_file = os.path.join(folder_path, os.path.splitext(filename)[0] + ".mp3")
        
        # Run the ffmpeg command to extract audio and convert to mp3
        command = ['ffmpeg', '-i', mp4_file, '-q:a', '0', '-map', 'a', mp3_file]
        
        # Execute the command
        subprocess.run(command, check=True)

print("Conversion complete!")

