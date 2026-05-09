a = [1,2,3,4,5,6,7,8,9]
k = 9
def subarray_sum(a,k):
    start = 0
    count = 0
    sum = 0
    for end in range(len(a)):
        sum += a[end]
            
        while sum > k and start <= end:
            sum -= a[start]
            start += 1
                
        if sum == k:
            count += 1  
    return count      

a = 14
def LargestGroup(n):
    d = {}
    count = 0
    for i in range(1, n+1):
        i_str = str(i)
        digit_sum = 0
        for digit in i_str:
            digit_sum += int(digit)
        d[digit_sum] = d.get(digit_sum, 0) + 1
    maxx = max(d.values())
    for k, v in d.items():
        if v == maxx:
            count += 1
    return count

nums = [2,1,4,3,5]
k = 10
def countSubarrays(nums, k):
    count = 0
    start = 0
    curr_sum = 0
    for end in range(len(nums)):
        curr_sum += nums[end]
        while start <= end and (curr_sum * (end-start+1)) >= k:
            curr_sum -= nums[start]
            start += 1
        count += (end-start+1)
    return count

nums = [7,8,-3]
def CountLessThank(nums):
    i,j = 0, 2
    count = 0
    while j <= len(nums)-1:
        mid = (i+j)//2
        if (nums[i]+nums[j]) * 2 == nums[mid]:
            count += 1
        i += 1
        j += 1
    return count

pattern = "abba"
s = "dog cat cat fish"
def wordPattern(pattern, s):
    s = s.split(" ")
    if len(pattern) != len(s):
        return False
    d1 = {}
    d2 = {}
    for i in range(len(pattern)):
        c1 = pattern[i]
        c2 = s[i]

        if c1 in d1:
            if d1[c1] != c2:
                return False
        else:
            d1[c1] = c2
        
        if c2 in d2:
            if d2[c2] != c1:
                return False
        else:
            d2[c2] = c1
    return True

