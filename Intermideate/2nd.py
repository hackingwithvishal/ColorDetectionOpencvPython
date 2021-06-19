import cv2
import numpy as np

pic = cv2.imread('im.jpg', 0)

threshold_value = 50
(T_value, binary_threshold) = cv2.threshold(pic,
                                   threshold_value,255,cv2.THRESH_BINARY)
cv2.imshow('binary', binary_threshold)
cv2.waitKey()
cv2.destroyAllWindows()
