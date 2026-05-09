a = input() # takes string as input

l = list(a) # converts the string into list
print(l)

l.reverse() # reverses the list
print(l)

b = "".join(l) # converts the list into string
print(b)

if a == b:
    print("The string is palindrome")
else:
    print("The string is not palindrome") 
