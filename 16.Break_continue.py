Num = int(input("Enter Number: "))
for i in range(1,11):
    print(Num, "*", i , "=",Num * i)


#break
Num = int(input("Enter Number: "))
for i in range(1,11):
    if(i == 10):
        break
    print(Num, "*", i , "=",Num * i)

#continue
Num = int(input("Enter Number: "))
for i in range(1,11):
    if(i == 8):
        continue
    print(Num, "*", i , "=",Num * i)