a = [1,0,1,0,1,1,1,0,1,1,0,0]
b = []
for i in range(len(a)):
    if a[i] == 0:
        b.append(a[i])
        
for i in range(len(a)):
    if a[i] == 1:
        b.append(a[i])
        
print(b)
