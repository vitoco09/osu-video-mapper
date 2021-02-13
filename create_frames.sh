#!/bin/bash

VID=$(realpath $1)
FPS=$2

set -e -x

mkdir workdir
cd workdir

ffmpeg -i $VID -vf scale=32:24,fps=$FPS image_%d.png