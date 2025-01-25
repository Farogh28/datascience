import cv2


img = cv2.imread("D:/Cell Data/images/ladakh/IMG20240920104804.jpg")

# cv2.imshow("image", img)


edges = cv2.Canny(img, 100,100)  #(10,10)

# cv2.imshow("edge detect", edges)

edge_resize = cv2.resize(edges,(400,500))


cv2.imshow("edge detect", edge_resize)


cv2.waitKey(0)