'''
     #------# ##### #### #      #         #######   #     #
     #      # #   # #    # #    #         #          #   #
     #      # ##### ###  #   #  #         #           # #
     #------# #     #    #      #         #######      #
              #     ####    

 Author Name:Tarun Sharma
 Problem Statement:Image Processing in Opencv
 
'''
#Different color conversion available for you
import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )

'''

For HSV, hue range is [0,179], saturation range is [0,255], and value range is [0,255]. Different software use different scales.
 So if you are comparing OpenCV values with them, you need to normalize these ranges.
'''
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,100,100])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()

#how to find hsv values to track???
green = np.uint8([[[255,0,0 ]]])
hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
print( hsv_green )


'''
Now you take [H-10, 100,100] and [H+10, 255, 255] as the lower bound and upper bound respectively. Apart from this method, 
you can use any image editing tools
like GIMP or any online converters to find these values, but don't forget to adjust the HSV ranges.

'''
