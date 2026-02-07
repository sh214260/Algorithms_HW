import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
import colorsys

# ---------------------------------------------------------
# קבלת R,G,B משורת הפקודה
# ---------------------------------------------------------
R = int(sys.argv[1])
G = int(sys.argv[2])
B = int(sys.argv[3])

# נרמול ל-0..1 עבור חישובי HSV/HSL
r = R / 255
g = G / 255
b = B / 255

# ---------------------------------------------------------
# א. מימוש ידני של HSV
# ---------------------------------------------------------
Cmax = max(r, g, b)
Cmin = min(r, g, b)
delta = Cmax - Cmin

# Hue
if delta == 0:
    H = 0
elif Cmax == r:
    H = 60 * (((g - b) / delta) % 6)
elif Cmax == g:
    H = 60 * (((b - r) / delta) + 2)
else:
    H = 60 * (((r - g) / delta) + 4)

# Saturation
S = 0 if Cmax == 0 else delta / Cmax

# Value
V = Cmax

print("\n--- HSV (manual) ---")
print("H =", H)
print("S =", S)
print("V =", V)

# ---------------------------------------------------------
# ב. HSV בעזרת cv2
# ---------------------------------------------------------
rgb = np.uint8([[[R, G, B]]])
hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)[0][0]

print("\n--- HSV (cv2) ---")
print("H =", hsv[0] * 2)     # OpenCV stores H in [0..180]
print("S =", hsv[1] / 255)
print("V =", hsv[2] / 255)

# ---------------------------------------------------------
# א. מימוש ידני של HSL
# ---------------------------------------------------------
L = (Cmax + Cmin) / 2
if delta == 0:
    S_L = 0
else:
    S_L = delta / (1 - abs(2 * L - 1))

print("\n--- HSL (manual) ---")
print("H =", H)
print("S =", S_L)
print("L =", L)

# ---------------------------------------------------------
# ב. HSL בעזרת colorsys
# ---------------------------------------------------------
h2, l2, s2 = colorsys.rgb_to_hls(r, g, b)

print("\n--- HSL (colorsys) ---")
print("H =", h2 * 360)
print("S =", s2)
print("L =", l2)

# ---------------------------------------------------------
# א. מימוש ידני של YCrCb
# ---------------------------------------------------------
Y  = 0.299 * R + 0.587 * G + 0.114 * B
Cb = 128 - 0.168736 * R - 0.331264 * G + 0.5 * B
Cr = 128 + 0.5 * R - 0.418688 * G - 0.081312 * B

print("\n--- YCrCb (manual) ---")
print("Y  =", Y)
print("Cb =", Cb)
print("Cr =", Cr)

# ---------------------------------------------------------
# ב. YCrCb בעזרת cv2
# ---------------------------------------------------------
ycrcb = cv2.cvtColor(rgb, cv2.COLOR_RGB2YCrCb)[0][0]

print("\n--- YCrCb (cv2) ---")
print("Y  =", ycrcb[0])
print("Cr =", ycrcb[1])
print("Cb =", ycrcb[2])

# ---------------------------------------------------------
# הצגת צבע המקור (לא חובה אבל לפי ההוראות משתמשים ב-matplotlib)
# ---------------------------------------------------------
plt.imshow([[ [R/255, G/255, B/255] ]])
plt.title("Input RGB Color")
plt.axis('off')
plt.show()
