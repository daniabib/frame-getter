import os
import subprocess
from typing import Optional

import typer

app = typer.Typer()

def main(input: Optional[str] = typer.Argument(None),
         fps:float = 1/5,
         size: str = "960x540") -> str:
    if input:
        query = f'ffmpeg -i {input} -r {fps} -s {size} frames/TEST-out%04d.jpg'
        subprocess.run(query, shell=True)
        raise typer.Exit()

    files = os.listdir('videos/')
    if not files:
        typer.echo("Videos folder is empty.\nInsert a video in the videos folder or specify an input.")
        raise typer.Exit(code=1)

    for file in files:
        if size:
            query = f'ffmpeg -i videos/{file} -r {fps} -s {size} frames/{file}-out%04d.jpg'
        else:
            query = f'ffmpeg -i videos/{file} -r {fps} frames/{file}-out%04d.jpg'
        subprocess.run(query, shell=True)
    raise typer.Exit()

if __name__ == '__main__':
    # app()
    typer.run(main)