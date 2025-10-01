def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#fibbonacci
def fibbonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)

print("fibo---->",fibbonacci(3))