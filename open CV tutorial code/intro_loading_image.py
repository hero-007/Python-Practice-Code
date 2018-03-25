""" openCV is a library which is used for performing image analysis and video analysis """
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('C:\\Users\\HP\\Desktop\\open CV tutorial code')
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)


""" Alpha : is the degree of opaqueness
    image analysis is generally performed on gray scale because it is more simplified as it has no alpha.

    IMREAD_COLOR = 1
    IMREAD_UNCHANGED = -1
    IMREAD_UNCHANGED = 0
    """
cv2.imshow('watch_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('gray_watch.jpg',img)       # this is used for saving the image 
""" Displaying image using matplotlib 
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()
"""
    
