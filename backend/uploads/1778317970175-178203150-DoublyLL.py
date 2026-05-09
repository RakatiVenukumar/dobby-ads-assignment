class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
class DLL:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp!= None:
            print(temp.value)
            temp = temp.next
            
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value
    
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
             return self.append(value)
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node
        self.length += 1
        return True
            
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            return self.pop()
        else:
            self.head = self.head.next
            self.temp = None
            self.head.prev = None
        self.length -= 1
        return temp.value
    
    def get(self,index):
        if index < 0 or index > self.length:
            return False
        else:
            temp = self.head
            if index < self.length//2:
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1,index,-1):
                    temp = temp.prev
        return temp.value 
    
    def set(self,index,value):
        if index < 0 or index > self.length:
            return False
        else:
            temp = self.head
            if index < self.length//2:
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1,index,-1):
                    temp = temp.prev
            temp.value = value
            
    def InsertAtIndex(self,index,value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return a.prepend(value)

        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        before = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        new_node.next = before 
            
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        before = self.head
        for i in range(index-1):
            before = before.next
        temp = before.next
        after = before.next.next
        before.next = temp.next 
        after.prev = before.prev
        # temp.next.prev = before.next.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return True
        
    def swap_first_and_last(self):
        if self.length == 0:
            return None
        self.head.value, self.tail.value = self.tail.value, self.head.value
        
    def reverse(self):
        temp = self.head
        while temp:
            temp.next,temp.prev = temp.prev,temp.next
            temp = temp.prev
        self.head, self.tail = self.tail, self.head
        return True
    
    def palindrome_check(self):
        if self.length <= 0:
            return True
        temp1 = self.head
        temp2 = self.tail
        for i in range(self.length//2):
            if temp1.value != temp2.value:
                return False 
            temp1 = temp1.next
            temp2 = temp2.prev
        return True
    
    def swap_pairs(self):
        if self.length == 0 or self.length == 1:
            return False
        else:
            dummy = Node(None)
            dummy.next = self.head
            before = dummy
            
            while before.next and before.next.next:
                first = before.next
                second = before.next.next 
            
                first.next = second.next 
                if second.next:
                    second.next.prev = first
                    
                second.next = first
                first.prev = second
                before.next = second
                second.prev = before
                before = first
                
            self.head = dummy.next
        return True

        
a = DLL(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
#.append(6)
a.swap_pairs()
a.print_list()
