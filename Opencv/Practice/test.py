
# Open Cv by CampusX (13 vdo playlist)


import cv2
import numpy as np

# # Basic image is gray image.(Black and white)

# # img = np.zeros((512,512,3))

# # for line

# cv2.line(img, pt1= (0,0), pt2= (512,512), color = (255,0,0))

# # for rectangle
# cv2.rectangle(img,pt1=(100,100),pt2= (300,300), color=(00, 250, 240), thickness= 3) # if thickness is -1 then it will be filled

# # for circle

# cv2.circle(img, center=(100,400), radius=50 , color= (204, 165, 24), thickness= -1)

# # to add text

# cv2.putText(img, "Hello", org=(100,400), fontFace= 3, fontScale= 4, color=(0,255,255))


# cv2.imshow("Hello", img)

# cv2.waitKey(0)  # Here '0' means for intinite period of time.

#--------------------------------------------------------------------------------

# Converting a RGB image to a gray scale image
img = cv2.imread("image33.png")

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # cv2.imshow('Real img', img)
# print (img_gray.shape)

# print (img.shape)
# cv2.imshow('Gray img', img_gray)

# cv2.waitKey(0)
#--------------------------------------------------------------------------------

#  Change th BGR of image

# img [Blue:Green:Red]

# img[:,:,0] = 0
# cv2.imshow('converting img', img)

# img2= img[:,:,2]
# cv2.imshow('img_2', img2)

# img3= img[:,:,1]
# cv2.imshow('img_3', img3)
#----------------------------------------------------Ploting image in single canvas
# imgblue = img[:,:,0]
# imggreen = img[:,:,1]
# imgred = img[:,:,2]

# new_img = np.hstack((imgblue,imggreen,imgred))   # To add all immage in one canvas

# cv2.imshow('new_img', new_img)

# cv2.waitKey(0)
#------------------------------------------------------------------ 
# #Make a project on this to resize the image, (and user can upload the img ) 

# Resizing image
# # Actual size= 445x791

# cv2.resize(image_path_holder,(width, Height))

# img_resize_big = cv2.resize(img,(700,1300))

# img_resize_small = cv2.resize(img,(250,450))

# cv2.imshow('Resize big', img_resize_big)

# cv2.imshow('Resize small', img_resize_small)
# ------------------------------------------------------------
# To half the size

# img_half = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

# cv2.imshow('Half',img_half)
# ------------------------------------------------------------
# cv2.imshow('Real', img)

# cv2.waitKey(0)
#-----------------------------------------------------------------------


# To flip the image 

img_flip_0 = cv2.flip(img, 0) # 0 > upside down, 1>

# cv2.imshow('Flip with 0', img_flip_0)

img_flip_1 = cv2.flip(img, 1)
# cv2.imshow('Flip with 1', img_flip_1)

img_flip_2 = cv2.flip(img, -1)
# cv2.imshow('Flip with 2', img_flip_2)

# cv2.imshow('Real', img)

new_img = np.hstack((img,img_flip_0,img_flip_1,img_flip_2)) 

new = cv2.resize(new_img,(1500,680))
cv2.imshow('All', new)

cv2.waitKey(0)



















