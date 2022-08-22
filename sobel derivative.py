import cv2
import numpy as np
from numpy import sqrt


img = cv2.imread("image.png")
img= cv2.resize(img, (500,500))
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("Orginal Image", img)

img1 = np.zeros_like(img)       #Create matrix for new values


for i in range (1,499,1):
    for j in range (1,499,1):
        Gy = (-1)*img[i-1,j-1]+ (-2)*img[i-1,j]+ (-1)*img[i-1,j+1]+  1*img[i+1,j-1]+ 2*img[i+1,j]+ 1*img[i+1,j+1]
        Gx = (-1)*img[i,j]+ (-2)*img[i,j-1]+ (-1)*img[i+1,j-1]+   1*img[i-1,j+1]+ 2*img[i,j+1]+ 1*img[i+1,j+1]
        G = sqrt(Gx**2+Gy**2)
        img1[i,j] = G

        
cv2.imshow("Derivative Sobel", img1)
cv2.waitKey(0)
