#Question 8 (Level: Medium):
# Write a Python function called fizz_buzz that takes an integer n as input and returns a list of numbers from 1 to n (inclusive), but for multiples of 3, add "Fizz" instead of the number, for multiples of 5, add "Buzz", and for multiples of both 3 and 5, add "FizzBuzz".


def fizz_buzz(n):

    for i in range(1,n):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0):
            print("Fizz")
        elif(i%5==0):
            print("Buzz")
        else:
            print(i)


n = int(input("Enter Number:"))
fizz_buzz(n)