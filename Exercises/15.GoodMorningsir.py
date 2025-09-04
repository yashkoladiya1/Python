import time

HourStamp = int(time.strftime("%H"))

if HourStamp < 12:
    print("Good Morning Sir")
elif 12 <= HourStamp < 17:
    print("Good Afternoon Sir")
elif 17 <= HourStamp <= 21:
    print("Good Evening Sir")
else:
    print("Good Night Sir")