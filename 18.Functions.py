# There are two types of functions
# 1. Built in function
# 2. User-defined funcations

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("second number is greater")

def isLesser():
    pass

a = 23
b = 2
isGreater(a,b)
calculateGmean(a,b)