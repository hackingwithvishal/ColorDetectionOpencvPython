import cv2
import numpy as np

cap = cv2.VideoCapture(r'C:\Users\Public\Videos\Sample Videos\Wildlife.wmv')

while True:
     _, frame = cap.read()
     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     # Detecting a Red Color
     low_red = np.array([161, 155, 84])
     high_red = np.array([179, 255, 255])
     red_mask = cv2.inRange(hsv_frame,low_red,high_red)
     red = cv2.bitwise_and(frame, frame, mask = red_mask)
     
     # Detecting a Blue Color
     low_blue = np.array([94, 80, 25])
     high_blue = np.array([126, 255, 255])
     blue_mask = cv2.inRange(hsv_frame,low_blue,high_blue)
     blue = cv2.bitwise_and(frame, frame, mask = blue_mask)

     # Detecting a Green Color
     low_green = np.array([25, 52, 72])
     high_green = np.array([102, 255, 255])
     green_mask = cv2.inRange(hsv_frame,low_green,high_green)
     green = cv2.bitwise_and(frame, frame, mask = green_mask)

     cv2.imshow('Frame', frame)
     cv2.imshow('Red', red)
     cv2.imshow('Blue', blue)
     cv2.imshow('Green', green)

     key = cv2.waitKey(1)
     if key == 27:
          break
     
                             
