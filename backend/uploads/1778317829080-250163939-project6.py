# simple calculator 

import os

def calculator(a,b):
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        return a / b
    

x = int(input("Enter first number: "))

end = False
while not end:    
    operation = input("choose operations '+' or '-' or '*' or '/' \n: ")
    y = int(input("Enter next number: "))
    output = calculator(x,y)
    print(f'{x} {operation} {y} = {output}')
    d = input("Enter 'c' to continue with current calculation, 'n' to start new calculation and 'e' to exit:\n ").lower()
    if d == 'c':
        x = output
    elif d == 'n':
        os.system('cls')
        x = int(input("Enter first number: "))
    elif d == 'e':
        end = True
        print('DONE!!')


