def find_anagrams(s, p):

    result = []
    p_count = {}
    s_count = {}
    for char in p:
        p_count[char] = p_count.get(char,0)+1

        
    p_len = len(p)
    for i in range(len(s)):
        s_count[s[i]] = s_count.get(s[i],0)+1
        
        if i >= p_len:
            if s_count[s[i-p_len]] == 1:
                del s_count[s[i-p_len]]
            else:
                s_count[s[i-p_len]] -= 1
                
        if p_count == s_count:
            result.append(i-p_len+1)
            
    return result
# s = "cbaebabacd"
# p = "abc"        


def subarray_sum(arr,k):
    count = 0
    sum = 0
    dict1 = {0:1}

    for i in arr:
        sum += i
        
        if sum - k in dict1:
            count += dict1[sum-k]
            
        if sum in dict1:
            dict1[sum] += 1
        else:
            dict1[sum] = 1
            
    return count


