#Question 4 (Level: Medium):
# Write a Python function called find_max_min that takes a list of numbers as input and returns a tuple containing the maximum and minimum numbers in the list.

def find_max_min(lst):
    max_value = lst[0]
    min_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return (max_value, min_value)

lst = list(map(int, input("Enter space-separated numbers: ").split()))
rvs = find_max_min(lst)
print(rvs)