'''
     #------# ##### #### #      #         #######   #     #
     #      # #   # #    # #    #         #          #   #
     #      # ##### ###  #   #  #         #           # #
     #------# #     #    #      #         #######      #
              #     ####    

 Author Name:Tarun Sharma
 Problem Statement:Geometrical transformation
 
'''
import numpy as np
import cv2 as cv 
import matplotlib.pyplot as plt 
ch=int(input())
if(ch ==1): 
  img = cv.imread('opencv.png')
  res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)
  #OR
  height, width = img.shape[:2]
  res = cv.resize(img,(width//2, height//2), interpolation = cv.INTER_CUBIC)
  while True:
    cv.imshow('img',res)
    key=cv.waitKey(0)
    if key==ord('q'):
       break
  cv.destroyAllWindows()

elif(ch==2):
  #Translation
  img = cv.imread('messi.jpg',0)
  rows,cols = img.shape
  M = np.float32([[1,0,100],[0,1,50]])
  dst = cv.warpAffine(img,M,(cols,rows))
  cv.imshow('img',dst)
  cv.waitKey(0)
  cv.destroyAllWindows()
#Rotation  
elif(ch ==3):
    img = cv.imread('messi.jpg',0)
    rows,cols = img.shape
    # cols-1 and rows-1 are the coordinate limits.
    M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    #print(M)
    dst = cv.warpAffine(img,M,(cols,rows))
    cv.imshow('res',dst)
    cv.waitKey(0)
    cv.destroyAllWindows()
elif(ch==4):
    #import matplotlib as plt
    img = cv.imread('grid.png')
    rows,cols,ch = img.shape
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv.getAffineTransform(pts1,pts2)
    dst = cv.warpAffine(img,M,(cols,rows))
    
    plt.subplot()
    plt.imshow(img)
    plt.title('Input')
    plt.subplot()
    plt.imshow(dst)
    plt.title('Output')
    plt.show()
  
elif(ch == 5):
    img = cv.imread('grid2.jpg')
    rows,cols,ch = img.shape
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(300,300))  
    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()       
  
      
  