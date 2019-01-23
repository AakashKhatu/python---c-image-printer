import json
import cv2

def RGBtoHSV(r, g, b):
    if r == g and r == b:
        v = max(r, g, b)
        h = 0
    else:
        v = max(r, g, b)
        h = np.arctan2(np.sqrt(3)*(g-b), 2*r-g-b)

with open('data.txt', 'r') as file:
    colors = json.load(file)

img = cv2.imread("smile.png")
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
for x in img:
    for y in x:
        print(y)
