# Video CLI made with Python

## Features

Features:
- extract subclip from a video
- screen recording (without sound)

## Installation

It's recommended to use a Python virtual environment: `python -m venv venv`

Activation on Linux: `source venv/bin/activate`

Activation on Windows: `.\venv\Scripts\activate` (use `Set-ExecutionPolicy Unrestricted -Scope Process`)

Install dependencies: `pip install -r requirements.txt`

You will also need [ffmpeg](https://www.ffmpeg.org/).

## Usage

Extract subclip: `python video.py extract-video VIDEO START END`

Example: `python video.py extract-video video.mp4 0.0 20.0`

You can use the option `--output` to change the output, it's `subclip.mp4` by default.

---

Record the screen: `python video.py record`

Options:
- `--output`: output file, `output.mp4` by default
- `--monitor`: monitor to record, `1` by default
- `--width` and `--height`: part of the screen to record, `1920` and `1080` by default
- `--fps`: FPS of the video, `30` by default

