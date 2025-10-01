#List syntax
marks = [3,4,6,2,"yash","raj",2,6]
print(marks)

#access List element
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

#slicing in List
print(marks[1:3])

#negative slicing
print(marks[-4:-2])

#jumpindex
print(marks[1:8:2])

#list comprehension
lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0] #with condition
print(lst)