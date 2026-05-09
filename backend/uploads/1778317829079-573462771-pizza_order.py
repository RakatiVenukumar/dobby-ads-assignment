# ordering a pizza 

a = input("what pizza do you prefer (S/M/L/N)? :")   # s = small, m = medium, l = large, n = nothing

if (a == 'S'):
    print("the prize of small pizza ia 100")
    bill = 100
elif ( a == 'M'):
    print("the prize of medium pizza is 200")
    bill = 200
elif (a == 'L'):
    print("the prize of large pizza is 300")
    bill = 300
else:
    print("i am not willing to have a pizza right now")
    bill = 0


b = input("do you wanna have pepperoni in the pizza (S/M/L/N)?")

if ( b == 'S'):
    print("extra 30rs for pepperoni for small pizza")
    bill2 = 30
elif (b == 'M' or b == 'L'):
    print("extra 50rs for pepperoni for medium or large pizza")
    bill2 = 50
else:
    print("no need of pepperoni")
    bill2 = 0


c = input("do you prefer extra cheese in the pizza (Y/N)? :")

if ( c == 'Y'):
    print("Additional 20rs for the extra cheese")
    bill3 = 20
else:
    print("no need of extra cheese")
    bill3 = 0
    
    
total_bill = bill + bill2 + bill3
print("the total billing amount is :" , total_bill)
