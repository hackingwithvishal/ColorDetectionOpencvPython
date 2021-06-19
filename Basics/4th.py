##import numpy as np
##import cv2
##pic = np.zeros((500,500,3),dtype = 'uint8')
##cv2.line(pic,(450,350),(400,400),(0,0,255))
##cv2.imshow('dark', pic)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##     
import numpy as np
import cv2
pic=np.zeros((700,1300,3), dtype='uint8')
cv2.line(pic,(150,350),(300,350),(0,0,255),3)
cv2.imshow('dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
