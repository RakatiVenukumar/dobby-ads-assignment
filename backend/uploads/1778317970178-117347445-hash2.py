a = [2,7,11,15]
def two_sum(a,target):
    b = {}
    target = 9
    curr_sum = 0
    for i in range(len(a)):
        curr_sum += a[i]
        complement = curr_sum - target
        
        if complement in b:
            return [b[complement]+1,i]
        else:
            b[curr_sum] = i
   
            
def contains_duplicate(arr):
    a = set()
    for i in range(len(arr)):
        if arr[i] in a:
            return True
        else:
            a.add(arr[i])
    return False


def Valid_anagram(a,b):
    dict1 = {}
    for i in a:
        dict1[i] = dict1.get(i,0)+1

    for i in b:
        if i in dict1:
            dict1[i] -= 1
        else:
            return False
        
    for i in dict1:
        if dict1[i] == 0:
            return True


def Intersection_of_arrays(arr1,arr2):
    list1 = []
    arr1 = set(arr1)
    for i in set(arr2):
        if i in arr1:
            list1.append(i)
    return list1


a = 'aA'
b = 'aAAZZZZZ'
def jewels_and_stones(a,b):
    dict1 = {}
    count = 0
    for i in a:
        dict1[i] = dict1.get(i,0)+1

    for i in b:
        if i in dict1:
            count += 1
    return count
print(jewels_and_stones(a,b))

a = 'leetcode'
def first_non_repeating_char(a):
    b = {}
    for i in a:
        b[i] = b.get(i,0)+1
    for i,char in enumerate(a):
        if b[char] == 1:
            return i
    return -1


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagrams(strs):
    dict1 = {}
    for i in strs:
        sorted_string = "".join(sorted(i))
        if sorted_string not in dict1:
            dict1[sorted_string] = [i]
        else:
            dict1[sorted_string].append(i)
    return list(dict1.values())

a = 'abcd'
b = 'abcde'
def find_difference(a,b):
    a = set(a)
    for i in set(b):
        if i in a:
            continue
        else:
            return i
    return ""

n = 28
def happy_num(n):
    a = set()
    while n != 1 and n not in a:
        a.add(n)
        sum = 0
        for i in str(n):
            sum += int(i) ** 2
        n = sum
    if n == 1:
        return True
    return False 


a = [100,1,200,2,3,4]
# a.sort()
# count = 0
# i = a[0]
# while a:
#     if i in a:
#         count += 1
#         i += 1
#     else:
#         break
# print(count)

def longest_consecutive(a):
    b = set(a)
    max_len = 0
    for i in a:
        if i-1 not in b:
            curr_num = i
            curr_streak = 1
            while curr_num+1 in b:
                curr_num += 1
                curr_streak += 1
        max_len = max(max_len,curr_streak)
    return max_len


from collections import Counter
s = "cbaebabacd"
p = "abc"
def find_anagrams(s,p):
    result = []
    p_count = Counter(p)
    s_count = Counter()
    p_len = len(p)

    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= p_len:
            if s_count[s[i-p_len]] == 1:
                del s_count[s[i-p_len]]
            else:
                s_count[s[i-p_len]] -= 1
        
        if s_count == p_count:
            result.append(i - p_len + 1)
    return result
