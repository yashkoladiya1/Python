#Strings are immutable

a = "!! yash !!"

#for Length
print(len(a))

#for upperCase
print("upper---",a.upper())

#for Lower
print("lower",a.lower())

#for remove strip first
print("remove strip",a.rstrip("!"))

#for replace 
print("replcae",a.replace("yash","raj"))

#for split
print("split",a.split(" ")) 

#Blogging heading
blog = "introduction of python"
print("blogging heading----",blog.capitalize())

#center text
print("text center----",blog.center(50))

#count 
print("count----",a.count("y"))

#endwith
print("check end text----",a.endswith("!!"))

#find text
print("find text-----",blog.find("of"))

#index text
print("Find index---",blog.find("off"))

#isalnum
print("Find isalnum----",blog.isalnum())

#isspace
g=" "
print("find space---",g.isspace())

#startwith
print("start with---",blog.startswith("introduction"))

#title
print("title----",blog.title())