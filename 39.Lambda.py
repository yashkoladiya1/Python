#What is a Lambda Function?
"""A lambda function in Python is a small anonymous function, defined with the keyword lambda. They are often used for short, simple functions that are not reused elsewhere."""

#Basic Syntax
#lambda arguments: expression

def add(x, y):
    return x + y

add = lambda x, y: x + y
print(add(2, 3))  

#Where are Lambda Functions Used?
# Lambda functions are commonly used with functions like map(), filter(), and sorted()

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # Output: [2, 4, 6]

pairs = [(2, 'two'), (1, 'one'), (3, 'three')]
pairs_sorted = sorted(pairs, key=lambda x: x[1])
print(pairs_sorted)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (1*2*3*4)