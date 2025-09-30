#length method
a = "!!!!Yash!!!! yash esqa"
b = "fdaf24"
c = " "
print("length---->",len(a))

#strings are immutable

#uppercase
print("upper case---->",a.upper())

#lowercase
print("Lower case---->",a.lower())

#rstrip
print("rstrip method---->",a.rstrip("!"))

#replace
print("replace method---->",a.replace("Y","J"))

#split method
print("split method---->",a.split(" "))

#capitalize
blogHeading = "introduction of js"
print("capitalize---->",blogHeading.capitalize())

#center
print("center---->",a.center(50))

#count
print("count---->",a.count("yash"))

#endwith
print("endwith---->",a.endswith("qa"))
print("endwith---->",a.endswith("sh",13,17))

#find method
print("find--->",a.find("yash"))

#index
# print("Index---->",a.index("yashhh"))

#isalnum
print("isalnum---->",b.isalnum())

#isalpha
print("isalpha---->",b.isalpha())

#isprintable
print("isprintable---->",b.isprintable())

#isspace
print("isspace---->",c.isspace())

#swapcase
print("swapcase---->",b.swapcase())