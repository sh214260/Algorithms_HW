from PIL import Image
import sys

def show_color_channels(image_path):
    # טען את התמונה
    image = Image.open(image_path)
    
    # המר ל-RGB אם לא כבר
    image = image.convert("RGB")
    
    # פצל את הערוצים
    r, g, b = image.split()
    
    # הצג כל ערוץ בנפרד
    r.show(title="Red Channel")
    g.show(title="Green Channel")
    b.show(title="Blue Channel")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex01.01.py my_image.jpg")
    else:
        show_color_channels(sys.argv[1])
