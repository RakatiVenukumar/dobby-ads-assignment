# multiplication table
num = int(input("enter the number you want multiplication of: "))
for i in range (1,11):
    print(str(num) + " X " + str(i) + "=" + str(num*i))
#print(f"{num}X{i}={num*i}") - use of fstrings for the multiplication cause