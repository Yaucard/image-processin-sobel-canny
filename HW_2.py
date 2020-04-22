import cv2
import numpy as np
 
img = cv2.imread("/home/pi/Pictures/zxc1.jpg", 0)
 
x = cv2.Sobel(img,cv2.CV_16S,1,0)
y = cv2.Sobel(img,cv2.CV_16S,0,1)
 
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
 
dst = cv2.addWeighted(absX,0.5,absY,0.5,0)

img = cv2.GaussianBlur(img,(3,3),0)
cny = cv2.Canny(img,50,150)

#cv2.imshow("S", img)
#cv2.imshow("absX", absX)
#cv2.imshow("absY", absY)
 
cv2.imshow("sobel", dst)
cv2.imshow("canny", cny)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
