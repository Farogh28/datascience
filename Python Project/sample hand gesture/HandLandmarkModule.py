import cv2 
import mediapipe as mp  
import time  

class MyHandTrackingModule:
    def __init__(self, mode = False, maxHands= 2, model_complexity = 2,min_detection_confidence = 0.5, min_tracking_confidence = 0.5):
        # Setting all parameter as attributes
        # constructor ues coz, we can use this in every class (correct it later)
        self.mode= mode
        self.maxHands = maxHands
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.map_hands = mp.solutions.hands   
        self.hands = self.map_hands.Hands()   
        self.show_landmarks = mp.solutions.drawing_utils
        self.change_landmark_cover = self.show_landmarks.DrawingSpec(color= (6, 48, 115), thickness = 3)
        self.change_connection_cover = self.show_landmarks.DrawingSpec(color= (7, 247, 203), thickness = 5)
        self.result = None

    def HandDetector(self, img, draw = True):
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        self.result = self.hands.process(rgb_img)
        ptime = 0 
        ctime= 0

        if self.result.multi_hand_landmarks:
            for hands_landmarks in self.result.multi_hand_landmarks:
                self.show_landmarks.draw_landmarks(img, hands_landmarks,self.map_hands.HAND_CONNECTIONS, self.change_landmark_cover,self.change_connection_cover)

        
        ctime = time.time()
        fps = 1/ (ctime-ptime)
        ptime = ctime

        cv2.putText(img, f"fps is {str(fps)[:5]}", (5,25),1,2,(194,16,21),2) 

    def HandCordinates(self, img, numofHands = 0, draw = True):
        landmark_lst = []
        if self.result.multi_hand_landmarks:    
            myhand = self.result.multi_hand_landmarks[numofHands]
            for id, lm in enumerate(myhand.landmark):
                h,w,c = img.shape
                cx, cy = (int(lm.x*w),int(lm.y*h)) 
                self.landmark_lst.append([id,cx,cy])
        return landmark_lst

# capture = cv2.VideoCapture(0)

# while True:

#     isDone, frame = capture.read()

#     if not isDone:
#         print ("Failed to capture image")
#         break


#     if self.result.multi_hand_landmarks:    
#         myhand = self.result.multi_hand_landmarks[0]
#         for id, lm in enumerate(myhand.landmark):
#             h,w,c = frame.shape
#             cx, cy = (int(lm.x*w),int(lm.y*h)) 
#             self.landmark_lst.append([id,cx,cy])
         
#         for hands_landmarks in self.result.multi_hand_landmarks:
#             self.show_landmarks.draw_landmarks(frame, hands_landmarks,self.map_hands.HAND_CONNECTIONS, self.change_landmark_cover,self.change_connection_cover)


#     cv2.imshow("Myvideo", frame)
#     if cv2.waitKey(3) & 0xff == ord("q"):
#         break    