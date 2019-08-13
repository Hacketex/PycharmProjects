# author=pratik
# created date=2 aug 2019
# last modified date=11 aug 2019
# https://github.com/hacketex
year = int(input("enter the year to check :  "))
four = year % 4
hundred = year % 100
last = year % 400
if four == 0:
    print("leap year")
    if hundred == 0:
        print('leap year')
        if last == 0:
            print("leap year")
else:
    print('not a leap year')
