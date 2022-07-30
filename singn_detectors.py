import cv2
import numpy as np
from sqlalchemy import null

class SignDetections:
    def __init__(self) -> None:
        null

    def Find_Rectangles(self, Image):
        gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (25,25), 0)
        thresh_img = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        cnts = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        ROI_number = 0
        ROI = []
        for cnt in cnts:
            approx = cv2.contourArea(cnt)
            if approx > 500:
                x,y,w,h = cv2.boundingRect(cnt)
                ROI.append(Image[y:y+h, x:x+w])
                cv2.rectangle(Image,(x,y),(x+w,y+h),(36,255,12),2)
                ROI_number += 1
        return ROI

    def Check_For_Features(self, Images):
        null

image_name = 'audi-2763807-2-1849218343.png'
img = cv2.imread(image_name)
MD = SignDetections()    
images = MD.Find_Rectangles(img)
n = 'a'
for i in images:
    cv2.imwrite(n + '.png',i)
    n = chr(ord(n) + 1)


            