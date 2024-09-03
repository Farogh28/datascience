import cv2 
import mediapipe as mp  # Developed by google
# There were so many modules in mediapipe, and we are choosing/ using only hands module

map_hands = mp.solutions.hands   # Create a Mediapipe Hands instance
#  in solutoins most of modules were found

hands = map_hands.Hands()   # Hands consist LandMarks of Numpy array

show_landmarks = mp.solutions.drawing_utils


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

    # print(result.multi_hand_landmarks)

    class_name = ''

    if result.multi_hand_landmarks:    # We pass this because, if result.multi_hand_landmarks consist some value then it will show the array otherwise it will not, 
        #coz it also consist None value  

        landmarks = [] 
        for hands_landmarks in result.multi_hand_landmarks:
            show_landmarks.draw_landmarks(frame, hands_landmarks)


    cv2.imshow("Myvideo", frame)

    cv2.waitKey(3)
    