#Question 3 (Level: Easy):
# Write a Python function called reverse_list that takes a list as input and returns a new list with the elements in reverse order.

def reverse_list(lst):
    lst.reverse()
    return lst

lst = list(map(int, input("Enter space-separated numbers: ").split()))
rvs = reverse_list(lst)
print(rvs)
