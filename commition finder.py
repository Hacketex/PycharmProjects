key = "y"
n = 1
comm_rate = 2.5
while key == 'y':
    product = int(input("Enter the number of product   "))
    while n <= product:
        sales = float(input("Enter the sale of product %d    " % n))
        commision = sales * (comm_rate / 100)
        print("The commision of product %d is %.2f" % (n, commision))
        n = n + 1
    n = 1
    key = input("Do you want to continue (y/n) ")
