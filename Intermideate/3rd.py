import cv2
import numpy as np

pic = cv2.imread('im.jpg', 0)

matrix = (7,7)
blur = cv2.GaussianBlur(pic, matrix, 0)
cv2.imshow('GaussianBlur', blur)
cv2.waitKey()
cv2.destroyAllWindows()

##matrix = 3
##blur = cv2.medianBlur(pic, matrix)
##cv2.imshow('medianBlur', blur)
##cv2.waitKey()
##cv2.destroyAllWindows()
