# import cv2


# capture = cv2.VideoCapture(0)
# # we need to convert vdo into frames to read the vdo

# while True:
#     is_True, frame = capture.read()   # isTru identify that vdo exists or not

#     cv2.imshow("title", capture)
#     # cv2.waitKey(10)

#     if cv2.waitKey(10) & 0xFF == ord("q"):
#         break
        



import cv2

capture = cv2.VideoCapture(0)   # 0 for web camera reading and to run a video pass the path of the vdo

while True:
    x,y = capture.read()

    # cv2.imshow("xyz", y)   # fie=rst param = and 2nd is condition 

    if cv2.waitKey(10) and 0xFF == ord("x"):
        break

