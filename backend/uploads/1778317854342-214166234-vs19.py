#factorial of the given number
num = int(input("enter the number: "))
factorial = 1
for i in range(1,num+1):
    if(num == 1 and num == 0):
        print(1)
    else:
        factorial = factorial * i
        print(factorial)        
    