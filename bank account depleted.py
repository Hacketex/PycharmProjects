account = 10000
intrest = 0.5
month = 1
print('month     withdrawal      balance ')
while account != 0 and month <= 100:
    tax = account * intrest / 100
    total = account + tax
    if month > 12:
        month = 1
    print(" " * 3 + f'{month:d}' + " " * 8 + "500" + " " * 11 + f'{total:.2f}')
    month = month + 1
    account = account - 500
    # account = account - 500 * intrest
