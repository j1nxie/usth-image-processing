import cv2
import matplotlib.pyplot as plt

from .constants import img


def image_thresholding():
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    plt.hist(thresh.ravel(), 256, [0, 256])
    plt.title("binarized histogram")
    plt.xlabel("intensity")
    plt.ylabel("frequency")
    plt.show()

    cv2.imshow("binarized image", thresh)
