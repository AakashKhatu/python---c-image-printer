# ---------------------------------
# Get Hue and Lightness Value of
# the 16 colors in C
# ----------------------------------
import numpy as np
import json

RGB = {
    '0': [0, 0, 0],
    '1': [0, 0, 176],
    '2': [0, 176, 0],
    '3': [0, 177, 177],
    '4': [176, 0, 0],
    '5': [176, 0, 176],
    '6': [171, 80, 0],
    '7': [180, 180, 180],
    '8': [80, 80, 80],
    '9': [80, 80, 255],
    'A': [83, 255, 83],
    'B': [84, 255, 255],
    'C': [255, 80, 80],
    'D': [255, 82, 255],
    'E': [255, 255, 84],
    'F': [255, 255, 255],
}

HSV = {}
for key, color in RGB.items():
    r = color[0]
    g = color[1]
    b = color[2]
    if r == g and r == b:
        v = max(r, g, b)
        h = 0
    else:
        v = max(r, g, b)
        h = np.arctan2(np.sqrt(3)*(g-b), 2*r-g-b)
    HSV[key] = [h, v]
HSV.sort()
data = {
    'RGB': RGB,
    'HSV': HSV,
}

with open("data.txt", 'w') as out:
    json.dump(data, out, indent=4)
