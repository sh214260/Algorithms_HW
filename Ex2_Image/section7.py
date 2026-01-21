import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys

def compute_histogram_manual(gray_image):
    # יצירת מערך של אפסים בגודל 256 (לכל ערך אפשרי בגווני אפור)
    histogram = [0] * 256

    # מעבר על כל הפיקסלים בתמונה
    height, width = gray_image.shape
    for y in range(height):
        for x in range(width):
            value = gray_image[y, x]
            histogram[value] += 1

    return histogram

def main():
    parser = argparse.ArgumentParser(description="Grayscale + manual histogram")
    parser.add_argument("input_file", help="Path to image file")
    args = parser.parse_args()

    # קריאת תמונה
    image = cv2.imread(args.input_file)
    if image is None:
        print("לא ניתן לקרוא את הקובץ")
        sys.exit(1)

    # המרה לגווני אפור
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # חישוב היסטוגרמה ידנית
    hist = compute_histogram_manual(gray)

    # הצגת היסטוגרמה
    plt.figure(figsize=(10, 4))
    plt.bar(range(256), hist, color='gray')
    plt.title("היסטוגרמה של התמונה")
    plt.xlabel("ערך פיקסל (0–255)")
    plt.ylabel("כמות פיקסלים")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
