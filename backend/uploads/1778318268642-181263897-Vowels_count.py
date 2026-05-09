def prime(x, y):
    nums = []
    for i in range(x, y+1):
        if i < 2:
            continue
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                nums.append(i)
    return nums

a = [1,2,3,4,5]
l = 0
r = len(a)-1
while l < r:
    a[l],a[r] = a[r],a[l]
    l += 1
    r -= 1
print(a)
                    