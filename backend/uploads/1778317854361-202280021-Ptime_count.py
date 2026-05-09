def a(n):
    count = 0
    if n == 0 or n == 1:
        return 0
    else:
        if n > 1:
            for i in range(2,n): # 2 3 4 5 6 7 8 9
                for j in range(2,i): 
                    if i % j == 0:
                        break
                else:
                    count += 1
    return count
                

print(a(100))