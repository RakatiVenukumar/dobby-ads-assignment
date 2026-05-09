#password generator 

import random
 
print('WELCOME TO PASSWORD GENERATOR')
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
         'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

password = []
n_alphabets = int(input('enter the number of alphabtes u want: '))

for i in range(1,n_alphabets+1):
    a = random.choice(alphabets)
    password += a
print(password)

numbers = ['0','1','2','3','4','5','6','7','8','9']
n_numbers = int(input("enter the number of numbers u want: "))
for i in range(1,n_numbers+1):
    b = random.choice(numbers)
    password += b
print(password)

symbols = ['!','@','#','$','%','^','&','*','(',')','_']
n_symbols = int(input("enter the number of symbols u want: "))
for i in range(1,n_symbols+1):
    c = random.choice(symbols)
    password += c
print(password)

random.shuffle(password)
print(password)

password1 = ''
for i in password:
    password1 += i
print(password1)
