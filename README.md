Uses FFMPEG to extract frames from a bunch of videos.

## Usage

By default the application will lookup in the ./videos folder and output to the ./frames folder.


TODO:
Change implementation for faster extraction with:
```bash
time for i in {0..39} ; do ffmpeg -accurate_seek -ss `echo $i*60.0 | bc` -i input.mp4 -frames:v 1output-$i.png ; done
```

count frames:
ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 input.mp4
