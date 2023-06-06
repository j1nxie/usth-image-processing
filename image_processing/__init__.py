import cv2

from image_processing.change_brightness import change_brightness
from image_processing.display import display
from image_processing.histogram_equalization import histogram_equalization
from image_processing.image_thresholding import image_thresholding
from image_processing.resize import resize


def main():
    display()
    resize()
    change_brightness()
    histogram_equalization()
    image_thresholding()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


__all__ = ["main", "change_brightness", "display", "resize"]
