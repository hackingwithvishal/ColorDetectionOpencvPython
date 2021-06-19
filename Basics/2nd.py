import cv2
img = cv2.imread('im.jpg')
img = cv2.imwrite('Image.png',img)
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
