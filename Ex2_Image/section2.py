import numpy as np
import cv2

def brighten(img, b, func):
    if func == "נמפי":
        return np.add(img, b)
    elif func == "cv2":
        return cv2.add(img, b)
    else:
        raise ValueError("הפרמטר func חייב להיות 'numpy' או 'cv2'")
