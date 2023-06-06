import cv2


def display():
    img = cv2.imread("assets/Grayscale_Cat.jpg", 0)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
