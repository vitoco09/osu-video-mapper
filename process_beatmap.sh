#!/bin/bash

VID=$(realpath $1)
OUTPUT=$(realpath $2)
FPS=$3

set -e -x

mkdir workdir
cd workdir

ffmpeg -i $VID -vf scale=32:24,fps=$FPS image_%d.png

cd ..
python make_bw_beatmap.py ./workdir $OUTPUT $FPS

rm -r workdir