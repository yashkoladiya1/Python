"""

*****
*****
*****
*****
*****

"""

for i in range(6):
    print("*" * 5)

"""

*
**
***
****
*****

"""
n = int(input("Enter Number:"))
for i in range(1,n+1):
    print("*"*i)


"""

*****
****
***
**
*

"""

k = int(input("Enter K value: "))
for i in range(k,0,-1):
    print("*"*i)


"""

    *
   ***
  *****
 *******
*********


"""

j = int(input("Enter J value: "))

for i in range(1, j+1):   # rows
    spaces = " " * (j - i)        # spaces before stars
    stars = "*" * (2*i - 1)       # odd number of stars
    print(spaces + stars)