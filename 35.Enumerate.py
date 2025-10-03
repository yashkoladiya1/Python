marks = [11,23,2,45,23,53]
for index,mark in enumerate(marks):
    print(index,mark)


# Without enumerate
for i in range(len(fruits)):
    print(i, fruits[i])

# With enumerate (better)
for i, fruit in enumerate(fruits):
    print(i, fruit)