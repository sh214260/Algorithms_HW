def partition_lomuto(a, key):
    pivot = key(a[-1])          # המפתח של האיבר האחרון
    i = -1

    for j in range(len(a) - 1):
        if key(a[j]) <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[-1] = a[-1], a[i+1]
    return i + 1  # אינדקס ה-pivot החדש

def partition_hoare(a, key):
    pivot = key(a[0])
    i = -1
    j = len(a)

    while True:
        # התקדמות מימין לשמאל
        j -= 1
        while key(a[j]) > pivot:
            j -= 1

        # התקדמות משמאל לימין
        i += 1
        while key(a[i]) < pivot:
            i += 1

        if i >= j:
            return j   # נקודת החיתוך

        a[i], a[j] = a[j], a[i]
