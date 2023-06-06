import cv2

from .constants import img


def resize():
    scaling_factor = 0.5
    width = int(img.shape[1] * scaling_factor)
    height = int(img.shape[0] * scaling_factor)
    new_dim = (width, height)
    resized_img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("resized image", resized_img)
