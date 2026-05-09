# def fact(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(4))

n = int(input("Enter the number: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)