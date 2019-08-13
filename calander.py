# author=pratik
# created date=2 aug 2019
# https://github.com/hacketex
month = int(input("enter the number of month between 1-12 :  "))
if month < 4:
    print("number is in first quarter")
elif month < 7:
    print("number is in second qurter")
elif month < 10:
    print("num is in third quater")
else:
    print("number is in fourth quarter")
