#default arguments
def average(a=5,b=1):
    print("default Average--->",(a+b)/2)

average()

#Keyword arguments
def average2(a,b):
    print("Keyword Average--->",(a+b)/2)

average2(b=6,a=5)

#Required Arguments

def average3(a,b,c=1):
    print("Required Average--->",(a+b+c)/2)

average3(b=6,a=5)

#variable argument

def average4(*number):#tuple *
    sum = 0
    for i in number:
        sum = sum + i
    print("variable averge--->",sum/len(number))

average4(1,2,3,4,5)

def average5(**names):#dict
    print("Yash",names["mname"],names["lname"])

average5(mname = "sureshbhai", lname = "Koladiya")

#return functions
def average6(*number):#tuple *
    sum = 0
    for i in number:
        sum = sum + i
    return sum/len(number)

c = average6(1,2,3,4,5)

print(c)