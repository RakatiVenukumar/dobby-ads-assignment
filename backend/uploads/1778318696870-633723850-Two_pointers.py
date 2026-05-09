# Move zeroes to the end
def move_zeroes(arr):
    n = len(arr)
    i,j = 0,0
    while i < n:
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
        i += 1
    print(arr)



# max Height of container
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




# three-sum equals to 0
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
                
                while l < r and arr[l] == arr[l-1]:
                    l +=1 
                while l < r and arr[r] == arr[r+1]:
                    r -= 1
            
            elif current_sum < 0:
                l += 1
            else:
                r -= 1
    return result



# Intersection of two arrays
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



# two - sum
def Two_sum(arr,k):
    start = 0
    end = len(arr)-1
    sum = 0
    for i in range(len(arr)):
        sum = arr[start] + arr[end]
        if sum == k:
            return [arr[start],arr[end]]
        if sum > k:
            end -= 1
        else:
            start += 1
    return None


# Highest Odd Number
def Highest_odd_num(num):
    n = len(num)
    start = 0
    end = n-1
    while start < end:
        if int(num[end]) %2 != 0:
            return num[start:end+1]
        else:
            end -= 1
    return None
num = '61632534'
print(Highest_odd_num(num))