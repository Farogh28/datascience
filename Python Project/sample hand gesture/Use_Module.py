import cv2
from HandLandmarkModule import MyHandTrackingModule

module = MyHandTrackingModule()

capture = cv2.VideoCapture(0)  

while True:   # this loop initiated to continually capture vdo frames fromm camera and process them
    isDone, frame = capture.read()   # Reading the frame from camera

    module.HandDetector(frame) #  It detects hand in the frame.

    landmarkpoints = module.HandCordinates(frame) # it extracts the hand landmark points 
    
    # print (landmarkpoints, "Hello")

    if landmarkpoints:
        if landmarkpoints[8][2] < landmarkpoints[6][2]:
            print ("Hand Open")
        else:
            print ("Hand Closed")

    cv2.imshow("Getting Frame", frame)

    if cv2.waitKey(3) & 0xff == ord("q"):
        break