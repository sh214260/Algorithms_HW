import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

from section1 import create_gradient_image

def brighten(img, b, func):
    img_array = np.array(img)  # המרה ל־NumPy array

    if func == "numpy":
        brightened = np.add(img_array, b)
    elif func == "cv2":
        brightened = cv2.add(img_array, b)
    else:
        raise ValueError("func must be 'numpy' or 'cv2'")

    # החזרת תמונה חדשה מ־array
    return Image.fromarray(brightened.astype(np.uint8))

# יצירת תמונת גרדיאנט
image = create_gradient_image(255, 255)

# הפעלת brighten עם שתי שיטות
bright_np = brighten(image, 50, "numpy")
bright_cv2 = brighten(image, 50, "cv2")

# הצגה עם matplotlib
fig, axs = plt.subplots(1, 3, figsize=(12, 4))
axs[0].imshow(image, cmap='gray')
axs[0].set_title("Original Image")
axs[1].imshow(bright_np, cmap='gray')
axs[1].set_title("opacity with numpy")
axs[2].imshow(bright_cv2, cmap='gray')
axs[2].set_title("opacity with cv2")

for ax in axs:
    ax.axis('off')

plt.tight_layout()
plt.show()
