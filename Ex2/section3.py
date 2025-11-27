import heapq

def merge_sorted_lists(lists, key):
    heap = []
    result = []

    # הכנסה התחלתית של האיבר הראשון מכל רשימה לערימת-עזר (heap)
    for i, lst in enumerate(lists):
        if lst:  # רק אם הרשימה לא ריקה
            heapq.heappush(heap, (key(lst[0]), i, 0, lst[0]))

    # שליפה לפי סדר והחזרת הרשומות הממוינות
    while heap:
        _, list_index, item_index, value = heapq.heappop(heap)
        result.append(value)

        # הכנסה של האיבר הבא מאותה רשימה
        next_index = item_index + 1
        if next_index < len(lists[list_index]):
            next_value = lists[list_index][next_index]
            heapq.heappush(heap, (key(next_value), list_index, next_index, next_value))

    return result

# דוגמה לשימוש
list1 = [(1, 'a'), (4, 'd'), (7, 'g')]
list2 = [(2, 'b'), (3, 'c'), (5, 'e'), (8, 'h')]
list3 = [(0, 'z'), (6, 'f'), (9, '  i')]            
merged = merge_sorted_lists([list1, list2, list3], key=lambda x: x[0])
print(merged)   