import cv2
import numpy as np

img = np.zeros((600,600, 3),dtype= "uint8" )   # (rows and columns and channels), datatype) #zero requires 3 arguments 

# new_img= cv2.imread(img)

#------------------------------Putting text on the image 

cv2.putText(img, "Text is here", (100,100),1, 3, (80,250,125), 6)   
            # image , "text", # jda
            # rows and columns, then-> style, -> font size ,  color should be BGR, thicknes 

cv2.imshow("text", img)

cv2.waitKey(0)


