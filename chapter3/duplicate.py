numbers = [2, 3, 5, 2, 4, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
