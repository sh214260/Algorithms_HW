from PIL import Image, ImageOps
import sys
import matplotlib.pyplot as plt

def stretch_channel(channel):
    return ImageOps.equalize(channel)

def process_image(image_path):
    # א. קריאת קובץ תמונה
    image = Image.open(image_path).convert("RGB")

    # ב. חישוב היסטוגרמה לכל ערוץ בנפרד
    r, g, b = image.split()
    r_hist = r.histogram()
    g_hist = g.histogram()
    b_hist = b.histogram()

    # הצגת ההיסטוגרמות המקוריות
    plt.figure(figsize=(10, 4))
    plt.title("Original Histograms")
    plt.plot(r_hist, color='red', label='Red')
    plt.plot(g_hist, color='green', label='Green')
    plt.plot(b_hist, color='blue', label='Blue')
    plt.legend()
    plt.show()

    # ג. מתיחת היסטוגרמה לכל ערוץ בנפרד
    r_stretched = stretch_channel(r)
    g_stretched = stretch_channel(g)
    b_stretched = stretch_channel(b)

    # ד. יצירת תמונה חדשה והצגתה
    stretched_image = Image.merge("RGB", (r_stretched, g_stretched, b_stretched))
    stretched_image.show(title="Stretched RGB Image")

    # הצגת ההיסטוגרמות החדשות
    r_hist_new = r_stretched.histogram()
    g_hist_new = g_stretched.histogram()
    b_hist_new = b_stretched.histogram()

    plt.figure(figsize=(10, 4))
    plt.title("Stretched Histograms")
    plt.plot(r_hist_new, color='red', label='Red')
    plt.plot(g_hist_new, color='green', label='Green')
    plt.plot(b_hist_new, color='blue', label='Blue')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex03.py my_image.jpg")
    else:
        process_image(sys.argv[1])
