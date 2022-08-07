import numpy as np
import cv2 as cv

img = cv.imread('OpenCV/Python.jpg')
imgray = cv.imread('OpenCV/Python.jpg', 0)
thresh, bw = cv.threshold(imgray, 127, 255, cv.THRESH_BINARY)

imgb = cv.cvtColor(bw,cv.COLOR_GRAY2BGR)
resp = np.concatenate((img, imgb), axis = 1)
cv.imshow("Imagens", resp)
cv.waitKey(0)