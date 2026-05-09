#zigzag star pattern

for i in range(8):
    for j in range(3): 
        if i % 4 ==  3 and j == 1:
           print("* ", end = '')     
        if (i % 4 == j):
            print("* ", end = '')
        else:
            print(" ",end = '')
    print()


# n = int(input())
# arr = list(map(int, input().split()))
# print(arr)
# print(type(arr))



