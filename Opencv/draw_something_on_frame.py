import cv2
import numpy as np

frame = np.zeros((500,500, 3), dtype= 'uint8')    #zeroes parameter-  height , Width and channels
# print(frame)

# to draw someting on image

cv2.line(frame,(100,50),(100,400), (153, 0, 15),4)   # it takes RGB color code
cv2.line(frame,(100,50),(400,50), (235, 2, 25),4)
cv2.line(frame,(400,50),(100,400), (3, 221, 255),4)


# to put a text in frame

cv2.putText(frame, "Draw Line", (100,30), 6, 2, (255, 255, 255), 1)


cv2.imshow("my frame", frame)

cv2.waitKey(0)