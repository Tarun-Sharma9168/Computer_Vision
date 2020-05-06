'''
     #------# ##### #### #      #         #######   #     #
     #      # #   # #    # #    #         #          #   #
     #      # ##### ###  #   #  #         #           # #
     #------# #     #    #      #         #######      #
              #     ####    

 Author Name:Tarun Sharma
 Problem Statement:Smoothing Images with some many different filters..keep exploring on official opencv documentation
 
'''

#Average filtering 
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('wolf.jpg')
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


#Again average filtering using the blur function
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('opencv.png')
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#Now using the Gaussian Binding or mainly using the gaussian Kernel
img = cv.imread('car.png')
blur = cv.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()



#Now we are using the median blurring technique effectively work on salt and pepper noised image..
img = cv.imread('salt.jpeg')
median = cv.medianBlur(img,5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()



#Bilateral filtering 
img = cv.imread('vert.jpg')
blur = cv.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

