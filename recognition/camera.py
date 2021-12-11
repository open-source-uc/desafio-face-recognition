import cv2
from threading import Timer

from settings import FRAME_RATE

# connect to an ip camera and display the image

class Camera:
    def __init__(self, ip):
        self.ip = ip
        self.camera = cv2.VideoCapture(self.ip)
        self.frame = None
        self.camera_timer: Timer = None
        self._running: bool = False
    
    def next_frame(self):
        ret, self.frame = self.camera.read()
        return ret
    
    def __manage_stream(self):
        self.next_frame()
        self.start_camera_stream()

    def __schedule_next_frame(self):
        self.camera_timer = Timer(1/FRAME_RATE, self.__manage_stream)
        self.camera_timer.name = "Next frame timer"
        self.camera_timer.start()
    
    def start_camera_stream(self):
        self._running = True
        self.__schedule_next_frame()
    
    def close(self):
        self.camera.release()
        if self.camera_timer is not None:
            self.camera_timer.cancel()
        cv2.destroyAllWindows()
        self._running = False