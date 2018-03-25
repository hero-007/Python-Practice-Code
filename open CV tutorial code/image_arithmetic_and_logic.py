import numpy as np
import cv2
import os

os.chdir('C:\\Users\\HP\\Desktop\\open CV tutorial code')

#img1 = cv2.imread('sample_img1.png')
#img2 = cv2.imread('sample_img2.png')

#add = img1+img2                 # this operation just overlaps both the images
#add = cv2.add(img1,img2)         # this add() adds the individual pixel BGR values
#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0) #cv2.addWeighted(img1,weight_value_of_image_1, img2,weight_value_of_image_2, gamma_value)
#cv2.imshow('add',weighted)


logo = cv2.imread('logo.png')
img = cv2.imread('sample_img1.png')

rows,cols,channels = logo.shape
roi = logo[0:rows,0:cols]

logo2gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

ret,mask = cv2.threshold(logo2gray,220,255,cv2.THRESH_BINARY_INV)   #threshold(image_to_apply,threshold_value,max_threshold)
# The above line means that if the pixel value is above threshold_value than it will be converted to 255 (white) if it is below threshold_value than it'll be converted to black(0)
#cv2.THRESH_BINARY_INV - inverse of the above statement because of INV

mask_inv = cv2.bitwise_not(mask)

logo_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img_fg = cv2.bitwise_and(img,img,mask=mask)
dst = cv2.add(logo_bg,img_fg)
logo[0:rows,0:cols] = dst

cv2.imshow('image',logo)
cv2.waitKey(0)
cv2.destroyAllWindows()
