def partition_two_pivots(a, p, q, key=lambda x: x):
    if key(p) > key(q):
        p, q = q, p  # נוודא ש-p <= q

    low = 0
    mid = 0
    high = len(a) - 1

    while mid <= high:
        if key(a[mid]) < key(p):
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1

        elif key(a[mid]) > key(q):
            a[mid], a[high] = a[high], a[mid]
            high -= 1

        else:
            mid += 1

    return low, high  # גבולות האזור האמצעי
