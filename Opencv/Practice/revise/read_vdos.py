# import cv2


# capture = cv2.VideoCapture(r"C://Users//Farogh//Videos//WhatsApp Video 2024-08-21 at 11.39.47_cf04cdac.mp4")
# # we need to convert vdo into frames to read the vdo

# while True:
#     is_True, frame = capture.read()   # isTru identify that vdo exists or not

#     cv2.imshow("title", capture)
#     # cv2.waitKey(10)

#     if cv2.waitKey(10) & 0xFF == ord("q"):
#         break
        

import cv2

capture = cv2.VideoCapture(r"C:\Users\Farogh\Videos\WhatsApp Video 2024-08-21 at 11.39.47_cf04cdac.mp4")

while True:
    is_True, frame = capture.read()   
    if not is_True:
        break
    cv2.imshow("title", frame)  # Corrected this line to use 'frame'
    

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
