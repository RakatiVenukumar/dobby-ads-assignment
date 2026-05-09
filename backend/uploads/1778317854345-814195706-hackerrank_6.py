# nested lists
dataList = []
scores = set()
lowestName = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    dataList.append([name, score])
#print(dataList)
    scores.add(score)
    
secondLowest = sorted(scores)[1]

for name, score in dataList:
    if score == secondLowest:
        lowestName.append(name)
        
for name in sorted(lowestName):
    print(name, end='\n')

