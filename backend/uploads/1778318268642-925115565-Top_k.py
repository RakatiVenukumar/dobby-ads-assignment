import heapq
from collections import Counter
def top_k(arr, k):
    freq = Counter(arr)
    min_heap = []
    for num,count in freq.items():
        heapq.heappush(min_heap,(count,num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)       
    result = []
    while min_heap:
        count,num = heapq.heappop(min_heap)
        result.append(num)
    return result

arr = [1,1,1,2,2,3,4,4]
k = 3
print(top_k(arr, k))
