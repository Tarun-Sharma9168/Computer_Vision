'''
     #------# ##### #### #      #         #######   #     #         
     #      # #   # #    # #    #         #          #   #         
     #      # ##### ###  #   #  #         #           # #         
     #------# #     #    #      #         #######      #            
              #     ####                                        

 Author Name:Tarun Sharma
 Problem Statement:All about image processing in opencv and mostly here numpy as used...
                   Splitting ,border,slicing ,changing of the Pixel ,taking out the Region of the interest
 
'''
import numpy as np
import cv2 as cv

img=cv.imread('wolf.jpg')
#cv.imshow('img',img)


#Accessing the Pixel value as image is nothing but a matrix of a number
px=img[100,100]
#it gives you the value for all three pixel that is BGR
print(px)


#Accessing only the blue pixel value
single_channel_blue=img[100,100,0]
print(single_channel_blue)


#we can also modify the value of pixels
img[100,100] = [255,255,255]
print(img[100,1000])


#these raw getting of the pixel values are not recommended so use some optimize array functions
px=img.item(10,10,2)
print(px)


#modifying the Red Value
img.itemset((10,10,2),100)
print(img.item(10,10,2))




#getting the info about the data is crucial
print(img.shape)

#If you want the total number of pixels
print(img.size)

#if you want to know the datatype then
print(img.dtype)


#Splitting and Merging image channels
#that is if you want to work with different channels
b,g,r=cv.split(img)
img=cv.merge((b,g,r))

#selecting the Blue channel then
blue_channel=img[:,:,0]

#selecting the Red channel
red_channel=img[:,:,2]

#The important thing is split() method is very costly
#so try to avoid this function use array indexing....


#Most Important Making Borders for Images (Padding)
import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('wolf.jpg')

replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)

reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)

reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)

wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)

constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()




#Selecting the Region of Interest
ball=img[280:340,330:390]
img[273:333,100:160]=ball
print(img)

#while True:
#    key=cv.waitKey(0)
#    if(key == ord('q')):
#        break
#cv.destroyAllWindows()    