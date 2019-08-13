user_sleep: int = int(input("how many hours you sleep in a day: "))
desirable_sleep: int = 8
week = user_sleep * 7
if user_sleep > desirable_sleep:
    sleep = week - (desirable_sleep * 7)
    print("you sleep %d hours in a week \n extra sleep per day: %d hours" % (week, user_sleep - 8))
    print("total extra sleep in a week: %d hours" % sleep)
    print("congratulations you have completed PHD in sleeping ")
else:
    print("you sleep %d hours in a week" % week)
