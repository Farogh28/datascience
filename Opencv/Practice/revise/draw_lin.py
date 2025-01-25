import cv2
import numpy as np

img = np.zeros((500,500,3), dtype = "uint8")

cv2.line(img, (200,200),(500,500),(122,23,42),5)

cv2.line(img, (100,200),(10,50),(12,25,155), 6)

cv2.imshow("blank img", img)

cv2.waitKey(0)