from section5 import max_heapify

def build_max_heap(arr, key=lambda x: x):
    heap_size = len(arr)
    # מתחילים מהצומת הפנימי האחרון ומתקדמים לאחור עד השורש
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(arr, i, heap_size, key)


# דוגמאות שימוש
if __name__ == "__main__":
    # דוגמה 1: מערך רגיל
    arr1 = [4, 10, 3, 5, 1]
    print(f"מערך לפני: {arr1}")
    build_max_heap(arr1)
    print(f"מערך אחרי build_max_heap: {arr1}")
    print()
    
   