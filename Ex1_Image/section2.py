from PIL import Image, ImageOps
import sys
import matplotlib.pyplot as plt

def process_image(image_path):
    # שלב א: קריאת קובץ תמונה
    image = Image.open(image_path)

    # שלב ב: הפיכה לשחור-לבן (גרייסקל)
    gray_image = ImageOps.grayscale(image)

    # שלב ג: חישוב היסטוגרמה
    histogram = gray_image.histogram()

    # הצגת ההיסטוגרמה המקורית
    plt.figure(figsize=(10, 4))
    plt.title("Original Histogram")
    plt.plot(histogram)
    plt.show()

    # שלב ד: מתיחת ההיסטוגרמה
    stretched_image = ImageOps.equalize(gray_image)

    # הצגת התמונה החדשה
    stretched_image.show(title="Stretched Histogram Image")

    # הצגת ההיסטוגרמה החדשה
    stretched_histogram = stretched_image.histogram()
    plt.figure(figsize=(10, 4))
    plt.title("Stretched Histogram")
    plt.plot(stretched_histogram)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex02.py my_image.jpg")
    else:
        process_image(sys.argv[1])
