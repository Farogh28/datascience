import cv2


img = cv2.imread("D:/Cell Data/images/ladakh/IMG20240920104804.jpg")


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resize_gray_img = cv2.resize(4000)
cv2.imshow()

blur_mg = cv2.GaussianBlur(gray_img, (49,49),0)


detect_edges = cv2.Canny(blur_mg, 100,100)
cv2.imshow()