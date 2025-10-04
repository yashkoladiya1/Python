file = open("myfile.txt","r")
line1 = file.readline()
line2 = file.readline()
lines = file.readlines()
print(line1)
print(line2)
print(lines)
file.close()

# file.tell(): Returns the current position of the cursor.
with open('myfile.txt', 'r') as file:
    print(file.tell())  # 0
    file.read(5)
    print(file.tell())  # 5
    file.seek(0)
    print(file.read(5))  # Reads first 5 characters again