freemin = float(input("enter your calling minute limit  :"))  # for 300 min
charge = float(input("limited calling cost Rs.         :"))  # 29.95
extracharge = float(input("additional charge Rs/min         :"))  # rs 0.45 for additional 1 min
tax = float(12.5)
finalcharge = float(input("enter your billing cost Rs.      :"))  # 33.70
addmin = finalcharge - charge  # 33.70-29.95 = 3.75 rs. extra charge in bill
additional = addmin * tax / 100
print()
print()
print("-" * 41)
print("\t\t\tBilling Details")
print("-" * 41)
print("minimum bill               = %.2f Rs" % charge)
print("total intrest              = %.1f%%" % tax)
print("additional                 = %.2f Rs" % additional)
print("Your free calling minute   = %d Rs" % freemin)
print("additional minutes cost    = %.2f Rs" % addmin)
charge2min = addmin / extracharge  # 3.75/0.45 = 8.33     8 min 33 sec extra
print("additional minute          = %.2f min" % charge2min)
answer = (addmin + charge) * tax / 100 + addmin + charge
print("Total charges with tax     = %.2f Rs" % answer)
answer2 = addmin + charge * 1.125
print("-" * 41)
