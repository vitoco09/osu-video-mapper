import sys
import os
from PIL import Image

WORKDIR = sys.argv[1]
BEATMAP_OUTPUT = sys.argv[2]
FPS = sys.argv[3]
NUM_FRAMES = len([name for name in os.listdir(WORKDIR) if os.path.isfile(os.path.join(WORKDIR, name))])

# Value in ms.
FRAME_PERIOD = 1000/FPS

hitcircles = []

for frame in range(NUM_FRAMES):

    current_frame = Image.open(WORKDIR + f'/image_{frame+1}.png')
    # We transform it to black and white, not the same as greyscale.
    current_frame_bw = current_frame.convert('1')  # Either 0 for black or 255 for white

    for i in range(32):     # CS10 max width:  32
        for j in range(24): # CS10 max height: 24

            bw = current_frame_bw.getpixel((i,j))

            if bw == 255:  # White
                hitcircle = f'{16*(i+1)},{16*(j+1)},{round(1337 + FRAME_PERIOD*frame)},1,0,0:0:0:0:'
                hitcircles.append(hitcircle)

circles = '\n'.join(hitcircles)

with open('map_template.osu', 'r') as template:
    BEATMAP_CONTENT = template.read()

with open(BEATMAP_OUTPUT, 'w') as f:
    f.write(BEATMAP_CONTENT + circles)
    print('Done!')
