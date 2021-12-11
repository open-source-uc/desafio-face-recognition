from pathlib import Path
from threading import Thread, Timer
from typing import TYPE_CHECKING

import cv2
import numpy as np
from cv2 import CascadeClassifier
from numpy.typing import NDArray

from recognition.camera import Camera
from recognition.face import face_detect
from settings import FRAME_RATE, ROOT_DIR

if TYPE_CHECKING:
    from recognition.camera import Camera


class IFace:
    def __init__(self, camera: Camera):
        self.camera = camera
        self._input_frame: NDArray = None
        self.output_frame: NDArray = None
        self.face_cascade: CascadeClassifier = CascadeClassifier(
            str(Path(ROOT_DIR / "models" / "haarcascade_frontalface_default.xml"))
        )
        self.smile_cascade: CascadeClassifier = CascadeClassifier(
            str(Path(ROOT_DIR / "models" / "haarcascade_smile.xml"))
        )
        self.thread_deteccion = None
        self.display_thread = None
        self._running = False

    @property
    def input_frame(self):
        self._input_frame = self.camera.get_frame()
        return self._input_frame

    # Constantly detects faces and smiles and returns the processed frame
    def recognition(self):
        while self._running:
            frame = np.copy(self.input_frame)
            if frame is not None and not len(frame.shape) == 0:
                self.output_frame = face_detect(
                    frame, self.face_cascade, self.smile_cascade
                )

    def start_detection(self):
        self._running = True
        self.thread_deteccion = Thread(
            target=self.recognition, name="detection", daemon=True
        )

        self.thread_deteccion.start()

    def stop_detection(self):
        self.self._running = False
