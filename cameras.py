import cv2
import time

class Cameras:
    def __init__(self) -> None:
        None

    def getFrame(self):
        self.vid = cv2.VideoCapture(0)
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        if not (self.vid.isOpened()):
            print("Could not open video device")
        ret, frame = self.vid.read()
        self.vid.release()
        return frame