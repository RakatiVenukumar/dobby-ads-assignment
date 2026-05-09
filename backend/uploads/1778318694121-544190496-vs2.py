# reverse of a number

a = 121
def reverse1(a):
    b = ''
    for i in str(a):
        b = b+ str(a%10)
        a = int(a//10)
    return b


# fibonacci series of a series

def fibonacci(n):
    n1 = 0
    n2 = 1
    print(n1,n2,end = " ")
    for i in range(n):
        next_term = n1 + n2
        n1 = n2
        n2 = next_term
        print(n2,end = " ")


# GCD 
def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
# print(gcd(200,100))

def reverse(string):
    stack1 = []
    stack2 = []
    for char in string:
        stack1.append(char)
       
    for i in range(len(stack1)):
        pop_item = stack1.pop()
        stack2.append(pop_item)
    return stack2
# a = reverse("venu")
# print(a)


# a = list(input().lower())
# b = input().lower()
# list1 = list(a)
# for i in range(len(list1)):
#     if list1[i] == b:
#         if b == 'a':
#             list1[i] = 'z'
#         else:
#             list1[i] = (chr(ord(list1[i])-1))
# result = "".join(list1)
# print(result)
        



def is_lower(str):
    count = 0
    for i in str:
        if i.islower():
            count += 1
            print(i,end = '')
    print(f":{count}")
# is_lower("VenuKumar")



# a = [10,20,30,40,50,60]
# sum = 0
# for i in range(len(a)-1,-1,-1): # 60 50 40 30 20 10
#     if i % 2 != 0:
#         sum += a[i]
# print(sum)


# a = ['h','e','l','l','o']
# l = 0
# r = len(a)-1
# for i in range(len(a)-1,-1,-1):
#     a[l],a[r] = a[r],a[l]
# print(a)


# Permutations of a given string

# from itertools import permutations # in-built library
# a = 'ab'
# b = permutations(a)
# c = ["".join(i) for i in b]
# # print(c)


# count = 1
# for i in range(6):
#     print(" " * i, end = "")
#     for j in range(6-i):
#         if count > 9:
#             count = 0
#         print(count,end = " ")
#         count += 1
#     print()


def Special_num(start,end):
    nums = []
    for i in range(start,end +1):
        is_prime = True
        if i <= 1:
            is_prime = False
        else:
            for j in range(2,i):
                if i % j == 0:
                    is_prime = False
                    break          
        if is_prime:
            nums.append(i)
    return nums


def is_amstrong(start,end):
    nums = []
    for i in range(start,end +1):
        str_num = str(i)
        power = len(str_num)
        total = 0
        for j in str_num:
            total += int(j)**power
        if total == i:
            nums.append(i)
    return nums

def is_perfect(start,end):
    nums = []
    for i in range(start,end +1):
        sum = 0
        for j in range(1,i):
            if i % j == 0:
                sum += j
        if sum == i:
            nums.append(i)
    return nums


def First_non_repeating_character(a):
    i = 0
    if i >= len(a):
        return None
    while i < len(a):
        if i < len(a)-1 and a[i] == a[i+1]:
            while i < len(a)-1 and a[i] == a[i+1]:
                i += 1
        else:
            return a[i]
            break      
        i += 1
# string = 'llleeetttcccoddde'
# print(First_non_repeating_character(string))



# def SubArray_sum(arr,target):
#     start = 0
#     sum = 0
#     for end in range(len(arr)):
#         sum += arr[end]
#         while sum > target and start <= end:
#             sum -= arr[start]
#             start += 1
#         if sum == target:
#             return [start,end]
#     return None
        

def Subarray_sum(a,k):
    sum = {0:1}
    current_sum = 0
    count = 0
    for num in a:
        current_sum += num
        
        if current_sum-k in sum:
            count += sum[current_sum-k]
            
        if current_sum in sum:
                sum[current_sum] += 1
        else:
            sum[current_sum] = 1
    return count


def Non_repeating_num(a):
    b = {}
    for i in a:
        b[i] = b.get(i,0)+1
    for i in b:
        if b[i] == 1:
            return i
    return -1    

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
a = [3,2,4,5,1]

def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    mid = n // 2
    L = arr[:mid]
    R = arr[mid:]
    left = merge_sort(L)
    right = merge_sort(R)
    l, r = 0, 0
    i = 0
    sorted_array = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_array.append(left[l])
            l += 1
        else:
            sorted_array.append(right[r])
            r += 1
        i += 1
        
    while l < len(left):
        sorted_array.append(left[l])
        l += 1
        i += 1
    
    while r < len(right):
        sorted_array.append(right[r])
        r += 1
        i += 1
    return sorted_array

n = "['3','0','1']"
n = n.strip("[]")
print(n)
n_list = n.replace("'", "").replace(",", "")
print(n_list)
nums = list(map(int, n_list))
print(nums)
length = len(nums)
sum = 0
total = length * (length + 1)//2
for i in nums:
    sum += i
missing_num = total - sum
print(missing_num)

# n = "['3','0','1','2']"
# n = n.strip("[]")
# n_list = n.replace("'", "").replace(",", "")
# nums = list(map(int, n_list))
# print(nums)
# seen = set()
# for i in nums:
#     if i in seen:
#         print('true')
#         break
#     else:
#         seen.add(i)
# else:
#     print('false')

n = 4
count = 1
for i in range(4):
    for j in range(i+1):
        print(count, end = " ")
        count += 1
    print(" ")