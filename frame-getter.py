import os
import subprocess
import re
from typing import Optional

import typer


def rename_files(path='videos/'):
    regex = r'[^a-zA-Z0-9.-]'

    files = os.listdir(path)
    for file in files:
        new_name = re.sub(regex, "", file)
        try:
            os.rename(file, new_name)
        except:
            os.rename(f"{path}{file}", f"{path}{new_name}")

    return os.listdir(path)


def main(input: Optional[str] = typer.Argument(None),
         fps: float = 1/5,
         size: str = "960x540"):

    if input:
        query = f'ffmpeg -i {input} -r {fps} -s {size} frames/TEST-out%06d.jpg'
        subprocess.run(query, shell=True)
        raise typer.Exit()

    files = rename_files()

    if not files:
        typer.echo(
            "Videos folder is empty.\nInsert a video in the videos folder or specify an input.")
        raise typer.Exit(code=1)
        

    for file in files:
        if size:
            query = f'ffmpeg -i videos/{file} -r {fps} -s {size} frames/{file}-out%06d.jpg'
        else:
            query = f'ffmpeg -i videos/{file} -r {fps} frames/{file}-out%06d.jpg'
        subprocess.run(query, shell=True)
    raise typer.Exit()


if __name__ == '__main__':
    typer.run(main)
