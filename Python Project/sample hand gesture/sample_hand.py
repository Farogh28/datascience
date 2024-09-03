import cv2 
import mediapipe as mp  # Developed by google
# There were so many modules in mediapipe, and we are choosing/ using only hands module

import time   # imort time to see how many frames are we getting.


map_hands = mp.solutions.hands   # Create a Mediapipe Hands instance
#  in solutoins most of modules were found
hands = map_hands.Hands()   # Hands consist LandMarks of Numpy array
show_landmarks = mp.solutions.drawing_utils

# To change landmarks color 
change_landmark_cover = show_landmarks.DrawingSpec(color= (6, 48, 115), thickness = 3)

# # To change connections color 
change_connection_cover = show_landmarks.DrawingSpec(color= (7, 247, 203), thickness = 5)

capture = cv2.VideoCapture(0)   # if you have external cam then you can use 1 instead of 0

while True:
    # Read each frame from the webcam
    isDone, frame = capture.read()

    if not isDone:
        print ("Failed to capture image")
        break
    # Opencv takes ------> BGR Frames
    # Mediapipe takes ---- > RGB Frames/ format

    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # coz cv2 works in BGR format, so we contvert it here to RGB format

    result = hands.process(rgb_img)

    ptime = 0 # just initialize before executing, so we didn't get error
    ctime= 0
    # print(result.multi_hand_landmarks)
    landmark_lst = []

    if result.multi_hand_landmarks:    # We pass this because, if result.multi_hand_landmarks consist some value then it will show the array otherwise it will not, 
        #coz it also consist None value 
        
        # this code is for landmark_lst , Starts here----------
        myhand = result.multi_hand_landmarks[0]
        for id, lm in enumerate(myhand.landmark):   #enumerate -> it helps to manage the id and km in a proper way.
            # print (id, "This is I'd")
            # print (lm, "it's landmark")
            # print(frame.shape)  # runs as height x width x chanel ex.-(480,640,3)
            h,w,c = frame.shape
            # multiplicatoin of the width * x
            cx, cy = (int(lm.x*w),int(lm.y*h)) 
            # print (id, cx, cy)
            landmark_lst.append([id,cx,cy])

        #ends here-------------
         
        for hands_landmarks in result.multi_hand_landmarks:
            show_landmarks.draw_landmarks(frame, hands_landmarks,map_hands.HAND_CONNECTIONS, change_landmark_cover,change_connection_cover)


# to see the fps
    ctime = time.time()
    fps = 1/ (ctime-ptime)
    ptime = ctime

    cv2.putText(frame, f"fps is {str(fps)[:5]}", (5,25),1,2,(194,16,21),2)    #{str(fps)[:5]} in this we do type casting and slicing to get a shorter value 

    cv2.imshow("Myvideo", frame)
    if cv2.waitKey(3) & 0xff == ord("q"):
        break    