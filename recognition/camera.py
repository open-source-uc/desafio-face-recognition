from threading import Lock, Timer

import cv2
import numpy as np
from cv2 import VideoCapture
from numpy.typing import NDArray

from settings import FRAME_RATE

# connect to an ip camera and display the image


class Camera:
    def __init__(self, ip):
        self.ip = ip
        self.camera: VideoCapture = VideoCapture(self.ip)
        self._frame: NDArray = None
        self._camera_timer: Timer = None
        self._running: bool = False
        self._camera_lock: Lock = Lock()

    def _next_frame(self):
        ret, self._frame = self.camera.read()
        return ret

    def get_frame(self):
        """
        Returns a copy of the current frame from the camera
        """
        with self._camera_lock:
            if self._running:
                return np.copy(self._frame)
            else:
                return None

    def __manage_stream(self):
        self._next_frame()
        self.start_camera_stream()

    def __schedule_next_frame(self):
        self._camera_timer = Timer(1 / FRAME_RATE, self.__manage_stream)
        self._camera_timer.name = "Next frame timer"
        self._camera_timer.start()

    def start_camera_stream(self):
        self._running = True
        self.__schedule_next_frame()

    def stop_camera_stream(self):
        self.camera.release()
        if self._camera_timer is not None:
            self._camera_timer.cancel()
        self._running = False
