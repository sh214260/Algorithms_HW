def is_sorted(a, key):
    """
    מחזירה True אם הרשימה a מסודרת בסדר עולה לפי key.
    אחרת False.
    """
    for i in range(len(a) - 1):
        if key(a[i]) > key(a[i + 1]):
            return False
    return True


def merge(a, b, key):
    """
    ממזגת את שתי הרשימות הממוינות a ו-b
    לפי key ומחזירה רשימה חדשה.
    אם אחת מהן אינה ממוינת – מחזירה None.
    """

    # בדיקה שהרשימות באמת ממוינות
    if not is_sorted(a, key) or not is_sorted(b, key):
        return None

    i = 0
    j = 0
    result = []

    # מיזוג כמו ב־MergeSort
    while i < len(a) and j < len(b):
        if key(a[i]) <= key(b[j]):
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # הוספת השאריות
    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result

# דוגמה לשימוש
a = [1, 4, 7]
b = [2, 3, 5, 8]
# מצפה ל־[1, 2, 3, 4, 5, 7, 8]

merged = merge(a, b, key=lambda x: x)
print(merged)


a = [1, 7, 4]   # לא ממוינת
b = [2, 3, 5]

print(merge(a, b, key=lambda x: x))
# מצפה ל־None
