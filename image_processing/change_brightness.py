import cv2
import numpy as np

from .constants import img


def change_brightness():
    formula = 0.75 * img + 80
    processed_img = np.clip(formula, 0, 255).astype(np.uint8)
    cv2.imshow("processed image", processed_img)
