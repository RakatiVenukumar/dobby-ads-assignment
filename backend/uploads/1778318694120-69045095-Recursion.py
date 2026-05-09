def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fact(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * fact(n-1)

def binary_search(arr,target,left,right):
    if left > right:
        return -1
    mid = (left + right)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr,target,left,mid-1)
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,right)

def deci_to_bin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return deci_to_bin(n//2) + str(n%2)

