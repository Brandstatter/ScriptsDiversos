import numpy as np
import cv2 as cv

img = cv.imread('OpenCV/Python.jpg')

#1
print("Altura " + str(img.shape[0]))
print("Largura " + str(img.shape[1]))
print("Canais " + str(img.shape[2]))