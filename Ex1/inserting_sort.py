with open("data.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key

for num in numbers:
    print(num)
