# average heights of person without using len(), sum() functions

a = input("enter the list of heights: ")
list = a.split(" ")
print(list) 

count = 0
for heights in list:
    count = count + 1
print(count)
for i in range(0,count):
    list[i] = int(list[i])
     
    
total = 0
for person in list:
    total += person
print(total)
avg = total/count
print(round(avg))   
     