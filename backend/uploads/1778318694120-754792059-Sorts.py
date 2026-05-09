# bubble sort
nums = [4,2,5,1,3]
n = len(nums)
def bubbleSort(nums):
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

# insertion sort
def insertionSort(nums):
    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break
    return nums

# selection sort
def selectionSort(nums):
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
    return nums

# merge sort
def mergeSort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    
    mid = n // 2
    L = nums[:mid]
    R = nums[mid:]
    L = mergeSort(L)
    R = mergeSort(R)
    
    l, r = 0, 0
    nums1 = []
    
    while l < len(L) and r < len(R):
        if L[l] > R[r]:
            nums1.append(R[r])
            r += 1
        else:
            nums1.append(L[l])
            l += 1
    
    while l < len(L):
        nums1.append(L[l])
        l += 1
    while r < len(R):
        nums1.append(R[r])
        r += 1      
    # nums1.extend(L[l:])
    # nums1.extend(R[r:])
    return nums1

# quick sort
def quickSort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    pivot = nums[-1] 
    left = []
    right = []
    for num in nums[:-1]:
        if num > pivot:
            right.append(num)
        else:
            left.append(num)
    left = quickSort(left)
    right = quickSort(right)
    return left + [pivot] + right
