import cv2

img = cv2.imread("C://Users//Farogh//Pictures//sticker.png")

cv2.imshow("First parameter", img)   # always 2 parameter (name of the frame, and 2nd para is variable name in which image path is stored)

cv2.waitKey(0)
