import cv2

capture = cv2.VideoCapture("D:/Cell Data/GoPro-Exports/GH011684_1671360697606.MP4")

while True:
    x,y = capture.read()  # in x it stores the vdo and  every frame stores in y

    cv2.imshow("vdo",y)

    if cv2.waitKey(10) & 0xFF == ord("q")