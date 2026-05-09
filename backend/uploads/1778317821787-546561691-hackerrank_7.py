n = int(input())
def avg(scores): 
    count = len(scores)
    avg = sum(scores)/count
    print(avg)

marks = {}

for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    marks[name] = scores
    
query_name = input("enter the query_name: ")


if query_name in marks:
    avg(marks[query_name])
else:
    print("student not found")