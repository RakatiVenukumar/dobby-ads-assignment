# largest of four numbers
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))
d = int(input("enter the fourth number: "))

if( a>b and a>c and a>d):
    print("a is the largest number")

elif(b>a and b>c and b>d):
    print("b is the largest number")

elif(c>a and c>b and c>d):
    print("c is the largest number")

else:
    print("d nis the largest number")        
 

