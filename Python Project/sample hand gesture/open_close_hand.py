import cv2
from HandLandmarkModule import MyHandTrackingModule

capture = cv2.VideoCapture(0)
HandModule = MyHandTrackingModule()

while True:
    isDone, frame = capture.read()

    HandModule.HandDetector(frame)

    landmarkpoints = HandModule.HandCordinates(frame)
    # print(landmarkpoints, "hii")

    # if landmarkpoints[]

    cv2.imshow("Check hand open or close", frame)

    if cv2.waitKey(3) & 0xff == ord("q"):
        break