# import cv2

# cap = cv2.VideoCapture (0)

# while True:
#     done, frame = cap.read()

#     cv2.putText(frame, "Bhiyaaa", (10,10),10,4,(8, 156, 153), 4,cv2.FONT_HERSHEY_SIMPLEX)

#     cv2.imshow("Start Camera", frame)

#     cv2.waitKey(4)


import cv2

def resizingframe(frame,scale =0.25):   # Max Scaling is '1'  (Width, Heigh, and Channel)
    # pass
    width = int(frame.shape[0] * scale)    # Use type casting to convert value into integer
    height =int (frame.shape[1] * scale)   # Use type casting to convert value into integer

    dimension = (width,height)
    resized_image= cv2.resize(frame, dimension, interpolation= cv2.INTER_AREA)   # interpolation
    
    return

# cap = cv2.VideoCapture(0)
capture = cv2.VideoCapture("3141208-uhd_3840_2160_25fps.mp4")

while True:

    # done, frame = cap.read()

    istrue, frame = capture.read()
    # cv2.putText(frame, "My Camera", (10, 10), 10, 4, (52, 250, 250), 4)

    resized_frame = resizingframe(frame)

    # cv2.putText(frame, "My Cat", (50, 150), 20, 3, (51, 245, 29), 10, cv2.FONT_ITALIC)


    cv2.imshow("Resized Video", resized_frame)

    # cv2.imshow("Start Cemra", frame)

    if cv2.waitKey(20) & 0xFF == ord("x"):
        break

    cv2.waitKey(3)



# import cv2

# capture = cv2.imread("image33.png")    # image returns 3 things -->>> ( Width, Height and Channel)

# # print(capture)
# cv2.imshow('img',capture)

# cv2.waitKey(0)