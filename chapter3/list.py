numbers = [3, 4, 7, 10, 14]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
numbers.sort()
numbers.reverse()
print(numbers)