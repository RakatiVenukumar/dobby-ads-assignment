# fibonacci series using recursion
def fib (n):
    if(n <= 1):
        return n
    else:
        return (fib(n-1)+fib(n-2))
    
a = fib(10)
print(a)
for i in range(0,10):
    print(fib(i))    