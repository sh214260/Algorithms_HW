from PIL import Image

def create_gradient_image(height, width):
    # יצירת תמונה ריקה בגווני אפור
    img = Image.new("L", (width, height))
    pixels = img.load()

    # מעבר הדרגתי משחור (0) ללבן (255)
    for y in range(height):
        for x in range(width):
            value = int((x + y) * 255 / (width + height - 2))
            pixels[x, y] = value

    return img

# דוגמה לשימוש
image = create_gradient_image(255, 255)
image.show()      # מציג את התמונה
image.save("gradient.png")   # שומר לקובץ
