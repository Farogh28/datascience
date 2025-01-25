import cv2
import numpy as np

img = np.zeros((500,500,3), dtype= "uint8")

cv2.rectangle(img, (100,200),(400,300),(23,45,211), 6,5)

cv2.circle(img, (300,400),39, (23,32,222), 3)

cv2.circle(img, (200,20),123, (113,32,222), -1)

cv2.imshow("rect", img)

cv2.waitKey(0)