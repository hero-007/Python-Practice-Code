""" Color filtering means we can detect a particular range of color this can be used to remove a specific color from the
    pic or show only that specific color on the pic. This how we work with green screen we find that specific color and replace it
    with certain background."""


import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()        # here _ means that the function is returning a value but we don't require to use that value so we use _

    # hsv is a way of defining color just like BGR and HEX value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # reason we use hsv so that we can get range of color.
    # H - hue is color value
    # S - saturation is the intensity of the color
    # V - value which indicate how much of the color is in existance

    lower_green = np.array([80,20,100])
    upper_green = np.array([200,255,255])

    mask = cv2.inRange(hsv,lower_green,upper_green)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('msk',mask)
    cv2.imshow('result',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
