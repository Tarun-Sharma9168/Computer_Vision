'''
     #------# ##### #### #      #         #######   #     #
     #      # #   # #    # #    #         #          #   #
     #      # ##### ###  #   #  #         #           # #
     #------# #     #    #      #         #######      #
              #     ####    

 Author Name:Tarun Sharma
 Problem Statement:Handling the mouseclick events by drawing circle at each double click...
'''

#importing the libraries
import cv2 as cv
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )


import numpy as np
import cv2 as cv

# mouse callback function
# defining of the function of the action happened after the event occur 
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),0)#-1 means filled 0 means not filled 

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
#naming the window
cv.namedWindow('image')
#setting the mousecallback
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
#destroy all windows made 
cv.destroyAllWindows()
