a = [1,2,3,4,5]
b = []
for i in range(0,len(a)):
    pop_items = a.pop()
    print(pop_items,end = " ")
    b.append(pop_items)
print(b)