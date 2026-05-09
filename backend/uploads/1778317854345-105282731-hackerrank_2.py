a='a Blue MOON'
a=a.split()
c=''
for i in range(len(a)):
    list1=[]
    list1.append(a[i])
    b=[*list1[0]]
    c+=b[0]
    if len(b)==1:
        c+='!'
        continue
    elif i==len(a)-1:
        for i in range(len(b)-1):
            if b[i]>b[i+1]:
                c+=b[i+1].lower()
            elif b[i]<b[i+1]:
                c+=b[i+1].upper()
            else:
                c+=b[i+1]
    else: 
        for i in range(len(b)-1):
            if b[i]>b[i+1]:
                c+=b[i+1].lower()
            elif b[i]<b[i+1]:
                c+=b[i+1].upper()
            else:
                c+=b[i+1]
            if i==len(b)-2:
                c+='!'
    
print(c)
    