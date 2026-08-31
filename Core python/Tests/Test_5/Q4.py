numbers = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
print(frequency)