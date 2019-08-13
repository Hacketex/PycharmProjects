# author=pratik
# created date=13 jun 2019
# last modified date=13 jun 2019
# http://github.com/hacketex
a = int(input("enter the first number  "))
b = int(input("enter the second number  "))
c = int(input("enter the tird number  "))
d = int(input("enter the fourth number  "))
if a > b and a > c and a > d:
    print("%d is greater than %d, %d and %d" % (a, b, c, d))
elif b > a and b > c and b > d:
    print("%d is greater than %d, %d and %d" % (b, a, c, d))
elif c > a and c > b and c > d:
    print("%d is greater than %d, %d and %d" % (c, b, a, d))
else:
    print("%d is greater than %d, %d and %d" % (d, b, c, a))
