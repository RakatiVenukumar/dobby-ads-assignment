a = [4,0,0,3,0,2,1,0]
l = []
a.sort()

for i in range(len(a)):
    if a[i] != 0:
        l.append(a[i])
print(l)

for i in range(len(a)):
    if a[i] == 0:
        l.append(a[i])
print(l)
