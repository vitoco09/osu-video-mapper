import sys
import os
from PIL import Image

def near(val1, val2, val3, epsilon):
    if abs(val1-val2) < epsilon:
        if abs(val2-val3) < epsilon:
            if abs(val1-val3) < epsilon:
                return True
            return False
        return False
    return False

WORKDIR = 'D:/osu-video-mapper/workdir'
BEATMAP_OUTPUT = 'D:/Program Files/osu!/Songs/beatmap-637480869421055243-Masayoshi_Minoshima_-_Bad_Apple_feat._nomico_-_Touhou_PV_iichan (1)/badapel - badapel (vitoco) [badapel].osu'
FPS = 3

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

color_map = {'red':(1, 101, 85, 69, 53, 37, 21, 5, 1),
    'green':(5, 1, 101, 85, 69, 53, 37, 21, 1),
    'blue':(21, 5, 1, 101, 85, 69, 53, 37, 1),
    'cyan':(37, 21, 5, 1, 101, 85, 69, 53, 1),
    'magenta':(53, 37, 21, 5, 1, 101, 85, 69, 1),
    'yellow':(69, 53, 37, 21, 5, 1, 101, 85, 1),
    'white':(85, 69, 53, 37, 21, 5, 1, 101, 1),
    'grey':(101, 85, 69, 53, 37, 21, 5, 1, 1)}

colors = ('red','green','blue','cyan','magenta','yellow','white','grey')
colors_rgb = ('255,0,0','0,255,0','0,0,255','0,255,255','255,0,255','255,255,0','255,255,255','127,127,127')
first = -1

for frame in range(50):

    current_frame = Image.open(WORKDIR + f'/image_{frame+1}.png')
    
    current_frame_converted = current_frame.convert(CONVERT_MODE)

    for i in range(32):     # CS10 max width:  32
        for j in range(24): # CS10 max height: 24

            # pixel = tuple(r, g, b)
            pixel = current_frame_converted.getpixel((i,j))

            if pixel[0] < 5 and pixel[1] < 5 and pixel[2] < 5: # Pure Black
                continue

            #print('mamarre mamarre', first)
            if pixel[0] > 128 and pixel[1] < 128 and pixel[2] < 128: # Red
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['red'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 0
                COMBO_COLOUR = 0

            elif pixel[0] < 128 and pixel[1] > 128 and pixel[2] < 128: # Green
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['green'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 1
                COMBO_COLOUR = 1

            elif pixel[0] < 128 and pixel[1] < 128 and pixel[2] > 128: # Blue
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['blue'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 2
                COMBO_COLOUR = 2

            elif pixel[0] < 128 and pixel[1] > 128 and pixel[2] > 128: # Cyan
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['cyan'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 3
                COMBO_COLOUR = 3

            elif pixel[0] > 128 and pixel[1] < 128 and pixel[2] > 128: # Magenta
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['magenta'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 4
                COMBO_COLOUR = 4

            elif pixel[0] > 128 and pixel[1] > 128 and pixel[2] < 128: # "Yellow"
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['yellow'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 5
                COMBO_COLOUR = 5

            elif pixel[0] > 128 and pixel[1] > 128 and pixel[2] > 128: # White
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['white'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 6
                COMBO_COLOUR = 6

            elif near(pixel[0], pixel[1], pixel[2], 50):               # Grey
                hitcircle = f"{16*(i+1)},{16*(j+1)},{round(OFFSET + FRAME_PERIOD*frame)},{color_map['grey'][COMBO_COLOUR]},0,0:0:0:0:"
                hitcircles.append(hitcircle)
                if COMBO_COLOUR == -1:
                    first = 7
                COMBO_COLOUR = 7



beatmap_combo_colors = {}
beatmap_combo_colors[colors[(first+7)%8]] = 'Combo1 : ' + colors_rgb[(first+7)%8]
beatmap_combo_colors[colors[first%8]] = 'Combo2 : ' + colors_rgb[first%8]
beatmap_combo_colors[colors[(first+1)%8]] = 'Combo3 : ' + colors_rgb[(first+1)%8]
beatmap_combo_colors[colors[(first+2)%8]] = 'Combo4 : ' + colors_rgb[(first+2)%8]
beatmap_combo_colors[colors[(first+3)%8]] = 'Combo5 : ' + colors_rgb[(first+3)%8]
beatmap_combo_colors[colors[(first+4)%8]] = 'Combo6 : ' + colors_rgb[(first+4)%8]
beatmap_combo_colors[colors[(first+5)%8]] = 'Combo7 : ' + colors_rgb[(first+5)%8]
beatmap_combo_colors[colors[(first+6)%8]] = 'Combo8 : ' + colors_rgb[(first+6)%8]


circles = '\n'.join(hitcircles)

with open('templates/map_template.osu', 'r') as template:
    BEATMAP_CONTENT = template.read()

with open(BEATMAP_OUTPUT, 'w') as f:
    f.write('')

with open(BEATMAP_OUTPUT, 'a') as f:
    f.write(BEATMAP_CONTENT)
    f.write(beatmap_combo_colors[colors[(first+7)%8]] + '\n')  # osu! is weird
    for i in range(7):
        f.write(beatmap_combo_colors[colors[(first+i)%8]] + '\n')
    f.write('\n' + '[HitObjects]' + '\n')
    f.write(circles)

    print('Done!')
