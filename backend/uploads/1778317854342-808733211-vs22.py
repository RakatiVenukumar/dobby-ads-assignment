# full pyramid
n = 3
for i in range (3):
    for j in range(i,n):
        print(" ",end = "")
    for j in range (i):
        print("*", end = "")
    for j in range(i+1):
        print("*", end = "") 
    print()