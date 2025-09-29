#Explicit Typecasting
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum = number + string_number
print("The sum of both the numbers is:",sum)

# Implicit typecasting
a = 11.4
b = 2

print("Implicit Typecasting",a+b)

