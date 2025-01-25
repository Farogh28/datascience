import cv2 
import numpy as np
import os

peoples = ["elon musk", "img", "new"]
path = r"C:\Users\Farogh\Desktop\New DataScience\datascience\project nov"


# to detect faces 
face_detector = cv2.CascadeClassifier(cv2.data.haar)


features =[]
labels = []


for person in peoples:
    folder_path = os.path.join(path, person)
    lable= peoples.index(person)
    

    for images in os.listdir(folder_path):
        # print(images)
        images_path = os.path.join(folder_path, images)   # code to get the whole path of the file

        # print(images_path)
        # converting images into gray scale

        # before this converting into numpy as it auto done coz of openong in numpy array
        images_aray= cv2.imread(images_path)

        gray_img= cv2.cvtColor(images_aray, cv2.COLOR_BGR2GRAY)
        

        #face detection code
        face_region = face_detector.detectMultiScale(gray_img, scaleFactor= 1.1, minNeighbors= 3)

        for (x,y,w,h) in face_region:
            face_roi= gray_img[y:y+h, x:x+w]
            features.append(face_roi)
            labels.append(lable)


        # print(gray_img)
        cv2.imshow("hey", gray_img) 

        cv2.waitKey(0)