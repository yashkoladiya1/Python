#What are Exceptions?
# An exception is an error that happens during program execution.
# If not handled, Python stops the program and s''hows a traceback.

#Basic Exception Handling
try:
    x=10/0
except ZeroDivisionError:
    print("You cannot divide by zero!")

#Multiple except Blocks
try:
    num=int("abc")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid number format")

#Catching All Exceptions
try:
    x = 10 / 0
except Exception as e:
    print("Error:", e)

#else Block with Exceptions
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error: cannot divide by zero")
else:
    print("Division successful, result =", x)

