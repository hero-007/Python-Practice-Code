import numpy as np
import cv2
import os

os.chdir('C:\\Users\\HP\\Desktop\\open CV tutorial code')
img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,255,255),15)
#cv2.line(image_on_which_to_draw, starting_coordinate, ending_coordinate, line_color (BGR) format, line_width(value in px))

cv2.rectangle(img,(15,25),(200,150),(0,0,0 ),5)  
#cv2.rectangle(image_on_which_to_draw, top_left_coordinate, bottom_right_coordinate, line_color (BGR) format, line_width(value in px))

cv2.circle(img,(100,63),55,(0,0,255),5)  
#cv2.circle(image_on_which_to_draw, center_coordinate, radius , line_color (BGR) format, line_width(value in px))

pta = np.array([[10,5],[20,30],[70,20],[50,10]] ,np.int32 )
#pta = pta.reshape((-1,1,2))
cv2.polylines(img,[pta],True,(0,255,255),3 )    # True inidcate whether we want to connect the last point to first one or not here we want to connect them
# drawing a ploygon

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'here comes the text',(0,130),font,1,(200,200,200),2,cv2. LINE_AA)
#cv2.putText(img,'here comes the text',(text starting coordinates),font,size,(200,200,200),thickness,cv2. LINE_AA) 
# writing some text on the image

cv2.imshow('image',img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
