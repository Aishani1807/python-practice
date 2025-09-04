import time
timestamp=int(time.strftime('%H'))
if 5<=timestamp<12:
    print("Good morning Sir")
elif 12<=timestamp<18:
    print("Good afternoon Sir")
else:
    print("Good evening Sir")