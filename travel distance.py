speed = int(input("enter the speed of vehicle in kmph:  "))  # 40 kmph
time = int(input("enter the hour u've travelled:  "))  # 3 hrs
print("-" * 40)
print("Hour\t\t Distance Travelled")
n = 1
while n <= time:
    distance = speed * time
    print(n, "\t\t\t\t", speed * n)
    n = n + 1
