arr = [1,2,6,10,12,14,17,18,21,22,24,25,26,28]
x = 6
def BinarySearch(a,x,low,high):
    while low <= high:
        mid = (low + high)//2  
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            high = mid-1
        elif a[mid] < x:
            low = mid + 1
    return 0

result = BinarySearch(arr,x,0,len(arr)-1)

if result == 0:
    print("Element not found")
else:
    print(f'Element found: {result}')