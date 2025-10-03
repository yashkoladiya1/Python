#reading a file
# f = open("myfile.txt","r")
# text = f.read()
# print(text)
# f.close()

#writing a file
# f = open("myfile.txt","w")
# f.write("Hello World")
# f.close()

#with
with open("myfile.txt","a") as f:
    f.write("I am Yash")