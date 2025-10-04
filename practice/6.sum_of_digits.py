#Question 6 (Level: Medium):
# Write a Python function called sum_of_digits that takes an integer as input and returns the sum of its digits. The function should work for both positive and negative integers.


def sum_of_digits(n):
    sum = 0
    for i in n:
        sum = sum + int(i) 
    print(sum)

    
    

n = list(input("Enter: "))
sum_of_digits(n)
