# If image pixels are high and unable to place it or see the whole image so we can resize the image


import cv2

def resizingframe(frame,scale =0.25):   # Max Scaling is '1'  (Width, Heigh, and Channel)
    # pass
    width = int(frame.shape[0] * scale)    # Use type casting to convert value into integer
    height =int (frame.shape[1] * scale)   # Use type casting to convert value into integer

    dimension = (width,height)
    resized_image= cv2.resize(frame, dimension, interpolation= cv2.INTER_AREA)   # interpolation
    
    return

img = cv2.imread('image33.png')

resize_image= resizingframe(img)

resize_image_more = resizingframe(img, scale=0.10)

cv2.imshow('Original image', img)

cv2.waitKey(0)