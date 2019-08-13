# author=pratik
# created date=2 aug 2019
# https://github.com/hacketex
weight = int(input("enter the weight :  "))
if weight < 3:
    a = weight * 1.50
    print("shiping charges= %d\nrate per pound 1.5" % a)
elif weight < 7:
    b = weight * 3.00
    print("shiping charges= %d\nrate per pound 3.00" % b)
elif weight < 11:
    c = weight * 4.00
    print("shiping charges= %d\nrate per pound 4.00" % c)
else:
    d = weight * 4.75
    print("shiping charges= %d\nrate per pound 4.75" % d)
