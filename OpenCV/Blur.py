import cv2
import numpy as np
img = cv2.imread('OpenCV/taj_noise.jpg')
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1)
cv2.imshow("Comparativa", compare)
cv2.waitKey(0)