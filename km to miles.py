kms = 1.60934  #kms
mile = 10
m = 10
print("\t kms \t     miles")
print('-'*28)
while mile <= 800:
    mile = mile * kms
    print(" " * 5 + f'{m:d}' + " " * 10 + "%d" % round(mile))
    mile = mile + 10
    m = m + 10