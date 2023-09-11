list=[10,3,4,3,5,7,7,9]
uniques=[]

for numbers in list:
    if numbers not in uniques:
        uniques.append(numbers)

print(uniques)