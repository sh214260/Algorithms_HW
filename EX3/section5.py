from section4 import left, right

def max_heapify(arr, i, heap_size, key=lambda x: x):
    largest = i
    l = left(i)
    r = right(i)

    if l < heap_size and key(arr[l]) > key(arr[largest]):
        largest = l

    if r < heap_size and key(arr[r]) > key(arr[largest]):
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size, key)