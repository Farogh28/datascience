import cv2

cap = cv2.VideoCapture (0)

while True:
    done, frame = cap.read()

    cv2.putText(frame, "Bhiyaaa", (10,10),10,4,(8, 156, 153), 4,cv2.FONT_HERSHEY_SIMPLEX)

    cv2.imshow("Start Camera", frame)

    cv2.waitKey(4)