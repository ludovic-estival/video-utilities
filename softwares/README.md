# Softwares

## ffmpeg

[Link](https://ffmpeg.org/)

Upscale video to 4k: `ffmpeg -i input.mp4 -vf scale=3840:2160:flags=lanczos -c:v libx264 -preset slow -crf 20 output.mp4`

Mute video: `ffmpeg -i input -c copy -an output`

## yt-dlp

[Link](https://github.com/yt-dlp/yt-dlp)

Installation:
- Windows: `winget install ffmpeg`
- WSL: `sudo apt install ffmpeg`

Some commands:
- `yt-dlp.exe URL --cookies-from-browser BROWSER --no-playlist --list-formats`
- `yt-dlp.exe URL --cookies-from-browser BROWSER --no-playlist -f FORMAT`
- `yt-dlp.exe URL -x --audio-format mp3`


## Video/audio editing

[lossless-cut](https://github.com/mifi/lossless-cut)


## Player

[potplayer](https://potplayer.tv/)


## Internet Download Manager

[Internet Download Manager](https://www.internetdownloadmanager.com/)
