import cv2


# cap = cv2.VideoCapture("C:\\Users\\Farogh\\Videos\WhatsApp Video 2024-08-21 at 11.39.47_cf04cdac.mp4")  # Video have multiple frames, so to play the vdo we're going to run a loop

# while True:
#     done, frame = cap.read()

#     cv2.imshow("My Video", frame)        # To show the video

#     cv2.waitKey(0) # to wait the frame after loop


cap = cv2.imread("C:\\Users\\Farogh\\Pictures\\sticker.png")



# To add text on the immage 
# '225x225'
# Open cv always use RGB Color in color parameter

cv2.putText(cap, 'sticker', (100,125), 1,3, (81, 47, 181), 3,
            cv2.font)

cv2.imshow('Sticker', cap)
cv2.waitKey(0)