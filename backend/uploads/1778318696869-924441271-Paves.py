# n = list(map(int, input().split()))
# dict1 = {}
# for i in n:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# for key, value in dict1.items():
#     if value == 1:
#         print(key)
#         break
       
       
# n = list(map(int, input().split()))
# target = int(input())
# dict1 = {}
# for i, num in enumerate(n):
#     diff = target - num
#     if diff in dict1:
#         print([dict1[diff], i])
#         break
#     dict1[num] = i
 
 
# n = int(input())
# fib = {0:0, 1:1}
# for i in range(2, n):
#     fib[i] = fib[i-1] + fib[i-2]
# for i in range(n):
#     print(fib[i], end = " ")

# n1, n2 = input().split()
# if len(n1)!= len(n2):
#     print("Not anagrams")
# else:
#     d = {}
#     for i in n1:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
    
#     for i in n2:
#         if i in d:
#             d[i] -= 1
#         else:
#             d[i] = 1
    
#     is_anagrams = True
#     for i in d:
#         if d[i] != 0:
#             is_anagrams = False
#             break
# if is_anagrams:
#     print("Anagrams")
# else:
#     print("Not Anagrams")


# n = int(input())
# arr = list(map(int, input().split()))
# if n == 1:
#     print(arr[0])
# elif n > 2:
#     buy = arr[0]
# max_profit = 0
# for i in range(1, n):
#     if buy > arr[i]:
#         buy = arr[i]
#     else:
#         max_profit = max(max_profit, arr[i] - buy)
# print(max_profit)


# n = int(input())
# arr = list(map(int, input().split()))
# k = 3
# dict1 = {0:1}
# curr_sum = 0
# count = 0
# for i in arr:
#     curr_sum += i
#     if curr_sum - k in dict1:
#         count += dict1[curr_sum - k]
#     if curr_sum in dict1:
#         dict1[curr_sum] += 1
#     else:
#         dict1[curr_sum] = 1
# print(count)


# n = int(input())
# arr = list(map(int, input().split()))
# l = 0
# m = 0
# h = n-1
# while m <= h:
#     if arr[m] == 0:
#         arr[l], arr[m] = arr[m], arr[l]
#         l += 1
#         m += 1
#     elif arr[m] == 1:
#         m += 1
#     elif arr[m] == 2:
#         arr[m], arr[h] = arr[h], arr[m]
#         h -= 1
# print(arr)


# n = int(input())
# arr = list(map(int, input().split()))
# dict1 = {}
# target = int(input())
# for i in range(len(arr)):
#     curr_sum = target - arr[i]
#     if curr_sum not in dict1:
#         dict1[arr[i]] = i
#     else:
#         print([dict1[curr_sum], i])
#         break    


# n = int(input())
# arr = list(map(int, input().split()))
# prefix = [0] * n
# suffix = [0] * n
# result = [0] * n

# prefix[0] = 1
# for i in range(1, n):
#     prefix[i] = prefix[i-1] * arr[i-1]
# suffix[-1] = 1
# for i in range(n-2,-1,-1):
#     suffix[i] = suffix[i+1] * arr[i+1]
# for i in range(n):
#     result[i] = prefix[i] * suffix[i]
# print(result)


# n = int(input())
# arr = list(map(int, input().split()))
# curr_sum = max_sum = arr[0]
# for i in arr:
#     curr_sum = max(i, curr_sum + i)
#     max_sum = max(max_sum, curr_sum)
# print(max_sum)


# n = input()
# dict1 = {}
# for i in n:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# is_there = True
# for key, val in dict1.items():
#     if val == 1:
#         is_there = False
#         print(key)
#         break
# if is_there:
#     print(-1)


# s = input()
# t = input()
# dict1 = {}
# if len(s) != len(t):
#     print("NO")
#     exit()
# else:
#     if sorted(s) == sorted(t):
#         print("YES")
#     else:
#         print("NO")

# for i in s:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1

# for i in t:
#     if i in dict1:
#         dict1[i] -= 1
#     else:
#         print('NO')
#         exit()

# for freq in dict1:
#     if dict1[freq] >= 1:
#         print('NO')
#         break
# else:
#     print('YES')


# n = int(input())
# arr = list(map(int, input().split()))
# count = 0
# k = int(input())
# for i in arr:
#     if i - k > k:
#         count += 1
# print(count)    


