# Reversing a string

# a = 'hello'   # method 2
# a = list(a)
# a.reverse()
# a = ''.join(a)
# print(a)
# print(type(a))

#print(a[::-1])    #method 2



# factorial of a number

# def fact(n):      # method 1
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(6))

#n = int(input("Enter the number: "))   #method 2
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)


#palindrome

# a = input()
# b = a[::-1]
# if a == b:
#     print("palindrome")
# else:
#     print("not palindrome")


num = 1333
original_num = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num//10
    
if original_num == rev: 
    print("palindrome")
else:
    print("not palindrome")
