# HK Startup DAO Podcast

Repository for managing podcast audio files for the HK Startup DAO podcast.

## Podcast Links

- Spotify: [https://open.spotify.com/show/6vHdLvls35yJgvBPtjIi0S](https://open.spotify.com/show/6vHdLvls35yJgvBPtjIi0S)
- Apple Podcasts: [https://podcasts.apple.com/us/podcast/香港創業島-hk-startup-dao-全球創業-科技-每週radio重播/id1734721713](https://podcasts.apple.com/us/podcast/香港創業島-hk-startup-dao-全球創業-科技-每週radio重播/id1734721713)

## Workflow

1. After each show, download the raw MP4 file from Clubhouse
2. Place the MP4 file in the `audio` directory
3. Run the conversion script to create MP3 files:
   ```
   python mp42pm3.py
   ```
4. Upload the generated MP3 file to Spotify at:
   [https://creators.spotify.com/pod/dashboard/episode/wizard](https://creators.spotify.com/pod/dashboard/episode/wizard)
5. Apple Podcast will automatically pick up the show from Spotify

## Script Details

The `mp42pm3.py` script automatically:
- Finds the most recent MP4 file in the `audio` directory
- Converts it to MP3 format using ffmpeg
- Saves the MP3 file in the same `audio` directory
- Preserves audio quality during the conversion process

## Requirements

- Python 3
- ffmpeg (must be installed and available in PATH)