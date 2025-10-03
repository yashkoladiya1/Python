#Raising Your Own Exceptions
x = -1
if (x < 0):
    raise ValueError("x cannot be negative")

#Custom Exception Class
class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong!")
except MyError as e:
    print("Caught custom error:", e)