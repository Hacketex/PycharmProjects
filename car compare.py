#author=pratik
#created date=12 jun 2019
#last modified date=13 jun 2019
#http://github.com/hacketex
print()
print("-"*100)
print("                                        Welcome to Car House ")
print("-"*100)
print()
print("            Enter the details to compare the cars")
print()
car1=input("Enter the first car name              :")
car2=input("Enter the second car name             :")
price1=int(input("Enter the %s car price            :"%(car1)))
price2=int(input("Enter the %s car price             :"%(car2)))
avr1=int(input("Enter the avarage of %s car       :"%(car1)))
avr2=int(input("Enter the avarage of %s car        :"%(car2)))
yr1=int(input("Years you want to use the car         :"))
petrol=int(input("Petrol price per liter                :"))
kmpy=int(input("km car drive per year                 :"))
calc1=kmpy*yr1
car1totalltr=kmpy/avr1
car2totalltr=kmpy/avr2
cost1petrol=car1totalltr*petrol
cost2petrol=car2totalltr*petrol
total1=cost1petrol*yr1
total2=cost2petrol*yr1
car1cost=total1+price1
car2cost=total2+price2
print()
print("_"*100)
print("                                         Compare Table  ")
print("_"*100)
print("Car Name                        : %s"%(car1),end="\t\t|\t\t")
print("Car Name                        : %s"%(car2))
print("Car Price                       : %d Rs"%(price1),end="\t\t|\t\t")
print("Car Price                       : %d Rs"%(price2))
print("Car avarage                     : %d kmpl"%(avr1),end="\t\t|\t\t")
print("Car avarage                     : %d kmpl"%(avr2))
print("Operating Year                  : %d years"%(yr1),end="\t\t|\t\t")
print("Operating Year                  : %d years"%(yr1))
print("Operating Year km in %d years   : %d km"%(yr1,calc1),end="\t\t|\t\t")
print("Operating Year km in %d years   : %d km"%(yr1,calc1))
print("Petrol cost in %d years         : %d Rs"%(yr1,total1),end="\t|\t\t")
print("Petrol cost in %d years         : %d Rs"%(yr1,total2))
print("_"*100)
print()
if car1cost>car2cost:
    sub=car1cost-car2cost
    print("%s car is better than %s.\nTotal Cost        = Rs %d\n%s Total Cost = Rs %d\nYou Save          = Rs %d"%(car2,car1,car2cost,car1,car1cost,sub))
else:
    sub2=car2cost-car1cost
    print("%s car is better than %s.\nTotal Cost        = Rs.%d\n%s Total Cost  = Rs %d\nYou Save          = Rs %d"%(car1,car2,car1cost,car2,car2cost,sub2))