#for  i in range(4):
#   print(" "*(i),end = "")
#   for j in range(0,4-i):
#       print("*",end = "")
#   print('') 
    

n = 3
for i in range(3):                        # ***        # * * *
    for j in range(i):                    #  **        #  * *
        print(" ",end = "")               #   *        #   *
    for j in range(0,3-i):
        print("*",end = "")
    print('')
