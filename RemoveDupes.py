numbers = [5,2,1,7,4,2,4,7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)