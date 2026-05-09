n = 29
if n == 1:
    print('1 is not a prime number')
else:
    for i in range(2,n+1):
        if n%i == 0:
            print(f"{n} is not a prime number")
            break
        else:
            print(f"{n} is a prime number")
