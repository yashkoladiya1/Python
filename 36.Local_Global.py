#Global Variables
# Declared outsid'e any function.
# Accessible everywhere in the file (functions, loops, etc.).
# Lives as long as the program runs.

x = 10   # global variable

def show():
    print("Inside function:", x)

show()
print("Outside function:", x)


#Local Variables
def show():
    y = 20   # local variable
    print("Inside function:", y)

show()
print("Outside function:", y)   # ❌ NameError (y not defined outside)


#Global vs Local Conflict
x = 10  # global

def test():
    x = 5   # local with same name
    print("Inside function:", x)

test()
print("Outside function:", x)

#Using global Keyword
x = 10

def change():
    global x
    x = 50   # modifies global x
    print("Inside function:", x)

change()
print("Outside function:", x)