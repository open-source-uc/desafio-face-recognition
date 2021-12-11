import cv2
# from cv2 import imread
from settings import ROOT_DIR
from pathlib import Path
from recognition.smile import smileDetect

def faceDetect(): 
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(str(Path(ROOT_DIR / "models" / "haarcascade_frontalface_default.xml")))
    smile_cascade = cv2.CascadeClassifier(str(Path(ROOT_DIR / "models" / "haarcascade_smile.xml")))
    # Read the input image
    img = cv2.imread(str(Path(ROOT_DIR / "data" / "sadFace.jpg")))
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        smileDetect(smile_cascade, img, gray)
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()
