#Question 1:
"""

Write a Python function called is_even that takes a single integer as an argument and returns True if the number is even, and False if it is odd.

"""


def iseven(n):
    if(n % 2 == 0):
        return True
    else:
        return False

n = int(input("Enter N value: "))
ans = iseven(n)
print("ans---->",ans)