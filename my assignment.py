for i in range(0, 20):
    for j in range(i):
        #if j > 1:
            j = j % 2
         #   print(j)
    if i > 1:
        i = i // 2
        print(f'{i:d}' + ' '*2 + f'{j:d}')
        #print(f'{i:d}')

#    if i > 1:
#        i = i // 2
#        print(i)
# for j in range(0, 20):
#    print('*',end=' ')
