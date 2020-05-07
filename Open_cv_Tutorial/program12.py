'''
     #------# ##### #### #      #         #######   #     #           
     #      # #   # #    # #    #         #          #   #   
     #      # ##### ###  #   #  #         #           # #
     #------# #     #    #      #         #######      #
              #     ####    

 Author Name:Tarun Sharma
 Problem Statement:Morphological transformation erosion,dilation,opening and closing...
 
'''

#Erosion is the basic one which decreases the thickness of the character
'''
The basic idea of erosion is just like soil erosion only, it erodes away the boundaries of foreground object 
(Always try to keep foreground in white). So what it does? The kernel slides through the image (as in 2D convolution).
A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1,
otherwise it is eroded (made to zero).

So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel.
So the thickness or size of the foreground object decreases or simply white region decreases in the image. 
It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects etc.

'''
import cv2 as cv
import numpy as np
import  matplotlib.pyplot as plt
img = cv.imread('Q.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Eroded')
plt.xticks([]), plt.yticks([])
plt.show()

'''
It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it 
increases the white region in the image or size of foreground object increases. Normally, 
in cases like noise removal, erosion is followed by dilation. Because, erosion removes white 
noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't 
come back, but our object area increases. It is also useful in joining broken parts of an object.


'''

#now comes to the dilation which is just opposite to the erosion
#increases the thickness little bit which is used at somany places..
img=cv.imread('S.jpg',0)
kernel = np.ones((5,5),np.uint8)
dilation = cv.dilate(img,kernel,iterations = 1)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation),plt.title('dilated')
plt.xticks([]), plt.yticks([])
plt.show()

'''
Opening is just another name of erosion followed by dilation. It is 
useful in removing noise, as we explained above. Here we use the function, cv.morphologyEx()
'''
#Opening which is just the erosion followed by the dilation
img=cv.imread('ope.jpeg',0)
kernel=np.ones([3,3],np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening),plt.title('opening')
plt.xticks([]), plt.yticks([])
plt.show()
'''
Closing is reverse of Opening, Dilation followed by Erosion.
It is useful in closing small holes inside the foreground objects, or small black points on the object.
'''
#Closing is just the opposite of the opening that is dilation followed by erosion..
img=cv.imread('a..jpg',0)
kernel=np.ones([5,5],np.uint8)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing),plt.title('closing')
plt.xticks([]), plt.yticks([])
plt.show()
