# A set is a collection of unique, unordered elements.
# Written with { } curly brackets.
# Duplicates are automatically removed.

# Creating a set
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)  #unordered elements.

for i in fruits:
    print(i)

# Empty set
s = set()

# From a list
numbers = set([1, 2, 3, 2, 1])
print(numbers)  # {1, 2, 3}

fruits = {"apple", "banana"}

fruits.add("cherry")       # add one item
print(fruits)

fruits.update(["mango", "orange"])  # add multiple items
print(fruits)

fruits.remove("banana")    # remove item (error if not found)
print(fruits)

fruits.discard("banana")   # remove safely (no error if not found)
print(fruits)

fruits.clear()             # remove all items
print(fruits)              # set()


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))          # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))   # {3, 4}
print(a.difference(b))     # {1, 2}
print(b.difference(a))     # {5, 6}
print(a.symmetric_difference(b))  # {1, 2, 5, 6}


nums = {1, 2, 3}

print(len(nums))            # 3
print(2 in nums)            # True
print(5 in nums)            # False

nums_copy = nums.copy()     # copy set
print(nums_copy)

# Subset & Superset
x = {1, 2}
y = {1, 2, 3}
print(x.issubset(y))        # True
print(y.issuperset(x))      # True
