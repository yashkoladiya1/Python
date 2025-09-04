#break
tableNum = int(input("enter Number"))

for i in range(12):
    print(tableNum ,"X",i,"=",tableNum*i)
    if(i ==10):
        break

#continue

for i in range(12):
    if(i ==11):
        print("skip the iteration")
        continue
    print(tableNum ,"X",i,"=",tableNum*i)