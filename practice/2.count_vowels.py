#Question 2 (Level: Easy):
# Write a Python function called count_vowels that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string (case-insensitive).

def count_vowels(n):
    count = 0
    vowels = "aeiouAEIOU"
    for i in n:
        if i in vowels:
            count += 1
    return count

word = input("Enter word: ")
count = count_vowels(word)
print(count)
