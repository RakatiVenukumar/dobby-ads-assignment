# a = input()
# width = int(input())
# for i in range(0, len(a), width):
#     print(a[i:i+width])

# def wrap(str,width):
#     list1 = []
#     for i in range(0,len(str),width):
#         list1.append(str[i:i+width])
#     return "\n".join(list1)
    
# a = wrap('bhuahahahahahahaha',3)
# print(a)

a = [-1,2,3,-5,-10,1]
closest_num = a[0]
for i in a:
    if abs(i) <= abs(closest_num) and i > closest_num:
        closest_num = i
print(closest_num)
        