import cv2

img = cv2.imread("D:/Cell Data/images/ladakh/IMG20240920104804.jpg")

cv2.imshow("blur", img)

blured_img= cv2.GaussianBlur(img, (21,21),0)

cv2.imshow(blured_img, blured_img)

cv2.waitKey(0)