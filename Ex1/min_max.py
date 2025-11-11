with open("data.txt", "r") as f:
    first_line = f.readline()
    min_val = max_val = float(first_line.strip())
    for line in f:
        num = float(line.strip())
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

print(f"min={min_val}")
print(f"max={max_val}")

#זמן ריצה: O(n) כי אנחנו עוברים על כל המספרים פעם אחת בלבד
#זיכרון: O(1) כי אנחנו שומרים רק שני משתנים נוספים (min_val ו-max_val) ללא תלות בגודל הקלט