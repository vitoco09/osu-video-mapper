import sys
import os
from PIL import Image

# WORKDIR = 'D:/projects/osu-video-mapper/workdir'
# BEATMAP_OUTPUT = 'D:/projects/osu-video-mapper/valecallampalacueca.osu'
# FPS = 20

WORKDIR = sys.argv[1]
BEATMAP_OUTPUT = sys.argv[2]
FPS = int(sys.argv[3])
NUM_FRAMES = len([name for name in os.listdir(WORKDIR) if os.path.isfile(os.path.join(WORKDIR, name))])

# Value in ms.
FRAME_PERIOD = 1000/FPS

# Offset, for reference in bad apple is 1337ms.
OFFSET = 1337

# Convert mode, bw: '1', grayscale: 'L', rgb: 'rgb'
CONVERT_MODE = '1'

hitcircles = []

for frame in range(NUM_FRAMES):

    current_frame = Image.open(WORKDIR + f'/image_{frame+1}.png')
    # We transform it to black and white, not the same as greyscale.
    current_frame_converted = current_frame.convert(CONVERT_MODE)  # Either 0 for black or 255 for white

    for i in range(32):     # CS10 max width:  32
        for j in range(24): # CS10 max height: 24

            pixel = current_frame_converted.getpixel((i,j))

            # If you try to use rgb you must change this
            if pixel > 128:  # White-ish
                hitcircle = f'{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},1,0,0:0:0:0:'
                hitcircles.append(hitcircle)

circles = '\n'.join(hitcircles)

with open('templates/map_bw_template.osu', 'r') as template:
    BEATMAP_CONTENT = template.read()

with open(BEATMAP_OUTPUT, 'w') as f:
    f.write(BEATMAP_CONTENT + circles)
    print('Done!')
