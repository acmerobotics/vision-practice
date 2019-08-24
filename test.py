import cv2
import os
import numpy as np

yellow_min = np.array([15, 150, 0], np.uint8)
yellow_max = np.array([30, 255, 255], np.uint8)
kernel_size = 17
kernel = np.ones((kernel_size, kernel_size))

files = os.listdir("./in")

for file in files:
    file = "./in/" + file
    photo = cv2.imread(file)
    photo = cv2.resize(photo, (400, 300))
    photo = cv2.GaussianBlur(photo, (5, 5), 0)
    photo = cv2.cvtColor(photo, cv2.COLOR_BGR2HSV)

    photo = cv2.inRange(photo, yellow_min, yellow_max)

    photo = cv2.morphologyEx(photo, cv2.MORPH_CLOSE, kernel)
    photo = cv2.morphologyEx(photo, cv2.MORPH_OPEN, kernel)

    cv2.imshow('photo', photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




