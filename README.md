# osu-video-mapper
osu! black and white video mapper, maps any black and white video in osu!

This script was used for doing a visualization of bad apple in osu!, in cs10, ar11 and 7fps.

This is a wip project, for now it only works with bw or greyscale videos, however you can use colored videos and the script will process it in bw - greyscale for creating an osu! beatmap.

In a future this will be able to do an 8-bit colored beatmap.

### Requirements
In order to run the script you need to install FFMPEG in your PATH, and install the library PIL in python, this by doing the command pip install Pillow.

### How does it work
First we have FFMPEG process any video and have it split into different frames, then a python script will read all the frames and make a .osu file.
