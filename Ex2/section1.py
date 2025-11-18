from random_tuples import create_random_tuples

# מייצרים 5 טאפלים, כל אחד: (int, float, str)
tuples_list = create_random_tuples(5, 3, [int, float, str])

print("The original list of tuples:")
for t in tuples_list:
    print(t)

# מיון לפי הרכיב הראשון (int)
sorted_by_int = sorted(tuples_list, key=lambda x: x[0])
print("\nint sorted by the first element (int):")
for t in sorted_by_int:
    print(t)

# מיון לפי הרכיב השני (float)
sorted_by_float = sorted(tuples_list, key=lambda x: x[1])
print("\nfloat sorted by the second element (float):")
for t in sorted_by_float:
    print(t)

# מיון לפי הרכיב השלישי (str)
sorted_by_str = sorted(tuples_list, key=lambda x: x[2])
print("\nstr sorted by the third element (str):")
for t in sorted_by_str:
    print(t)
