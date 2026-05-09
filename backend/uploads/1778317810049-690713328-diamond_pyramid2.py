for i in range(3):
    print(" "*(3-i-1),end = '')
    for j in range(2*i+1):
        print("*",end ='')
    print("")

for i in range(3):
    print(" "*(i),end='')
    for j in range(5-i*2):
        print("*",end ='')
    print('')
