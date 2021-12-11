import cv2


def smile_detect(smile_cascade, img, gray):

    smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(img, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)


# Source: https://www.geeksforgeeks.org/python-smile-detection-using-opencv/
