import cv2
import numpy as np

# frame = np.zeros((512,512, 3))

# cv2.rectangle(frame, pt1=(100,100), pt2= (400,400), color=(97, 176, 156))

# cv2.circle(frame, center=(300,400), radius= 50,color=(0,0,255))

# cv2.rectangleIntersectionArea


# cv2.imshow("Heyy",frame)

# cv2.waitKey(0)


image = np.zeros((500, 500, 3), dtype="uint8")

start_point = (100, 100)  # Top-left corner
end_point = (400, 400)    # Bottom-right corner
color = (255, 255, 255)   # White color in BGR
thickness = 2 

red_color = (0, 0, 255)  # Red color in BGR
cv2.rectangle(image, start_point, end_point, red_color, 5)

# Draw a green rectangle inside the red one
green_start_point = (150, 150)
green_end_point = (350, 350)
green_color = (0, 255, 0)  # Green color in BGR
cv2.rectangle(image, green_start_point, green_end_point, green_color, 3)


x, y, w, h = 50, 50, 200, 150  # Coordinates for the rectangle
cv2.rectangle(image, (x, y), (x+w, y+h), color, thickness)

# Display the image
cv2.imshow('Colorful Rectangles', image)
cv2.waitKey(0)
