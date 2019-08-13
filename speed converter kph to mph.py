kph = float(60)
mph = float(kph * 0.621)
speed = float(10)
# print(mph)
stop = 140
# while kph<stop:
#    print(mph)
#    mph=mph*speed;
for i in range(60, 140, 10):
    print("%d" % i)
while mph < kph:
    print(mph)
    mph = kph * speed
