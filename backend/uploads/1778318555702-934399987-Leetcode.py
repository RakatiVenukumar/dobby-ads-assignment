def minimumOperations(nums):
    n = len(nums)
    for i in range(0, n+1, 3):
        my_list = nums[i:]
        freq = {}
        for var in my_list:
            freq[var] = freq.get(var, 0) +1
        
        is_distinct = True
        for count in freq:
            if freq[count] > 1:
                is_distinct = False
                break
        if is_distinct:
            return i // 3
    return (n+2) // 3

def removeDuplicates(nums):
        if not nums:
            return 0
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k

def max_profit(prices):
    min_price = 1000000
    max_profit = 0
    for i in prices:
        if i < min_price:
            min_price = i
        else:
            max_profit = max(max_profit, i - min_price)
    return max_profit

def move_zeroes(a):
    n = len(a)
    i,j = 0,0
    while i < n:
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
        i += 1
    return a

def numberOfPowerfulInt(start: int, finish: int, limit: int, s: str) -> int:
    count = 0
    if int(s) > finish:
        return 0
    for i in range(start, finish + 1):
        if i < int(s):
            continue
        if int(str(i)[0]) > limit:
            continue
        # is_valid = False
        # if str(i).endswith(s):
        #     is_valid = True
        #     count += 1
        rev_i = str(i)[::-1]
        z = rev_i[:len(s)]
        if z[::-1] == s:
            count += 1
    return count

def reverse(a,l,r):
    while l < r:
        a[l],a[r] = a[r],a[l]
        l += 1
        r -= 1   
def rotate_array(a, k):
    n = len(a)
    reverse(a,0,n-1)
    reverse(a, 0, k-1)
    reverse(a, k, n-1) 
    return a

def countSymmetricIntegers(low: int, high: int) -> int:
    count = 0
    for i in range(low, high + 1):
        i = str(i)
        n = len(i)
        nums1, nums2 = i[:n//2], i[n//2:]
        sum1 , sum2 = 0,0
        for i in nums1:
            sum1 += int(i)
        for j in nums2:
            sum2 += int(j)
        if sum1 == sum2:
            count+= 1
    return count

def plusOne(digits):
    n = len(digits)
    for i in range(n-1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + [0]*n

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
def countGoodTriplets(arr, a ,b, c):
    count = 0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(i+2, len(arr)):
                if i < j < k:
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
    return count

def countPairs(nums, k):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count

def findMedianSortedArray(nums1, nums2):
    nums3 = []
    l, r = 0, 0
    while l < len(nums1) and r < len(nums2):
        if nums1[l] < nums2[r]:
            nums3.append(nums1[l])
            l += 1
        else:
            nums3.append(nums2[r])
            r += 1
            
    while l < len(nums1):
        nums3.append(nums1[l])
        l += 1

    while r < len(nums2):
        nums3.append(nums2[r])
        r +=1
    print(nums3)
    n = len(nums3)
    low = 0
    high = n - 1
    mid = (low + high)//2
    if n%2 != 0:
        return nums3[mid]
    else:
        return (nums3[mid] + nums3[mid+1])/2
    
def countLargestGroup(n):
    dict1 = {}
    count = 0
    for i in range(1, n+1):
        i_str = str(i)
        digit_sum = 0
        for j in i_str:
            digit_sum += int(j)
        dict1[digit_sum] = dict1.get(digit_sum, 0)+1
    maxx = max(dict1.values())
    for v in dict1.values():
        if v == maxx:
            count += 1
    return count

def countSubarrays(nums, k):
    count = 0
    start = 0
    curr_sum = 0
    for end in range(len(nums)):
        curr_sum += nums[end]
        length = end - start +1
        while start <= end and (curr_sum * (length)) >= k:
            curr_sum -= nums[start]
            start += 1
            length -= 1
        count += length 
    return count

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

def noOfEvenDigits(nums):
    count = 0
    for i in range(len(nums)):
        i_str = str(nums[i])
        if len(i_str) % 2 == 0:
            count += 1
    print(count)
    
def numEquivDominoPairs(dominoes):
    dict1 = {}
    count = 0
    for i in range(len(dominoes)):
        key = tuple(sorted(dominoes[i]))
        if key not in dict1:
            dict1[key] = 1
        else:
            dict1[key] += 1
    for v in dict1.values():
        if v > 1:
            count += v*(v-1) // 2
    return count

def differenceOfSums(n, m):
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1):
        if i%m == 0:
            sum2 += i
        else:
            sum1 += i
    return (sum1-sum2)

def minSum(nums1, nums2):
    z1 = 0
    for i in nums1:
        if i ==0:
            z1 += 1
    z2 = 0
    for j in nums2:
        if j == 0:
            z2 += 1
    s1 = z1 + sum(nums1)
    s2 = z2 + sum(nums2)
    if (s1>s2 and z2 == 0) or (s1<s2 and z1 == 0):
        return -1
    return max(s1,s2)

def threeConsecutiveOdds(arr):
    for i in range(len(arr)-2):
        if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2]%2 == 1:
            return True       
    return False

def findEvenNumbers(digits):
    freq = {}
    for i in digits:
        freq[i] = freq.get(i, 0) + 1
    ans=[]
    for x in range(100, 1000, 2):
        x0, x1, x2=x%10, (x//10)%10, x//100
        if freq.get(x0,0) > 0 and freq.get(x1,0)>0 and freq.get(x2,0)>0:
            freq[x0]-=1
            freq[x1]-=1
            freq[x2]-=1
            if freq[x0]>=0 and freq[x1]>=0 and freq[x2]>=0:
                ans.append(x)
            freq[x0]+=1
            freq[x1]+=1
            freq[x2]+=1
    return ans

def getLongestSubsequence(words, groups):
    res = []
    order = -1
    for i in range(len(groups)):
        if groups[i] != order:
            order = groups[i]
            res.append(words[i])
    return res

def maxDifference(s):
    dict1 = {}
    for i in s:
        dict1[i] = dict1.get(i, 0) + 1
    max_even = len(s)
    max_odd = 0
    for v in dict1.values():
        if v % 2 == 0:
            if v < max_even:
                max_even = v
        else:
            if v > max_odd:
                max_odd = v
    return max_odd - max_even

def partitionArray(nums, k):
    nums.sort()
    res = 1
    min_val = nums[0]
    for i in nums[1:]:
        if i-min_val > k:
            res += 1
            min_val = i
    return res

def maxDistance(s, k):
    distance = []
    x , y = 0, 0
    for i in s:
        if i == "N":
            x += 1
        elif i == 'S':
            x -= 1
        elif i == "W":
            y -= 1
        elif i == "E":
            y += 1
        distance.append(abs(x) + abs(y))
    max_dist = distance[1]
    prev_dist = distance[0]
    ans = 0
    for i in range(1, len(distance)):
        if distance[i] < prev_dist and k > 0:
            ans += 2
            k -= 1
        prev_dist = distance[i]
        distance[i] += ans
        max_dist = max(max_dist, distance[i])
    return max_dist

def minimumDeletions(word, k):
    dict1 = {}
    for i in word:
        dict1[i] = dict1.get(i, 0) + 1
    freq = sorted(dict1.values())
    min_deletions = float('inf')
    n = len(freq)
    for i in range(n):
        base = freq[i]
        deletions = 0
        for j in range(i):
            deletions += freq[j]
        for j in range(i, n):
            if freq[j] > base + k:
                deletions += freq[j] - (base+k)
        min_deletions = min(min_deletions, deletions)
    return min_deletions

def divideString(s, k, fill):
    res = []
    for i in range(0, len(s), k):
        sub_str = s[i:i+k]
        if len(sub_str) < k:
            sub_str += fill * (k-len(sub_str))
        res.append(sub_str)
    return res

def findKDistantIndices(nums, key, k):
    marked = []
    for i in range(len(nums)):
        if nums[i] == key:
            marked.append(i)
    res = []
    for j in range(len(nums)):
        for idx in marked:
            if abs(j-idx) <= k:
                res.append(j)
                break
    return sorted(res)

def relativeSort(arr1, arr2):
    dict1 = {}
    for i in arr1:
        dict1[i] = dict1.get(i, 0) + 1
        
    res = []
    for i in arr2:
        if i in dict1:
            res.extend([i] * dict1[i])
            del dict1[i]
            
    for i in sorted(dict1.keys()):
        res.extend([i] * dict1[i])
    return res

nums = [2,1,3,1,1,1,7,1,2,1]
def minValIndex(nums):
    n = len(nums)
    freq = {}
    for i in nums:
        freq[i] = freq.get(i, 0) + 1
    dom, cnt = 0, 0
    for num, val in freq.items():
        if val > n//2:
            dom = num
            cnt = val
            break
    left_count = 0
    for i in range(n-1):
        if nums[i] == dom:
            left_count += 1
        left_size = i+1
        right_size = n - left_size
        right_count = cnt - left_count
        
        if left_count > left_size//2 and right_count > right_size//2:
            return i
    return -1

nums = [2,-1,1,2]
k = 2
def subArrayEqualToK(nums, k):
    curr_sum = 0
    dict1 = {0:1}
    count = 0
    for num in nums:
        curr_sum += num
        if curr_sum - k in dict1:
            count += dict1[curr_sum - k]
        if curr_sum in dict1:
            dict1[curr_sum] += 1
        else:
            dict1[curr_sum] = 1
    return count

nums = [4,5,0,-2,-3,1]
k = 5
def subArrayDivisibleByK(nums, k):
    curr_sum = 0
    dict1 = {0:1}
    count = 0
    for num in nums:
        curr_sum += num
        mod = curr_sum % k
        if mod < 0:
            mod = mod + k
        if mod in dict1:
            count += dict1[mod]
            dict1[mod] += 1
        else:
            dict1[mod] = 1
    return count

arr = [2,2,3,3,3]
def findLucky(arr):
    d = {}
    max_count = -1
    for i in arr:
        d[i] = d.get(i, 0) + 1
    for key, val in d.items():
        if key == val:
            max_count = max(max_count, key)
    return max_count

s = "aaabc"
def subsequencePalindrome(s):
    res = 0
    uniq = set(s)
    for c in uniq:
        start = -1
        end = -1
        
        for i in range(len(s)):
            if s[i] == c:
                if start == -1:
                    start = i
                end = i
            
            if start != -1 and end != -1 and start < end:
                middle_chars = set()
                for i in range(start+1, end):
                    middle_chars.add(s[i])
                res += len(middle_chars)
    return res

arr = [1,3,5]
def oddSubArrays(arr):
    even , odd = 1, 0
    prefix_sum = 0
    res = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum % 2 == 0:
            res += odd
            even += 1
        else:
            res += even
            odd += 1
    return res

rectangles = [[4,8],[3,6],[10,20],[15,30]]
def interChangeableRectangles(recangles):
    count = 0
    dict1 = {}
    for width, height in rectangles:
        ratio = height / width
        if ratio in dict1:
            count += dict1[ratio]
            dict1[ratio] += 1
        else:
            dict1[ratio] = 1
        return count

s = "cbaebabacd"
p = "abc"
def findAnagrams(s, t):
    res = []
    dict1 = {}
    for i in p:
        dict1[i] = dict1.get(i, 0) + 1
        
    start = 0
    end = len(p)
    while end <= len(s):
        dict1_copy = dict1.copy()
        curr_subarray = s[start:end]
        
        is_valid = True
        for i in curr_subarray:
            if i not in dict1_copy:
                is_valid = False
                break
            dict1_copy[i] -= 1
            if dict1_copy[i] < 0:
                is_valid = False
                break
            
        if is_valid and all(val == 0 for val in dict1_copy.values()):
            res.append(start)
        
        start += 1
        end += 1
    return res

nums = [3,5,30,34,9]
def largestNumber(nums):
    res = ''
    arr = []
    for i in nums:
        i_str = str(i)
        arr.append(i_str)
        
    keys = []
    for s in arr:
        keys.append((10*s, s))
        
    keys.sort(reverse = True)
    for _, i in keys:
        res += "".join(i)
    return res

nums = [1,3,0,0,2,0,0,3]
def zeroSubArrays(nums):
    dict1 = {0:1}
    prefix_sum = 0
    count = 0
    for num in nums:
        prefix_sum += num
        if prefix_sum in dict1:
            count += dict1[prefix_sum]
            dict1[prefix_sum] += 1
        else:
            dict1[prefix_sum] = 1
    return count

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
def wordSubsets(words1, words2):
    dict1 = {}
    for word in words2:
        word_count = {}
        for ch in word:
            word_count[ch] = word_count.get(ch, 0) + 1
        for ch, count in word_count.items():
            dict1[ch] = max(dict1.get(ch, 0), count) 
    res = []
    for word in words1:
        word_count = {}
        for c in word:
            word_count[c] = word_count.get(c, 0) + 1
        is_valid = True
        for ch, count in dict1.items():
            if dict1[ch] > word_count.get(ch, 0):
                is_valid = False
                break
        if is_valid:
            res.append(word)
    return res

nums = [2,3,5]
def getSumAbsDiff(nums):
    n = len(nums)
    result = [0] * n
    prefix = [0] * n
    suffix = [0] * n
    prefix[0] = nums[0]
    suffix[n-1] = nums[n-1]
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]
        suffix[n-i-1] = suffix[n-i] + nums[n-i-1]
    for i in range(n):
        abs_diff = ((nums[i]*i - prefix[i]) + suffix[i] - (nums[i] * (n-i-1)))
        result[i] = abs_diff
    return result

word = "234Adas@"
def isValid(word):
    if len(word) < 3:
        return False
    vowels = 0
    consonents = 0
    vowel_set = "aeiouAEIOU"
    for c in word:
        if c.isalpha():
            if c in vowel_set:
                vowels += 1
            else:
                consonents += 1
        elif not c.isdigit():
            return False
    return vowels >= 1 and consonents >= 1

s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
def addSpaces(s, spaces):
    res = ''
    l, r = 0, 0
    while l < len(s) and r < len(spaces):
        if l == spaces[r]:
            res += " "
            r += 1
        else:
            res += s[l]
            l += 1
    res += s[l:]
    return res

# points = [[6,2],[4,4],[2,6]]
# n = len(points)
# res = 0
# sorted_points = sorted(points, key = lambda x:(x[0],-x[1]))
# for i in range(n):
#     top = sorted_points[i][1]
#     bottom = -1
#     for j in range(i+1, n):
#         y = sorted_points[j][1]
#         if bottom <= y <= top:
#             res += 1
#             bottom = y
#             if bottom == top:
#                 break
# print(res)

