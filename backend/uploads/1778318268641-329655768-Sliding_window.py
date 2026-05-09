# Minimum subarray length equal to target
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



# Longest substring without repeating characters 
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




# Minimum subarray string
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



# maximum sliding window
def sliding_window_max(nums,k):
    start = 0
    max_window = []
    for end in range(len(nums)-k+1):
        current_window = nums[start:start+k]
        max_window.append(max(current_window))
        start += 1
    return max_window




# longest subarray less than or equal to k
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

def Max_avg_subarray(arr, k):
    n = len(arr)
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]
    max_avg = curr_sum / k
    
    for i in range(k, n):
        curr_sum += arr[i]
        curr_sum -= arr[i-k]
        avg = curr_sum / k
        max_avg = max(avg, max_avg)
    return max_avg