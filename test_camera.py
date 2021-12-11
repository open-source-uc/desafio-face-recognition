import base64

import cv2
import keyboard

from recognition.camera import Camera
from recognition.utils import nc200_connection_url
from settings import CAMERA_IP, CAMERA_PASSWORD, CAMERA_PORT, CAMERA_USER


def main():
    camera_url = nc200_connection_url(
        CAMERA_IP, CAMERA_USER, CAMERA_PASSWORD, CAMERA_PORT
    )
    cam = Camera(ip=camera_url)
    cam.start_camera_stream()
    while not keyboard.is_pressed("q"):
        if cam.frame is not None:
            # show camera frame
            cv2.imshow("img", cam.frame)
            cv2.waitKey()
        pass
    cam.stop_camera_stream()


if __name__ == "__main__":
    main()
