from pathlib import Path

import cv2

from recognition.smile import smile_detect

# from cv2 import imread
from settings import ROOT_DIR


# Receives img obj/stream, and two cascade filters.
def face_detect(img, face_cascade, smile_cascade):
    # Load the cascade
    # Read the input image from file
    # img = cv2.imread(str(Path(ROOT_DIR / "data" / "sadFace.jpg")))

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        smile_detect(smile_cascade, img, gray)
    # Display the output
    # cv2.imshow('img', img)
    # cv2.waitKey()

    return img
