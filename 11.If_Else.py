a = int(input("Enter a: "))

#conditional operator
# > < <= >= == 
# print(a<18)
# print(a>18)
# print(a>=18)
# print(a<=18)
# print(a==18)

if(a<18):
    print("you cannot drive")
else:
    print("you can drive2")


#if-else statement
num = int(input("enter the Num: "))

if(num>=0):
    print("number is positive")
else:
    print("number is negative")



#if-elif else
num2 = int(input("enter the Num: "))

if(num2>=0 and num2<=19):
    print("number is positive")
elif(num2>=20):
    print("number is special")
else:
    print("number is negative")


#nested if else

num3 = int(input("enter the Num: "))

if(num3 < 0):
    print("number is negative")
elif(num3 > 0):
    if(num3 <=10):
        print("number is between 1 to 19")
    elif(num3 > 10 and num3 < 20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")