#Question 5 (Level: Medium):
# Write a Python function called remove_duplicates that takes a list as input and returns a new list with all duplicate elements removed, preserving the original order

def remove_duplicates(lst):
    newList = []
    for i in lst:
        if i not in newList:
            newList.append(i)
    return newList

lst = list(map(int, input("Enter space-separated numbers: ").split()))
rvs = remove_duplicates(lst)
print(rvs)