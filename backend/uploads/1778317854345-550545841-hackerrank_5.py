# runner up score
a = input("enter the numbers: ")
b =a.split(',')

c = " ".join(map(str,b))
print(c)

for i in range(0,len(b)):
    b[i] = int(b[i])
print(b)

d = set(b)
e = list(d)
print(e)
print(e[-2])
    
    