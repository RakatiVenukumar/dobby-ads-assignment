# a = input().split(" ")
# a = list(map(int,a))
# print(a)
# first = second = third = 0
# if len(a) < 3:
#     print("Wrong input")
# for i in range(int(len(a))):
#     if a[i] > first:
#         third = second
#         second = first
#         first = a[i]
#     elif a[i] > second:
#         third = second
#         second = a[i]
#     else:
#         third = a[i]
# print(first,second,third)
    

a = input().split(" ")
a = list(map(int,a))
print(a)
first = second = 0
if len(a) < 2:
    print("Wrong input")
for i in range(int(len(a))):
    if a[i] > first:
        second = first
        first = a[i]
    elif a[i] > second:
        second = a[i]
print(second)