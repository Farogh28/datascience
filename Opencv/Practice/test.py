import cv2
import numpy as np

# Basic image is gray image.(Black and white)

img = np.zeros((512,512,3))

# for line

cv2.line(img, pt1= (0,0), pt2= (512,512), color = (255,0,0))

# for rectangle
cv2.rectangle(img,pt1=(100,100),pt2= (300,300), color=(00, 250, 240), thickness= 3) # if thickness is -1 then it will be filled

# for circle

cv2.circle(img, center=(100,400), radius=50 , color= (204, 165, 24), thickness= -1)

# to add text

cv2.putText(img, "Hello", org=(100,400), fontFace= 3, fontScale= 4, color=(0,255,255))


cv2.imshow("Hello", img)

cv2.waitKey(0)  # Here '0' means for intinite period of time.