class MinHeap:
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
        
    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self.parent_node(current)]:
                self.swap_nodes(current,self.parent_node(current))
                current = self.parent_node(current)
        return True
    
    def sink_down(self,index):
        max_index = index
        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)
        
            if left_index < len(self.heap) and self.heap[left_index] < self.heap[max_index]:
                max_index = left_index
                
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[max_index]:
                max_index = right_index
                
            if max_index != index:
                self.swap_nodes(max_index,index)
                index = max_index
            else:
                return 
            
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        if len(self.heap) > 1:
            max_value = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.sink_down(0) 
        return max_value   
                
     
a = MinHeap()
a.insert(99)
a.insert(65)
a.insert(72)
a.insert(58)
a.insert(50)
a.insert(49)
print(a.heap)
a.remove()
print(a.heap)