amt, last, total, end, yr, year = (20000, 26878, 20000, 26878, 1, 1)
print("3% Increment   Semister   Year    Total-Payment ")
while year <= 5:
    sem = 1
    while sem <= 2 and amt < last and total <= last and yr <= 5.9:
        data = amt * 3 / 100
        print("   %.2f" % data, " " * 10, end='')
        print("%d" % sem, end=" ")
        if yr > 2:
            yr = yr * 0.9
            if yr > 4:
                yr = yr - 0.3
        yr = yr * 1.3
        print("\t\t%d" % yr, end="  ")
        payment = data + amt
        print(" \t %.2f" % payment)
        # print(" " * 10 + f'{data:.2f}' + " " * 10 + f'{sem:d}' + " " * 10 + "%d"%round(yr) + " " * 10 + f'{payment:.2f}' + " " * 10)
        amt = amt + amt * 3 / 100
        sem = sem + 1
    year = year + 1
