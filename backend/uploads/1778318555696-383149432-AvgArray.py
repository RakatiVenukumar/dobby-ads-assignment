a = [10,20,30,40,50,60,70,80,90,100]
sum = 0
count = 0
for i in a:
    count += 1
print(f"The total number of elements = {count}")

for i in range(0,len(a)):
    sum += a[i]
print(f"The sum of elements = {sum}")

avg = sum//count
print(f"The average of elements = {avg}")