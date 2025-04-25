# HK Startup DAO Podcast

Repository for managing podcast audio files for the HK Startup DAO podcast.

## Workflow

1. After each show, download the raw MP4 file from Clubhouse
2. Place the MP4 file in the `audio` directory
3. Run the conversion script to create MP3 files:
   ```
   python mp42pm3.py
   ```
4. Upload the generated MP3 file to Spotify
5. Apple Podcast will automatically pick up the show from Spotify

## Requirements

- Python 3
- ffmpeg (must be installed and available in PATH)

## Script Details

The `mp42pm3.py` script automatically converts all MP4 files in the current directory to MP3 format using ffmpeg. The script preserves audio quality during the conversion process.