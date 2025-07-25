"""Videos manipulations."""

import os
from typing_extensions import Annotated
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from rich.console import Console
import pyscreenrec
import typer

app = typer.Typer()
console = Console()

@app.command()
def extract_video(
    video: Annotated[str, typer.Argument(help='Video to extract a subclip from')],
    start: Annotated[str, typer.Argument(help='Start of the subclip in seconds')],
    end: Annotated[str, typer.Argument(help='End of the subclip in seconds')],
    output: Annotated[str, typer.Option(help='Output file')] = 'subclip.mp4'):
    """Extract a sublicp from a video."""
    ffmpeg_extract_subclip(video, float(start), float(end), outputfile=output)


@app.command()
def record(
    output: Annotated[str, typer.Option(help='Output file')] = 'output.mp4',
    monitor: Annotated[str, typer.Option(help='Monitor to record')] = '1',
    width: Annotated[str, typer.Option(help='Width of the video')] = '1920',
    height: Annotated[str, typer.Option(help='Height of the video')] = '1080',
    fps: Annotated[str, typer.Option(help='FPS of the video')] = '30'
):
    """Record the screen. Sound is not captured. Press ctrl+c to stop recording."""

    if os.path.exists(output):
        os.remove(output)

    recorder = pyscreenrec.ScreenRecorder()
    record_config = {
        'mon': int(monitor),
        'left': 0,
        'top': 0,
        'width': int(width),
        'height': int(height)
    }

    recorder.start_recording(output, int(fps), record_config)

    try:
        with console.status('Recording...'):
            while True:
                continue
    except KeyboardInterrupt:
        recorder.stop_recording()
        print('Finished')


if __name__ == '__main__':
    app()
