def Common_elements(list1,list2):
    dict1 = {}
    for i in list1:
        dict1[i] = True
    for j in list2:
        if j in dict1:
            return True
    return False


def Find_duplicates(list1):
    dict1 = {}
    duplicates = []
    for i in list1:
        if i not in dict1:
            dict1[i] = True
        else:
            duplicates.append(i)
    return duplicates


def First_non_repeating_character(str):
    dict1 = {}
    for i in str:
        if i not in dict1:
            dict1[i] = 0
        else:
            dict1[i] += 1
    for i in str:
        if dict1[i] == 0:
            return i
    return None


def group_anagrams(strings):
    dict1={}
    for i in strings:
        sorted_string=''.join(sorted(i))
        if sorted_string not in dict1:
            dict1[sorted_string]=[i]
        else:
            dict1[sorted_string].append(i)
    return list(dict1.values())


def Find_pairs(arr1,arr2,target):
    a = set(arr1)
    list1 = []
    for i in arr2:
        if target-i in a:
            list1.append((target-i,i))
    return list1

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
#print(Find_pairs(a,b,7))


def two_sum(arr,target):
    dict1 = {}
    for i in range(len(arr)):
        sum = target - arr[i]
        if sum in dict1:
            return [dict1[sum],i]
        dict1[arr[i]] = i
        

def contains_duplicate(arr):
    a = set()
    for i in arr:
        if i in a:
            return True
        else:
            a.add(i)
    return False


def single_number(arr):
    dict1 = {}
    for i in arr:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in dict1:
        if dict1[i] == 1:
            return i
    return False


def valid_anagram(s,t):
    dict1 = {}
    if len(s) != len(t):
        return False
    
    for char in s:
        dict1[char] = dict1.get(char,0)+1
    
    for char in t:
        if char in dict1:
            dict1[char] -= 1
        else:
            return False
        
    for i  in dict1.values():
        if i == 0:
            return True
        else:
            return False
        
s = 'jam'
t = 'mat'
print(valid_anagram(s, t))

