class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self,value):
        self.stack1.append(value)
        
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def peek(self):
        if len(self.stack2) > 0:
            return self.stack2[-1]
        elif len(self.stack1) > 0:
            return self.stack1[0]
        return None
            
    def dequeue(self):
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) > 0:
            return self.stack2.pop()
        return None
    
    
    def print_list(self):
        for i in range(len(self.stack2)-1,-1,-1):
            print(self.stack2[i])
        for i in self.stack1:
            print(i)
    
a = Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.dequeue()
a.enqueue(4)
a.enqueue(5)
a.enqueue(6)
a.dequeue()
a.dequeue()
a.print_list()
print(a.peek())