sum1 = 0
word = ' '
while word != '':
    word = input("enter the word or press enter to exit: ")
    print(len(word))
    count = len(word)
    sum1 = sum1 + count
print("total word is ", sum1)

# key='yes'
# while key=='yes':
#    word=input("enter the word:  ")
#    count=len(word)
#    print(count)
#   if word=='':
#       key='no'
#    sum=sum+count
# print(sum)
