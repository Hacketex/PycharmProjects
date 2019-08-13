balance = float(10000)
perct = float(0.05)
lastamt = float(20000)
year = float(0)
pay1 = balance + balance * perct
# print(pay1)
pay2 = balance + pay1 * perct
# print(pay2)
while year < 0:
    # print(year)
    year = year + 1
print()
print("Year   Intrest      Balance  ")
print("-" * 33)
# print(end="")
while balance < lastamt:
    year = year + 1
    intrest = balance * perct
    print("%.d" % year, end="      ")
    print("%.2f" % intrest, end="     ")
    print("%.2f Rs" % balance)
    balance = balance + balance * perct
print("-" * 33)
print("Invested amount = 10,000 Rs\nTotal intrest earned = 989.97 \n%d saal me paisa double" % year)
