import numpy as np
import cv2
import os


def whatcolor(path, tc):
    rgb = cv2.imread(path)
    height, width, depth = rgb.shape
    newWidth = 200
    newHeight = (newWidth * height) // width
    rgb = cv2.resize(rgb, (newWidth, newHeight))

    hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)

    lower_g = np.array([50, 100, 100])
    upper_g = np.array([70, 255, 255])
    #
    lower_y = np.array([15, 100, 100])
    upper_y = np.array([35, 255, 255])
    #
    lower_r0 = np.array([0, 100, 100])
    upper_r0 = np.array([15, 255, 255])
    #
    lower_r1 = np.array([160, 100, 100])
    upper_r1 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_g, upper_g)
    mask2 = cv2.inRange(hsv, lower_y, upper_y)
    mask3 = cv2.inRange(hsv, lower_r0, upper_r0)
    mask4 = cv2.inRange(hsv, lower_r1, upper_r1)
    mask = cv2.bitwise_or(mask1, mask2, mask3, mask4)
    hist = cv2.calcHist([hsv], [0], mask, [255], [0, 255])
    i = hist.argmax()
    if 0 <= i <= 14 or 170 <= i <= 180:
        c = 'red'
    if 15 <= i <= 35:
        c = 'yellow'
    if 50 <= i <= 70:
        c = 'green'
    print(path + " " +tc +" распознан как "+c + " - " + str(c == tc))


a = os.listdir('../../../data/traffic-light/red')
b = os.listdir('../../../data/traffic-light/yellow')
c = os.listdir('../../../data/traffic-light/green')

for p in a:
    whatcolor('../../../data/traffic-light/red/'+p, 'red')
for p in b:
    whatcolor('../../../data/traffic-light/yellow/'+p, 'yellow')
for p in c:
    whatcolor('../../../data/traffic-light/green/'+p, 'green')

