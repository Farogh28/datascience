
# Sketch = load > convet into gray > blur img> and then convert into sketch by dividing it and use Scale parameter in last 


import cv2 

img = cv2.imread("D:/Cell Data/images/ladakh/IMG20240921131505.jpg")
res_im = cv2.resize(img, (400,500))
# cv2.imshow("hjty", res_im)

gray = cv2.cvtColor(res_im, cv2.COLOR_BGR2GRAY)
# cv2.imshow("new", gray)


invert_img = 255- gray
# cv2.imshow("inverted ", invert_img)

blur_img = cv2.GaussianBlur(invert_img, (41,41),0)
# cv2.imshow("blured", blur_img)

blur_invert = 255- blur_img
# cv2.imshow("blur_invert", blur_invert) 

sketch= cv2.divide(gray, blur_invert, scale= 140)
cv2.imshow("sketch", sketch)

# --------------------------------------To SAVE a IMAGE*************************************

# to Save an img

# cv2.imwrite("sketch_image.png", sketch)

# ----------------------------------

cv2.waitKey(0)