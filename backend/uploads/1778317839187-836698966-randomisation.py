import random

a = input("enter the names of friends seperated by comma :")
b = a.split(",")

c = len(b)
d = random.randint(0,c-1)
print(f"{b[d]} will pay the bill")