list1 = [[12,23,25,22],
         [30,24,6,27],
         [26,2,45,5],
         [13,14,15,16]]
max = 0
for i in range(0,len(list1)):
    for j in range(i+1):
        if list1[i][j] > max:
            max = list1[i][j]
        else:
            max = 0
    print(max)