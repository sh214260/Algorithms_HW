from section6 import build_max_heap
from section5 import max_heapify

def heap_sort(arr, key=lambda x: x):
    build_max_heap(arr, key)
    heap_size = len(arr)

    # בכל צעד מעבירים את המקסימום לסוף ומקטינים את הערימה
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size, key)


# דוגמה
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print(f"מערך לפני מיון: {arr}")
    heap_sort(arr)
    print(f"מערך אחרי מיון: {arr}")