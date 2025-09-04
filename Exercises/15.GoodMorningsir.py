import time

HourStamp = int(time.strftime("%H"))

if(HourStamp <= 12):
    print("Good Morning Sir")
elif(HourStamp >=12):
    if(HourStamp >= 17 and HourStamp<= 21):
        print("Good evening Sir")
    else:
        print("Good Night Sir")
else:
    print("Good after Noon sir")

