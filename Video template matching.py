import cv2 as cv
import numpy as np

template = cv.imread('4.png',0)
w, h = template.shape[::-1]
threshold = 0.8



vidcap = cv.VideoCapture('Helix.mp4')
success,img_rgb = vidcap.read()
count = 0
while success:
    
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

    loc = np.where( res >= threshold)
    flag = False
    for pt in zip(*loc[::-1]):
        flag = True
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    if flag:
        cv.imshow('img_rgb', img_rgb)
        cv.waitKey(0)
    
    success,img_rgb = vidcap.read()
    print('Read ',count,' frame: ', success)
    count += 1