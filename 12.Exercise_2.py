import time
timestamp = int(time.strftime("%H"))

if(timestamp >= 6 and timestamp <= 12):
    print("Good Morning Sir")
elif(timestamp > 12 and timestamp <= 18):
    if(timestamp > 12 and timestamp <= 16):
        print("Good Afternoon sir")
    else:
        print("Good Evening Sir")
else:
    print("Good night sir")