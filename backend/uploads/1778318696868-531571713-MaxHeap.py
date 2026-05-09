class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def left_child(self,index):
        return (2 * index) + 1
    
    def right_child(self,index):
        return (2*index) + 2
    
    def parent_node(self,index):
        return (index - 1) // 2
    
    def swap_nodes(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]
        
    def Insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] < self.heap[self.parent_node(current)]:
            self.swap_nodes(current,self.parent_node(current))
            current = self.parent_node(current)
        return True
    
    def sink_down(self,index):
        min_index = index
        left_index = self.left_child(index)
        right_index = self.right_child(index)
        
        while True:
            if left_index > len(self.heap) and self.heap[left_index] > self.heap[min_index]:
                min_index = left_index
                
            if right_index > len(self.heap) and self.heap[right_index] > self.heap[left_index]:
                min_index = right_index
                
            if min_index != index:
                self.swap_nodes(index,min_index)
                index = min_index
            else:
                return 
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        
        return min_value
    
    
a = MaxHeap()
a.Insert(99)
a.Insert(73)
a.Insert(72)
a.Insert(58)
a.Insert(50)
print(a.heap)
a.remove()
print(a.heap)