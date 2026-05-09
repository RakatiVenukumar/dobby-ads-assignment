arr = input().split(" ")
arr = list(map(int,arr))
print(arr)
# arr = [2,1,3,4,6]
n = len(arr)
target = 12
count = 0 
if n < 2:
    print("Invalid input")

for num_elements in range(2,n+1):
    for i in range(n):
        product = 1
        for j in range(num_elements):
            product *= (arr[(i+j)%n])
        if product == target:
            count += 1
print(count) 
