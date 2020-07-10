import cv2
import os
import numpy as np
import math
from enum import Enum

yellow_min = np.array([15, 150, 0], np.uint8)
yellow_max = np.array([30, 255, 255], np.uint8)
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size))


class GoldLocation(Enum):

    LEFT = True
    CENTER = True
    RIGHT = True


files = os.listdir("./in")

for file in files:
    file = "./in/" + file
    photo = cv2.imread(file)
    photo = cv2.resize(photo, (400, 300))
    img = cv2.GaussianBlur(photo, (5, 5), 0)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img = cv2.inRange(img, yellow_min, yellow_max)

    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(photo, contours, -1, (255, 0, 0), 5)

    def score(ellipse):
        _, (major, minor), _ = ellipse
        return (major/2 * minor/2) * math.pi

    ellipsis = [cv2.fitEllipse(contour) for contour in contours]
    center, _, _ = max(ellipsis, key=score)
    print(center)

    if (0, _) <= center <= (151, _):
        location = GoldLocation.LEFT
        print('Left')
    elif (151, _) <= center <= (275, _):
        location = GoldLocation.CENTER
        print('Center')
    else:
        location = GoldLocation.RIGHT
        print('Right')

    cv2.imshow('photo', photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




