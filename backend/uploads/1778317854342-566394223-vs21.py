# full pyramid
n = 3
for i in range(3):
    print(" " * (3-i-1), end="")
    for j in range (0,(2*i+1)):
        print("*", end= "")
    print("\r") # ending line after each row 
        