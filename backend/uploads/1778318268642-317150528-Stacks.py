class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
            
    def print_list(self):
        temp = self.top
        while temp!= None:
            print(temp.value)
            temp = temp.next
    
    def pop(self):
        temp = self.top
        if self.height == 0:
            return None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp.value
               
a = Stack(1)
a.push(2)
a.push(3)
a.push(4)
a.pop()
a.print_list()