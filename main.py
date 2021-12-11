import cv2
import keyboard
import numpy as np

from recognition.camera import Camera
from recognition.interface.iface import IFace
from recognition.utils.connections import nc200_connection_url
from settings import CAMERA_IP, CAMERA_PASSWORD, CAMERA_PORT, CAMERA_USER


def main():

    # Start camera stream
    camera_url = nc200_connection_url(
        CAMERA_USER, CAMERA_PASSWORD, CAMERA_IP, CAMERA_PORT
    )
    camera: Camera = Camera(ip=camera_url)
    camera.start_camera_stream()

    interface = IFace(camera)
    interface.start_detection()

    while not keyboard.is_pressed("q"):
        frame = np.copy(interface.output_frame)
        if frame is not None and not len(frame.shape) == 0:
            cv2.imshow("img", frame)
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break

    # Stops camera stream
    camera.stop_camera_stream()

    # Stops interface detection and display threads
    interface.stop_detection()


if __name__ == "__main__":
    main()
