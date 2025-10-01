#change Tuple

countries = ("India", "Germanay", "Canada", "America")
temp = list(countries)
temp.append("Russia")
temp.pop(2)
temp[2] = "autria"
countries = tuple(temp)
print("Change Tuple--->",countries)


#new tuple
countries = ("India", "Germanay", "Canada", "America")
countries2 = ( "Russia", "Autria")
countries3 = countries + countries2
print("New Tuple--->",countries3)

#count
print("count:",countries.count("India"))

#jumpindex
print(countries3[1:4:2])