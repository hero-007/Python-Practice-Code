import numpy as np
import cv2
import os

os.chdir('C:\\Users\\HP\\Desktop\\open CV tutorial code')

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

# we can actually refrence a pixcel - image_name[x_coordinate,y_coordinate]

img[55,55] = [255,255,255]     # changing color of that particular pixcel 
px = img[55,55]
print(px)

# ROI - Region of Image - which is sub image of a image

"""roi = img[100:150,100:150] 
print(roi)"""

#img[100:150,100:150] = [0,0,0]          # this turns entire selected portio to black

watch_face = img[37:111,107:194]         # we store entire region of a watch in a variable 
img[0:74,0:87]=watch_face


cv2.imshow('image',img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

