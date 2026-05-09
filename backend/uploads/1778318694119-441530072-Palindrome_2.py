a = int(input())
b = ''

while a > 0:
    b = b + str(a%10) # converts the number into string and 'add last digit to b'
    a = int(a/10) # removes the last digit 
b = int(b)
print(b)

if a == int(b):
    print('palindrome')
else:
    print('not palindrome')
    
