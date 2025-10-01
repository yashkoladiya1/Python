#List syntax
Tup = (3,4,6,2,"yash","raj",2,6)
print(Tup)

#access List element
print(Tup[0])
print(Tup[1])
print(Tup[2])
print(Tup[3])

#slicing in List
print(Tup[1:3])

#negative slicing
print(Tup[-4:-2])

#jumpindex
print(Tup[1:8:2])

#list comprehension
lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0] #with condition
print(lst)