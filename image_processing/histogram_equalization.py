import cv2
import matplotlib.pyplot as plt

from .constants import img


def histogram_equalization():
    cv2.calcHist([img], [0], None, [256], [0, 256])

    plt.hist(img.ravel(), 256, [0, 256])
    plt.title("image histogram")
    plt.xlabel("intensity")
    plt.ylabel("frequency")
    plt.show()

    eq_histogram = cv2.equalizeHist(img)

    plt.hist(eq_histogram.ravel(), 256, [0, 256])
    plt.title("equalized histogram")
    plt.xlabel("intensity")
    plt.ylabel("frequency")
    plt.show()

    cv2.imshow("equalized image", eq_histogram)
