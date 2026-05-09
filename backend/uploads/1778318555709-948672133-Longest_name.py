list1 = ["GeeksforGeeks", "FreeCodeCamp", "StackOverFlow", "MyCodeSchool"]
list2 = []
max = 0
for i in list1:
    if len(i) > max:
        max = len(i)
        
for i in range(0,len(list1)):
    if len(list1[i]) == max:
        list2.append(list1[i])
print(list2)
