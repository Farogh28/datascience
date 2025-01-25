import cv2

img = cv2.imread("D:/Cell Data/images/ladakh/IMG20240920104804.jpg")


# cv2.imshow("color", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


resizedimg = cv2.resize(gray_img, (400,400))
resiedimg = cv2.resize(img, (400,400))


cv2.imshow("color", resizedimg)
cv2.imshow("gray", resiedimg)
# /////////////////////////////////////////

hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("hsv",hsv)
cv2.waitKey(0)