a = [9,5,10,2,6,1,0] #0 1 2 5 6 9 10
b = len(a) 
  
for i in range(b): 
    for j in range (0,b-1-i):
        if (a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
        else:
            j += 1
print(a)
