# n = 1634
# len = len(str(n))
# sum = 0
# for i in range(0,n):
#     rem = n%10
#     sum = sum + rem**len
#     n = n//10
# print(sum)

arr = [52,66,64,36,45,24,32]
res = 0
for i in range(0,len(arr)-1):
    if arr[i] > arr[i+1]:
        res += arr[i]
print(res+arr[-1])
