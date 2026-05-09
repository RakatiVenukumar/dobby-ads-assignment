def count_substring(string, sub_string):
    count = 0
    
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            if string[i:j] == sub_string:
                count += 1
    return count
    
a = count_substring("BHUHAHAHAHAHAHBHU", "AHA")
print(a)
