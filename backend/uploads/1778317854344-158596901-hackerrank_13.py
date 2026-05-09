# a = input()
# width = int(input())
# for i in range(0, len(a), width):
#     print(a[i:i+width])

def wrap(str,width):
    list1 = []
    for i in range(0,len(str),width):
        list1.append(str[i:i+width])
    return "\n".join(list1)
    
a = wrap('bhuahahahahahahaha',3)
print(a)