from PIL import Image, ImageDraw

def create_low_contrast_image(fg, bg, width=200, height=200):
    # יצירת תמונה בגווני אפור עם צבע רקע fg
    img = Image.new("L", (width, height), color=fg)
    draw = ImageDraw.Draw(img)

    # ציור עיגול במרכז עם צבע bg
    radius = min(width, height) // 4
    center = (width // 2, height // 2)
    bbox = [center[0] - radius, center[1] - radius,
            center[0] + radius, center[1] + radius]
    draw.ellipse(bbox, fill=bg)

    return img

img = create_low_contrast_image(fg=20, bg=105)
img.show()
