# normal string
a = "Yash"
print("Normal string\n",a)

# long string
b = ''' hello i am boy
and studying in the university

i am yash
 '''

print("Long string\n",b)

#accessing characters of a string
c= "abcd"

print(c[0])
print(c[1])
print(c[2])
print(c[3])
print("looping start")
# print(c[4]) throws an error

#looping through the string
d = '''
I am yash

22 years old

master student
'''
for character in d:
    print(character)

#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)