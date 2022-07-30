import cv2
import numpy as np
from sqlalchemy import Boolean

class MotionDetection:
    def __init__(self) -> None:
        self.OldImage = None
        self.InitDone = False
        self.downPoints = (200, 200)
        self.ThresholdForMovement = 1_000_000

    def Motion_Present(self, Image) -> Boolean:
        #Downscale Image for fast Image processing
        gray2 = cv2.resize(Image, self.downPoints, interpolation= cv2.INTER_LINEAR)
        #Make Black and White image
        gray2 = cv2.cvtColor(gray2, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
        
        if self.InitDone == False:
            #Init Old Image for first use
            self.OldImage = gray2
            self.InitDone = True
            return False
        else:
            #Init is done now we can calculate the diff
            deltaframe=cv2.absdiff(self.OldImage,gray2)
            self.OldImage = gray2
            threshold = cv2.threshold(deltaframe, 35, 255, cv2.THRESH_BINARY)[1]
            kernel = np.ones((5, 5))
            threshold = cv2.dilate(threshold, kernel, 1)
            cv2.imshow('delta',deltaframe)
            cv2.imshow('threshold',threshold)
            if deltaframe.sum() > self.ThresholdForMovement:
                return True
            else:
                return False
            