#  else with for 'and while loops

# The else block runs only if the loop finishes normally (without hitting a break).
# If the loop is exited by break, the else block is skipped'

#for ... else
for i in range(5):
    print(i)
else:
    print("Loop finished without break.")


# Loop with break
for i in range(5):
    if i == 3:
        print("Breaking at", i)
        break
    print(i)
else:
    print("Loop finished normally.")

#while ... else
x = 0
while x < 3:
    print(x)
    x += 1
else:
    print("Loop ended normally.")