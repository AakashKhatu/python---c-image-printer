# import cv2
import numpy as np

RGB = [
    [0, 0, 0],
    [0, 0, 176],
    [0, 176, 0],
    [0, 177, 177],
    [176, 0, 0],
    [176, 0, 176],
    [171, 80, 0],
    [180, 180, 180],
    [80, 80, 80],
    [80, 80, 255],
    [83, 255, 83],
    [84, 255, 255],
    [255, 80, 80],
    [255, 82, 255],
    [255, 255, 84],
    [255, 255, 255],
]

HSV = []
for color in RGB:
    with color[0] as r, color[1] as g, color[2] as b:
        if r == g and r == b:
            v = max(r, g, b)
            h = 0
        else:
            v = max(r, g, b)
            h = np.arctan2((np.sqrt(3)*(g-b))/(2*r-g-b))
print(HSV)
