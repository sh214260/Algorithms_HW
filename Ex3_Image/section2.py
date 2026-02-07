import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# יצירת תמונות בסיסיות
# ---------------------------------------------------------

def create_gradient_image(height, width):
    img = np.zeros((height, width), dtype=np.uint8)
    max_sum = (height - 1) + (width - 1)

    for r in range(height):
        for c in range(width):
            value = (r + c) * 255 / max_sum
            img[r, c] = int(value)

    return img


def create_circle_image(height, width, bg=128, fg=130):
    img = np.full((height, width), fill_value=bg, dtype=np.uint8)
    center = (width // 2, height // 2)
    radius = min(height, width) // 4

    cv2.circle(img, center, radius, fg, -1)
    return img


# ---------------------------------------------------------
# ציור מלבן עם גרדיאנט
# ---------------------------------------------------------

def draw_gradient_rect(img, rect, col1, col2):
    (r0, c0), (r1, c1) = rect
    height, width = img.shape[:2]

    r0 = max(0, r0)
    c0 = max(0, c0)
    r1 = min(height, r1)
    c1 = min(width, c1)

    is_color = img.ndim == 3

    if is_color:
        col1 = np.array(col1, dtype=np.float32)
        col2 = np.array(col2, dtype=np.float32)
    else:
        col1 = float(col1)
        col2 = float(col2)

    h = r1 - r0
    w = c1 - c0

    for rr in range(r0, r1):
        for cc in range(c0, c1):
            t = ((rr - r0) / max(h - 1, 1) + (cc - c0) / max(w - 1, 1)) / 2
            val = (1 - t) * col1 + t * col2
            img[rr, cc] = np.clip(val, 0, 255).astype(np.uint8)


def create_multimodal_hist_image(specs, height, width, color=False):
    if color:
        img = np.zeros((height, width, 3), dtype=np.uint8)
    else:
        img = np.zeros((height, width), dtype=np.uint8)

    for spec in specs:
        draw_gradient_rect(img, spec['rect'], spec['colors'][0], spec['colors'][1])

    return img


# ---------------------------------------------------------
# Equalization functions
# ---------------------------------------------------------

def equalize_per_channel_rgb(img_rgb):
    out = img_rgb.copy()
    for ch in range(3):
        out[..., ch] = cv2.equalizeHist(out[..., ch])
    return out


def equalize_value_channel_hsv(img_rgb):
    hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)


def equalize_luminance_ycrcb(img_rgb):
    ycrcb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2YCrCb)
    ycrcb[..., 0] = cv2.equalizeHist(ycrcb[..., 0])
    return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2RGB)


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":
    height = 400
    width = 500

    # --- יצירת תמונות בסיס ---
    gradient_image = create_gradient_image(height, width)
    circle_image = create_circle_image(height, width)

    # --- הצגת gradient + circle ---
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(gradient_image, cmap='gray')
    axes[0].set_title("Gradient Image")
    axes[0].axis('off')

    axes[1].imshow(circle_image, cmap='gray')
    axes[1].set_title("Low Contrast Circle")
    axes[1].axis('off')

    plt.show()

    # --- יצירת תמונת היסטוגרמה ---
    specs = [
        {'rect': ((0, 0), (height, width)), 'colors': (50, 60)},
        {'rect': ((30, 30), (220, 200)), 'colors': (70, 80)},
        {'rect': ((100, 300), (360, 480)), 'colors': (180, 185)},
        {'rect': ((150, 340), (260, 430)), 'colors': (195, 200)},
    ]

    hist_img = create_multimodal_hist_image(specs, height, width)

    plt.figure(figsize=(6, 6))
    plt.imshow(hist_img, cmap='gray')
    plt.title("Multimodal Histogram Image")
    plt.axis('off')
    plt.show()

    # --- תמונת צבע ---
    color_specs = [
        {'rect': ((0, 0), (height, width)), 'colors': ((50, 20, 30), (55, 40, 35))},
        {'rect': ((30, 30), (220, 200)), 'colors': ((70, 10, 20), (80, 40, 30))},
        {'rect': ((100, 300), (360, 480)), 'colors': ((180, 120, 130), (185, 140, 135))},
        {'rect': ((150, 340), (260, 430)), 'colors': ((195, 150, 160), (200, 155, 165))},
    ]

    color_img = create_multimodal_hist_image(color_specs, height, width, color=True)

    # Equalization
    eq_rgb = equalize_per_channel_rgb(color_img)
    eq_hsv = equalize_value_channel_hsv(color_img)
    eq_y = equalize_luminance_ycrcb(color_img)

    # --- הצגת כל תמונות הצבע ---
    fig, axes = plt.subplots(1, 4, figsize=(18, 6))

    axes[0].imshow(color_img)
    axes[0].set_title("Original RGB")
    axes[0].axis('off')

    axes[1].imshow(eq_rgb)
    axes[1].set_title("Equalized per RGB Channel")
    axes[1].axis('off')

    axes[2].imshow(eq_hsv)
    axes[2].set_title("Equalized HSV (V channel)")
    axes[2].axis('off')

    axes[3].imshow(eq_y)
    axes[3].set_title("Equalized YCrCb (Y channel)")
    axes[3].axis('off')

    plt.show()
