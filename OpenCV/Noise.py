import cv2
import numpy as np

img = cv2.imread('OpenCV/taj_noise.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0)
print(suave.shape)
canny1 = cv2.Canny(suave, 20, 120)
imgs_concat = np.concatenate((gray, canny1), axis=1)
cv2.imshow('taj_noise',imgs_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()