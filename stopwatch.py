no_of_round = int(input("enter the number of round:  "))
n = 1
while n <= no_of_round:
    lap = float(input("enter the lap time for %d lap:  " % n))
    slow = fast = lap
    if slow < lap:
        slow = lap
        # print("slower",slow)
    else:
        fast = lap
        # print("fast",fast)
    n = n + 1
print("total round = %d\nslowest lap = %d\nfastest lap =%d" % (n, slow, fast))
