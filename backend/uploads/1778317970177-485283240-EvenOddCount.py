a = [12,23,38,28,25,33,26,34,29,31]
even_count = 0
odd_count = 0
for i in range(0,len(a)):
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print(f"Number of even elements = {even_count}")
print(f"Number of odd elements = {odd_count}")