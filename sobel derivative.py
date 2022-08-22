import cv2
import numpy as np
from numpy import sqrt


img = cv2.imread("C:\\Users\Admin\Desktop\sobel.png")
img= cv2.resize(img, (501,501))          #501 uzunluk 3 e bölünür.
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("Orjinal", img)

img1 = np.zeros_like(img)       #Yeni değerleri girmek için boş matris oluşturduk.


for i in range (1,499,1):
    for j in range (1,499,1):
        Gy = (-1)*img[i-1,j-1]+ (-2)*img[i-1,j]+ (-1)*img[i-1,j+1]+  1*img[i+1,j-1]+ 2*img[i+1,j]+ 1*img[i+1,j+1]
        Gx = (-1)*img[i,j]+ (-2)*img[i,j-1]+ (-1)*img[i+1,j-1]+   1*img[i-1,j+1]+ 2*img[i,j+1]+ 1*img[i+1,j+1]
        G = sqrt(Gx**2+Gy**2)
        img1[i,j] = G



cv2.imshow("Derivative Sobel", img1)
cv2.imwrite("C:\\Users\Admin\Desktop\plaka\\derivative.jpg",img1)
cv2.waitKey(0)
