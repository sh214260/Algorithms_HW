def partition_lomuto_with_key(arr, left, right, key=lambda x: x):
    pivot_value = key(arr[right])
    i = left
    for j in range(left, right):
        if key(arr[j]) < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quick_kth(arr, left, right, k, key=lambda x: x):
    if k < 1 or k > right - left + 1:
        raise ValueError("k is out of bounds")

    if left == right:
        return arr[left]

    # בוחרים pivot לפי הערך של key
    pivot_index = partition_lomuto_with_key(arr, left, right, key)
    pivot_pos = pivot_index - left + 1

    if pivot_pos == k:
        return arr[pivot_index]
    elif k < pivot_pos:
        return quick_kth(arr, left, pivot_index - 1, k, key)
    else:
        return quick_kth(arr, pivot_index + 1, right, k - pivot_pos, key)
