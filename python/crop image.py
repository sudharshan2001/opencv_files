import cv2
import numpy as np
import PIL
from PIL import Image

cropping = False

x_start, y_start, x_end, y_end = 0, 0, 0, 0


img = Image.open('image path')

img=img.resize((720, 480), PIL.Image.ANTIALIAS)
img.save('resized_image.jpg')

image = cv2.imread('resized_image.jpg')
oriImage = image.copy()


def mouse_crop(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
    
    
    elif event == cv2.EVENT_MOUSEMOVE:
        try:
            if cropping == True:
                x_end, y_end = x, y
        except:
            pass

    elif event == cv2.EVENT_LBUTTONUP:
        
        x_end, y_end = x, y
        cropping = False  

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2:  
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)
            


cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)

while True:
    i = image.copy()

    if not cropping:
        cv2.imshow("image", image)
        if cv2.waitKey(0):
            break

    elif cropping:
        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
        cv2.imshow("image", i)
    break
 

    cv2.waitKey(0)
    

cv2.destroyAllWindows()  
