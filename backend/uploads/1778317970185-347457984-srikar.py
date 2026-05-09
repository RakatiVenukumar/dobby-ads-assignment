# salesRecord=[[100,198,333,323],[122,232,221,111],[223,565,245,764]]
# def maxRevenue(salesRecord):
#     result=[]
#     for i in range(0,len(salesRecord)):
#         result.append(max(salesRecord[i]))
#     return result
# num=11

num=100
list2=[]
for i in range(2,num+1):
    list1=[]
    for j in range(1,i+1):
        if i%j==0:
            list1.append(j)
    if len(list1)==2:
        list2.append(i)
print(list2)