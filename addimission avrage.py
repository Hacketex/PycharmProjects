check = int(input(" enter the number of year to check:  "))
a = 1
sum1 = 0
while a <= check:
    print("    student addmission for %d year" % a)
    b = 1
    while b <= 12:
        month = int(input("enter the number of addmision in %d month:  " % b))
        sum1 = sum1 + month
        b = b + 1
    avr = sum1 / 12
    print("-"*45)
    print("total student addmission in %d year = %d \navrage addmission in %d year = %d\n" % (a, sum1, a, avr))
    a = a + 1