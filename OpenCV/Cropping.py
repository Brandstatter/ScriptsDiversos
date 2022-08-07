import numpy as np
import cv2 as cv

img = cv.imread('OpenCV/Python.jpg')

#2
crop = img[300:400, 200:250]

cv.imshow("Image", img)
cv.imshow("Image Cropada", crop)
cv.waitKey(0)