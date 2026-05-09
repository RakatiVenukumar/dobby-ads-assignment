#n= 5
#for  i in range(4):
#    print(" "*(n-1-i),end = "")
#    for j in range(0,i+1):
#        print("*",end = " ")
#    print('') 
    
n = 5
for i in range(3):                    #  *     #   *
    for j in range(3-i-1):            # **     #  * *
        print(" ",end = "")           #***     # * * *
    for j in range(i+1):
        print('*',end = "")
    print("")