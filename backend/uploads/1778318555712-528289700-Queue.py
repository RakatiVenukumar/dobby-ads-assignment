class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.front = new_node
        self.rear = new_node
        self.height = 1
        
    def enqueue(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.height += 1
        return True
    
    def print_list(self):
        temp = self.front
        while temp:
            print(temp.value)
            temp = temp.next
            
    def dequeue(self):
        temp = self.front
        if  self.height == 0:
            return None
        else:
            self.front = self.front.next
            temp.next = None
        self.height -= 1
        return temp.value
        
a = Queue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.dequeue()
a.print_list()