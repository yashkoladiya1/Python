#Question 7 (Level: Medium):
# Write a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise. The function should ignore case and spaces.

def is_palindrome(st):
    st = st.replace(" ", "").lower() 
    if(st == st[::-1]):
      return True
    else:
        return False

st = input("Enter a String: ")
ans = is_palindrome(st)
print(ans)

