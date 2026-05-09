# max number by taking input 

a = input("enter the list seperated by a space bar:")
list = a.split(" ")
print(list)
count = 0
for i in list:
    count = count + 1
print(count)
for j in range(0,count):
    list[j] = int(list[j])
print(list)
maximum = list[0]
for number in list:
    if (number > maximum):
        maximum = number
print("the maximum number is ", maximum)

    
