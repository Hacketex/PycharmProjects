print("    time calculator")
seconds = int(input("enter the seconds:  "))
minute = float(seconds / 60)
hour = float(seconds / 3600)
days = int(seconds / 86400)
if seconds >= 60:
    print("min = %.2f" % minute)
    if seconds >= 3600:
        print("hour = %.2f", hour)
        if seconds >= 86400:
            print("days = ", days)
else:
    print("0")