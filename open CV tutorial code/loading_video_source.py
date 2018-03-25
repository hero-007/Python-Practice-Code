""" In this module we'll see how to interact with a videofile from a webcam or a videofile
with openCv"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)   # 0 here represent the webcam that we are using it can be 1 if two webcam are attached to the system
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # we apply change bgr format of normal video feed to grayscale and display that in a new window
    out.write(frame)
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)                         # showing the frame in which grayscale video feed is running

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break


cap.release()       # this function releases the webcam because once the work is done we need to free the webcam else we cannot use it somewhere else
out.release()
cv2.destroyAllWindows()
