import os
import cv2
import argparse
import sys
import numpy as np

def normalize_image(src_image):
    # המרת התמונה ל־float32
    src_float = src_image.astype(np.float32)

    # מציאת ערכי מינימום ומקסימום
    min_val, max_val, _, _ = cv2.minMaxLoc(src_float)

    # חישוב פקטור הנורמליזציה
    factor = 255.0 / (max_val - min_val)

    # נורמליזציה
    dst_float = (src_float - min_val) * factor

    # חיתוך והמרה ל־uint8
    dst = np.clip(dst_float, 0, 255).astype(np.uint8)

    return dst


def main():
    # 1. קריאת פרמטרים מה־command line
    parser = argparse.ArgumentParser(description="Convert image to grayscale and normalize it.")
    parser.add_argument("input_file", help="Path to the input image file")
    args = parser.parse_args()

    # 2. טעינת התמונה
    image = cv2.imread(args.input_file)
    if image is None:
        print(f"Error: Could not open or find the image '{args.input_file}'")
        sys.exit(1)

    # 3. המרה לגווני אפור
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 4. שמירת תמונת grayscale
    file, ext = os.path.splitext(args.input_file)
    gray_filename = f"{file}_grayscale{ext}"
    cv2.imwrite(gray_filename, gray_image)
    print(f"Saved grayscale image: {gray_filename}")

    # 5. נורמליזציה
    normalized = normalize_image(gray_image)

    # 6. שמירת תמונת normalized
    norm_filename = f"{file}_normalized{ext}"
    cv2.imwrite(norm_filename, normalized)
    print(f"Saved normalized image: {norm_filename}")

    # 7. הדפסת נתונים
    min_val, max_val, _, _ = cv2.minMaxLoc(gray_image)
    mean_val = np.mean(gray_image)
    factor = 255.0 / (max_val - min_val)

    print(f"Min: {min_val}, Max: {max_val}, Mean: {mean_val:.2f}")
    print(f"Normalization factor: {factor:.2f}")

    ##########################################
    #תרגיל 6
    # 4.5 שינוי פיקסל אחד ל־0 ואחד ל־255
    gray_image[0, 0] = 0         # פיקסל בפינה שמאלית עליונה
    gray_image[-1, -1] = 255     # פיקסל בפינה ימנית תחתונה
    print("שונו שני פיקסלים: אחד ל-0 ואחד ל-255")

    # הצגה לאחר שינוי הפיקסלים
if __name__ == "__main__":
    main()
