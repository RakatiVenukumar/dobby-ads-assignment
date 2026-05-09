import heapq
   
def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    heap = []
    for i in range(n):
        min = heapq.heappop(arr)
        heap.append(min)
    return heap

def max_heap(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = -arr[i]
    heapq.heapify(arr)          
    b = []
    
    for i in range(n):
        largest = -heapq.heappop(arr)
        b.append(largest)   
    return b

def kth_largest(a,k):
    min_heap = a[:k]
    heapq.heapify(min_heap)

    for i in a[k:]:
        if i > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, i)
    return min_heap[0]
     
# a = [3,2,1,5,6,4]
# k = 2
# min_heap = []
# for i in a:
#     heapq.heappush(min_heap, i)
#     if len(min_heap) > k:
#         heapq.heappop(min_heap)

def top_k_elements(arr,k):
    dict1 = {}
    result = []

    for i in arr:
        dict1[i] = dict1.get(i, 0) + 1

    min_heap = []
    for num, freq in dict1.items():
        heapq.heappush(min_heap, (freq,num))

        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    while min_heap:
        freq, num = heapq.heappop(min_heap)
        result.append(num)   
    return result

def last_stone_weight(a):
    for i in range(len(a)):
        a[i] = -a[i]
    heapq.heapify(a)

    while len(a) > 1:
        heaviest = -heapq.heappop(a)
        second_heaviest = -heapq.heappop(a)
        
        if heaviest != second_heaviest:
            heapq.heappush(a, -(heaviest - second_heaviest))
    if a:
        return -a[0]
    else:
        return 0

# a = 'tree'
def frequency_sort(a):
    dict1 = {}
    for i in a:
        dict1[i] = dict1.get(i, 0) + 1

    max_heap = []
    for i,freq in dict1.items():
        heapq.heappush(max_heap, ((-freq), i))
    heapq.heapify(max_heap)

    result = []
    while max_heap:
        freq, i = heapq.heappop(max_heap)
        result.append(i*(-freq))
    result = "".join(result)
    return result

def K_closest(a,k):
    max_heap = []
    for x, y in a:
        distance = (x**2 + y**2)
        
        heapq.heappush(max_heap, ((-distance), [x,y]))
        
        if len(max_heap) > k:
            heapq.heappop(max_heap)
            
    result = []
    for (_,point) in max_heap:
        result.append(point)
    return result

def merge_sorted_lists(a):
    result = []
    min_heap = []
    for i in range(len(a)):
        heapq.heappush(min_heap, (a[i][0], i, 0))
        
    while min_heap:
        num, list_index, element_index = heapq.heappop(min_heap)
        result.append(num)

        if element_index + 1 < len(a[list_index]):
            next_num = a[list_index][element_index+1]
            heapq.heappush(min_heap, (next_num, list_index, element_index+1))
    return result
