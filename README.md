# osu-video-mapper
osu! video mapper, maps any video in osu!

This script was used for doing a visualization of bad apple in osu!, in cs10, ar11 and 7fps.

This is a wip project, for now it only works with bw or greyscale videos, however you can use colored videos and the script will process it in bw - greyscale for creating an osu! beatmap.

In a future this will be able to do an 8-bit colored beatmap.

### Requirements
In order to run the script you need to install FFMPEG in your PATH, and install the library PIL in python, this by doing the command `pip install Pillow`.

### How does it work
First we have FFMPEG process any video and have it split into different frames, these frames get stored in a temporary folder. Then a python script will read all the frames and make a `.osu` file, and finally the temporary folder gets deleted.

You must execute `process_beatmap.sh` in a terminal (cmd, powershell, etc in windows) with 2 parameters, the first one must be your video directory and the second one an output directory refering to your .osu file.

Before executing you might want to edit `map_template.osu` as you wish for metadata, it's important that map_template is in the same folder as `make_bw_beatmap.py`

### Considerations
Since osu! is not optimized for showing more than 10000 hitcircles per second you must consider that your computer is capable of running such a monster, for reference running bad apple on a laptop with an Intel Core I5-10300H, 16GB of RAM DDR4 3200MHz made osu! consume 3GB of RAM while loading the map and took about 2-3 minutes to load completely. A medium-tier graphics card would ease rendering the beatmap.

Bad apple map (at 7fps) consists of nearly 580000 hitcircles in a timespan of 3 minutes and 37 seconds, so consider that converting a really long video is only doable for very low FPS values. I tried recording bad apple at 10fps, but osu! suddenly closed halfway through; I suppose it was some overflow related error.

Another important thing to consider is to not use any higher FPS value than 15, unless you're sure that there won't be a lot of hitcircles in a frame (ex: a black background would have no hitcircles)

I strongly recommend using a skin with no approach circles and misses, like `badapel.osk` in this repository.

Also remember that this is not complete so there might be some issues if you try to run this. You are free to change some parameters and modify some attibutes and functions for a different image processing (like adding filters)

### Contact
Since this is an osu! related project, if you wish to contact me then you can do it by messaging my [osu! profile](https://osu.ppy.sh/users/4282963)
