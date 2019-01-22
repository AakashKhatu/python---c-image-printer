# import cv2
# import numpy as np

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
# img = cv2.imread['emoji.png']
for color in RGB:
    r = color[0]/255.0
    g = color[1]/255.0
    b = color[2]/255.0
    M = max(r, g, b)
    m = min(r, g, b)
    c = M-m
    v = M
    if r == g and r == b:
        h = 0
        s = 0
        HSV.append([h, s, v])
        continue
    s = c/M
    if M == r:
        h = (60 * ((g-b)/c) + 6)
    elif M == g:
        h = (60 * ((b-r)/c) + 2)
    else:
        h = (60 * ((r-g)/c) + 4)
    HSV.append([h, s, v])
print(HSV)
