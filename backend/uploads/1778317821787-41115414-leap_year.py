# leap year

n = int(input("enter the year: "))
if(n%400==0 or n%100!=0 and n%4==0):
    print("leap year")
else:
    print("not leap year")