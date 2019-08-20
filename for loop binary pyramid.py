for i in range(1, 7):
    for n in range(1, i + 1):
        if n > 1:
            n = n % 2
        print(n, end=' ')
    print()
