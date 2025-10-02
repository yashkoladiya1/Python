#  What is a Dictionary?

# A dictionary stores data in key–value pairs.
# Keys must be unique & immutable (string, number, tuple).
# Values can be anything.

student = {
    "name": "Alice",
    "age": 21,
    "course": "Data Science"
}

print(student["name"])    # ❌ KeyError: 'grade'
print(student.get("age"))  # None (instead of error)



student = {"name": "Alice", "age": 22, "course": "AI"}

print(student.keys())      # dict_keys(['name', 'age', 'course'])
print(student.values())    # dict_values(['Alice', 22, 'AI'])
print(student.items())     # dict_items([('name', 'Alice'), ('age', 22), ('course', 'AI')])

# Copy dictionary
copy_student = student.copy()
print(copy_student)

# Check key existence
print("age" in student)    # True
print("grade" in student)  # False

student = {"name": "Alice", "age": 22, "course": "AI"}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key & Value
for key, value in student.items():
    print(key, ":", value)


students = {
    "s1": {"name": "Alice", "age": 22},
    "s2": {"name": "Bob", "age": 23}
}

print(students["s1"]["name"])  # Alice