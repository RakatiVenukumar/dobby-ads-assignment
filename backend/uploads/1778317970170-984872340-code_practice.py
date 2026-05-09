# a = [1,8,3,4,5,0,3,0]
# x = int(input())
# b = []
# c = []
# for i in range(len(a)):
#     if a[i] >= x:
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print(b)
# print(c)
# a = c+b
# print(a)



# a = [1,1,2,2,2,3]
# count_dict = {}
# for i in a:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
# print(count_dict)



# for i in range(8):
#     for j in range(3): 
#         if i % 4 ==  3 and j == 1:
#            print("* ", end = '')     
#         if (i % 4 == j):
#             print("* ", end = '')
#         else:
#             print(" ",end = '')
#     print()



def even_odd_positions(arr):
    i = 0
    while i < len(arr):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        i += 2   
    return arr


def max_min(a):
    b = []
    while a:
        b.append(max(a))
        a.remove(max(a))
        if a is not None:
            b.append(min(a))
            a.remove(min(a))
    return b



def EvenOdd(a):
    b = []
    c = []
    for i in range(len(a)):
        if a[i]%2 == 0:
            b.append(a[i])
        else:
            c.append(a[i])
    return b+c
 
 
 
# a = [1,2,3,4,5,6,7]
# k = 2
# a[0:k] = a[0:k][::-1]
# a[k:a[-1]+1] = a[k:a[-1]+1][::-1]
# a.reverse()
# print(a)



def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end += 1    
def left_rotate(arr,d):
    n = len(arr)
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    

def No_of_traingles(arr,n):
    count = 0 
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (arr[i] + arr[j] > arr[k] and 
                    arr[j] + arr[k] > arr[i] and
                    arr[k] + arr[i] > arr[j]):    
                    count += 1
    return count


def unique_elements(arr):
    unique = []
    for i in range(len(arr)):
        if arr[i] not in unique:
            unique.append(arr[i])
    return unique


# def single_element(arr):
#     for i in arr:
#         if arr.count(i) == 1:
#             return arr[i]
#     return None
# arr = [1,1,2,2,3,4,4]
# result = single_element(arr)
# print(result)


def single_element(arr):
    dict1 = {}
    for num in arr:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    
    for num,count in dict1.items():  #[(1, 2), (2, 2), (3, 1), (4, 2)]
        if count == 1:
            return num
                  

def leader(arr,n):
    for i in range(n):
        k = False
        for j in range(i + 1, n):
            if(arr[i] <= arr[j]):
                k = True
                break
        else: 
            print(arr[i], end=' ')
                         

# a = [1,2,3,4,5,6,7,8,9]
def sub_array(arr,target_sum):
    current_sum = 0
    start = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        while current_sum > target_sum and start <= i:
            current_sum -= arr[start]
            start += 1
        if current_sum == target_sum:
            print(f'{start} {i}')
            break
    return None


# count = 1
# for i in range(4): # 0 1 2 3
#     for j in range(i+1):
#         # print(count,end= ' ')
#         # count += 1
#         print(i*(i+1)//2+j+1,end = ' ')
#     print()


# a = input()
# a = list(map(int,a))
# sum1 = 0
# sum2 = 0
# for i in a:
#     if i%2 == 0:
#         sum1 += i
#     else:
#         sum2 += i
# print(sum1)


# n = int(input())
# list1 = []
# for _ in range(n):
#     element = int(input("Enter an element: "))
#     list1.append(element)
# odd_sum = 0
# even_sum = 0
# for element in list1:
#     if element % 2 == 0:
#         even_sum += element
#     else:
#         odd_sum += element
# print(list1)
# print(odd_sum)
# print(even_sum)


def rearrange(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(n):
            if i == arr[j]:
                arr[j],arr[i] = arr[i],arr[j]
    for i in range(n):
        if arr[i] != i:
            arr[i] = -1
    for i in range(n):
        print(arr[i],end = " ")
# arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1] 
# rearrange(arr)


def two_sum(arr,target):
    start = 0
    end = len(arr)-1
    sum = 0
    while start < end:
        sum = arr[start]+arr[end]
        if sum == target:
            return [start,end]
            break
        elif sum > target:
            end -= 1
        else:
            start += 1  
# a = [2,5,7,11,15]
# print(two_sum(a,9))


def is_palindrome(str):
    n = len(str)
    start = 0
    end = n-1
    for i in range(n//2):
        if str[start] != str[end]:
            return False
        start += 1
        end -= 1
    return True
str1 = 'TOO hot To Hoot'
str1 = str1.lower()
# print(str1)
a = ''
for i in str1:
    if i.isalpha():
        a += i
# print(a)


def move_zeroes(arr):
    n = len(arr)
    i,j = 0,0
    while i < n:
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
        i += 1
    print(arr)
# arr = [1,1,3,1,0,0,1,32,12,0]
# move_zeroes(arr)


# a = ['h', 'e', 'l', 'l', 'o'] 
# l = 0
# n = len(a)
# r = n-1
# while l < r:
#     a[l],a[r] = a[r],a[l]
#     l += 1
#     r-=1
# print(a)


def remove_element(arr,k):
    for i in range(len(arr)):
        if arr[i] == k:
            arr.pop(i)
            arr.append('_')
    print(arr)    
# a = [2,3,2,2]
# remove_element(a,2)


def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        area = min_height * width
        
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


def replace_duplicates(arr):
    b = []
    for i in arr:
        if i not in b:
            b.append(i)
            
    b += "_" * (len(a)-len(b))
    return b

a = [1,2,2,1,3,4]
print(replace_duplicates(a))


def Three_sum(arr):
    arr.sort()
    result = []
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        l = i+1
        r = len(arr) - 1
        
        while l < r:
            current_sum = arr[i] + arr[l] + arr[r]
            
            if current_sum == 0:
                result.append([arr[i],arr[l],arr[r]])
                l += 1
                r -= 1
                
                while l < r and a[l] == [l-1]:
                    l +=1 
                while l < r and a[r] == a[r-1]:
                    r -= 1
            
            elif current_sum < 0:
                l += 1
            else:
                r -= 1
    return result

nums = [-1, 0, 1, 2, -1, -4]


def Intersection_arrays(a,b):
    a.sort()
    b.sort()
    result = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result

a = [1,2,2,1]
b = [2,2]
# res = Intersection_arrays(a,b)
# print(res)



def Minimum_subarray(arr,target_sum):
    min_length = 99999
    start = 0
    current_sum = 0
    
    for end in range(len(arr)):
        current_sum += arr[end]
        
        while current_sum >= target_sum:
            min_length = min(min_length,end-start+1)
            current_sum -= arr[start]
            start += 1
            
    return min_length

arr = [2, 3, 1, 2, 4, 3]
target_sum = 7
#print(Minimum_subarray(arr, target_sum))



def Longest_substring(str):
    max_length = 0
    i = 0
    s = ''
    for j in range(len(str)):
        while str[j] in s:
            s = s[1:]
            i += 1
        s += str[j]
        max_length = max(max_length,len(s))    # max(max_length,j-i+1)
    return max_length
str = "bvbndhvedncurfbviu"


def min_window(s,t):
    # edge cases
    if len(t) > len(s): # if length of target string is greater than given string
        return ""
    for char in t:
        if s.count(char) < t.count(char):  # if target string is not found in given string
            return ""
        
    min_length = 99999    # Initialization   
    min_window = ''
    i = 0
    
    for j in range(len(s)):   # Sliding  window approach 
        while True:
            window = s[i:j+1]  # current window substring
            contains_all = True
            for char in t:
                if window.count(char) < t.count(char):
                    contains_all =  False
                    break
            
            if contains_all:  # checks if current window is smaller than the previous window
                if (j-i+1) < min_length:
                    min_length = j-i+1
                    min_window = s[i:j+1]
                i += 1 # shrink the window
            else:
                break
    return min_window             

s = 'adobecodebanc'
t = 'abc'    



def sliding_window_max(nums,k):
    start = 0
    max_window = []
    for end in range(len(nums)-k+1):
        current_window = nums[start:start+k]
        max_window.append(max(current_window))
        start += 1
    return max_window

nums = [1,3,-1,-3,5,3,6,7]



def max_subarray(arr,k):
    i = 0
    current_sum = 0
    max_length = 0
    max_window = []
    for j in range(len(arr)):
        current_sum += arr[j] 
        
        if current_sum > k:
            max_length = max(max_length,j-i+1)
            max_window = arr[i:j+1]
            current_sum -= arr[i]
            i += 1
            
    return max_window


def SubArray_sum(arr,target_sum):
    start = 0
    current_sum = 0
    for end in range(len(arr)):
        current_sum += arr[end]
    
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1
        
        if current_sum == target_sum:
            return [start,end]

def Total_amount(denominations_count):
    denominations = [20,40,100,200,500,1000]
    Total_amount = 0
    for i in range(len(denominations)):
        Total_amount += denominations_count[i]*denominations[i]
    Total_amount_dollar = Total_amount / 100
    return Total_amount_dollar


def case_changer(a):
    words = a.split(" ")
    result = []
    for word in words:
        if word.isalpha():
            if word[0].isupper():
                result.append(word.upper())
            else:
                result.append(word.lower())
        else:
            result.append(word)
    return (" ".join(result))
