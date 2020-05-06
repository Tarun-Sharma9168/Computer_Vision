'''
     #------# ##### #### #      #         #######   #     #
     #      # #   # #    # #    #         #          #   #
     #      # ##### ###  #   #  #         #           # #
     #------# #     #    #      #         #######      #
              #     ####    

 Author Name:Tarun Sharma
 Problem Statement:Arithmetic Operation on images
 
'''
#image Addition
'''
There is a difference between OpenCV addition and Numpy addition. 
OpenCV addition is a saturated operation while Numpy addition is a modulo operation.
'''
import numpy as np
import cv2 as cv
x=np.uint8([250])
y=np.uint8([10])

#Saturated
print(cv.add(x,y)) #250+10=255

#Modulo Operation   250+10%256=4
print(x+y)

''' So there is a difference keep watch on it '''


#Image Blending

''' Image Blending
This is also image addition, but different weights are given to images in order to give a feeling of blending or transparency. 
Images are added as per the equation below:

                                   g(x)=(1−α)f0(x)+αf1(x)
               By varying α from 0→1, you can perform a cool transition between one image to another.

  Here I took two images to blend together. The first image is given a weight of 0.7 and the second image is given 0.3. cv.addWeighted() 
  applies the following equation to the image:

                                   dst=α⋅img1+β⋅img2+γ
                                  Here γ is taken as zero. 
'''

img1 = cv.imread('wolf.jpg')
cv.imshow('img1',img1)

img2 = cv.imread('flower.jpg')
cv.imshow('img2',img2)

img1.resize((800,800))
img2.resize((800,800))
cv.imshow('img1',img1)
cv.imshow('img2',img2)

dst = cv.addWeighted(img1,0.1,img2,0.9,0)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows() 