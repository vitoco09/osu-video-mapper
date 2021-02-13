import sys
import os
from PIL import Image

WORKDIR = 'D:/osu-video-mapper/workdir'
BEATMAP_OUTPUT = 'D:/Program Files/osu!/Songs/beatmap-637480869421055243-Masayoshi_Minoshima_-_Bad_Apple_feat._nomico_-_Touhou_PV_iichan (1)/badapel - badapel (vitoco) [badapel].osu'
FPS = 5

# WORKDIR = sys.argv[1]
# BEATMAP_OUTPUT = sys.argv[2]
# FPS = int(sys.argv[3])
NUM_FRAMES = len([name for name in os.listdir(WORKDIR) if os.path.isfile(os.path.join(WORKDIR, name))])

# Value in ms.
FRAME_PERIOD = 1.5*1000/FPS

# Offset, if needed.
OFFSET = 0

# Convert mode, bw: '1', grayscale: 'L', rgb: 'rgb'
CONVERT_MODE = 'RGB'

hitcircles = []

# We need the info of the last hitcircle in every pixel
# 0: Red, 1: Green, 2: Blue, 3: Cyan, 4: Magenta, 5: Yellow,
# 6: White, 7: Grey
COMBO_COLOUR = -1

color_map = {'red':(1, 5, 21, 37, 53, 68, 85, 101, 1),
    'green':(101, 1, 5, 21, 37, 53, 68, 85, 1),
    'blue':(85, 101, 1, 5, 21, 37, 53, 68, 1),
    'cyan':(68, 85, 101, 1, 5, 21, 37, 53, 1),
    'magenta':(53, 68, 85, 101, 1, 5, 21, 37, 1),
    'yellow':(37, 53, 68, 85, 101, 1, 5, 21, 1),
    'white':(21, 37, 53, 68, 85, 101, 1, 5, 1),
    'grey':(5, 21, 37, 53, 68, 85, 101, 1, 1)}

for frame in range(NUM_FRAMES):

    current_frame = Image.open(WORKDIR + f'/image_{frame+1}.png')
    
    current_frame_converted = current_frame.convert(CONVERT_MODE)

    for i in range(32):     # CS10 max width:  32
        for j in range(24): # CS10 max height: 24

            # pixel = tuple(r, g, b)
            pixel = current_frame_converted.getpixel((i,j))

            if pixel[0] < 5 and pixel[1] < 5 and pixel[2] < 5: # Pure Black
                continue

            if pixel[0] > 128 and pixel[1] < 128 and pixel[2] < 128: # Red
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['red'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 'red'
                COMBO_COLOUR = 0

            elif pixel[0] < 78 and pixel[1] > 228 and pixel[2] < 228: # Green
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['green'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 'red'
                COMBO_COLOUR = 1

            elif pixel[0] < 128 and pixel[1] < 128 and pixel[2] > 128: # Blue
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['blue'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 'red'
                COMBO_COLOUR = 2

            elif pixel[0] < 128 and pixel[1] > 128 and pixel[2] > 128: # Cyan
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['cyan'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 'red'
                COMBO_COLOUR = 3

            elif pixel[0] > 128 and pixel[1] < 128 and pixel[2] > 128: # Magenta
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['magenta'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 'red'
                COMBO_COLOUR = 4

            elif pixel[0] > 128 and pixel[1] > 128 and pixel[2] < 128: # "Yellow"
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['yellow'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 'red'
                COMBO_COLOUR = 5

            elif pixel[0] > 128 and pixel[1] > 128 and pixel[2] > 128: # White
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['white'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 'red'
                COMBO_COLOUR = 6

            else:                                                      # Grey
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['grey'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 'red'
                COMBO_COLOUR = 7
            
            

circles = '\n'.join(hitcircles)

with open('templates/map_template.osu', 'r') as template:
    BEATMAP_CONTENT = template.read()

with open(BEATMAP_OUTPUT, 'w') as f:
    f.write(BEATMAP_CONTENT + circles)
    print('Done!')
