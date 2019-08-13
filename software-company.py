# author=pratik
# created date=2 aug 2019
# modified date=11 aug 2019
# https://github.com/hacketex
price, n = (99, 10)
que = int(input("enter the no of package purchased: "))
actual_price = price * que
discount = actual_price * n / 100
total = actual_price - discount
if que >= 10:
    if que >= 20:
        n = 20
        if que >= 50:
            n = 30
            if que >= 100:
                n = 40
print("actual price = %d \ndiscount=%d\ntotal=%d\nyou got %d percent discount" % (actual_price, discount, total, n))
