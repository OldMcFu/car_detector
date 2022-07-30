from cv2 import CAP_OPENNI_IMAGE_GENERATOR_PRESENT

import cv2, time
import cameras
import motion_detections

Cam_Obj = cameras.Cameras()
Motion_Obj = motion_detections.MotionDetection()

while(True):
    Motion_Obj.Motion_Present(Cam_Obj.getFrame())
    time.sleep(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()