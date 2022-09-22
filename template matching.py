import cv2 as cv
import numpy as np
import os

template = cv.imread('3.jpg', 0)
w, h = template.shape[::-1]

for image in os.listdir("C:\\Users\\Vignesh Ganesan\\OneDrive\\Documents\\Current Semester Notes\\Image Processing Lab\\Image Finder\\Images"):
    print(image)
    img_rgb = cv.imread('Images\{}'.format(image))
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    print(loc)
    if len(loc[0]) > 0:
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv.imshow('img_rgb', img_rgb)
        cv.waitKey(0)
