# read img

import cv2

img = cv2.imread("D:/Cell Data/4-Peninsula_Great_Room_1_600.jpg.webp")

resiedimg = cv2.resize(img, (400,400))


cv2.imshow("hey", img)
cv2.imshow("new", resiedimg)
 

cv2.waitKey(0)