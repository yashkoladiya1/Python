list1 = [6,7,8,9,1,2,3,4,5,1]

#append method
list1.append(10)
print("after append:", list1)

#sort method
list1.sort()
print("after sort:", list1)

#reverse method
list1.reverse()
print("after reverse:", list1)

#index method
print("Index---->",list1.index(1))

#count
print("count:",list1.count(1))

#copy
cl = list1.copy()
print(cl)

#insert
list1.insert(1,2)
print(list1)

#extend
m = [4234,234,123,435,3]
list1.extend(m)
print("extend---->",list1)

#concatenating
k = list1 + m
print(k)