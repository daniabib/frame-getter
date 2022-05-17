import os
import subprocess

import typer

app = typer.Typer()

files = os.listdir('videos/')
print(files)
for file in files:
    query = f'ffmpeg -i videos/{file} -vf fps=1/5 -s 960x420 frames/{file}-out%04d.jpg'
    subprocess.run(query, shell=True)

if __name__ == '__main__':
    app()