a = 24
b = 34.67
c = 576.84
d = 98
n = 1
# print("%24d %10.2f %10.2f %10d "%(a,b,c,d))
print(" " * 10 + f'{a:d}' + " " * 10 + f'{b:.2f}' + " " * 10 + f'{d:.2f}')
while n <= 10:
    print(f'{n:d}' + f'{b:.2f}')
    n = n + 1
