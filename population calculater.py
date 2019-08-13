no_of_organisms = int(input("starting number of organisms: "))
avrage = int(input("avrage daily increase: "))
days = int(input("number of days to multiply: "))
avr = no_of_organisms * avrage / 100
total = days * no_of_organisms + avr
n = 1
print("Days\tApproximate Population")
while n <= days:
    while no_of_organisms <= total:
        daily_increase_avrage = no_of_organisms * avrage / 100
        no_of_organisms = no_of_organisms + daily_increase_avrage
        print(n, end="   ")
        print("\t\t%f" % (no_of_organisms))
        n = n + 1
