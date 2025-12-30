def left(i):
    """מחזיר את האינדקס של הילד השמאלי"""
    return 2 * i + 1


def right(i):
    """מחזיר את האינדקס של הילד הימני"""
    return 2 * i + 2


def is_max_heap(arr, i=0, key=lambda x: x):
    
    n = len(arr)
    # עוברים על כל האינדקסים החל מ-i+1
    for j in range(i + 1, n):
        # מחשבים את האינדקס של ה-parent
        parent_idx = (j - 1) // 2
        
        # אם ה-parent קטן מהילד, זו לא ערימת מקסימום
        if key(arr[parent_idx]) < key(arr[j]):
            return False
    
    return True


# דוגמאות שימוש
if __name__ == "__main__":
    # ערימת מקסימום תקינה
    heap1 = [10, 8, 6, 5, 3, 2, 1]
    print(f"האם {heap1} היא ערימת מקסימום? {is_max_heap(heap1)}")
    
    # לא ערימת מקסימום
    heap2 = [10, 8, 6, 9, 3, 2, 1]
    print(f"האם {heap2} היא ערימת מקסימום? {is_max_heap(heap2)}")
    
    # ערימת מקסימום תקינה עם טאפלים
    heap3 = [(10, 'a'), (8, 'b'), (6, 'c'), (5, 'd'), (3, 'e')]
    print(f"האם {heap3} היא ערימת מקסימום? {is_max_heap(heap3, key=lambda x: x[0])}")
    
    # בדיקה החל מאינדקס מסוים
    heap4 = [100, 50, 40, 30, 20, 10, 5]
    print(f"האם {heap4} היא ערימת מקסימום החל מאינדקס 1? {is_max_heap(heap4, i=1)}")
    
    # מערך שאינו ערימת מקסימום מהתחלה אבל כן מאינדקס מסוים
    heap5 = [5, 50, 40, 30, 20, 10, 5]
    print(f"האם {heap5} היא ערימת מקסימום? {is_max_heap(heap5)}")
    print(f"האם {heap5} היא ערימת מקסימום החל מאינדקס 1? {is_max_heap(heap5, i=1)}")
