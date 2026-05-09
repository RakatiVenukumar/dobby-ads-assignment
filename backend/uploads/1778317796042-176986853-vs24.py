# fibonacci series
f1 = 0
f2 = 1
next_term = f1 + f2
n = int(input("enter the number: "))
print("the fibonacci series is",f1,f2)
for i in range (3,n):
    print(next_term)
    f1 = f2
    f2 = next_term
    next_term = f1 + f2  
    