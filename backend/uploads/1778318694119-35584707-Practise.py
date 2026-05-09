class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
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
            self.tail = new_node
        self.length += 1
        return True
       
    def print_list(self):
        temp = self.head
        for i in range(self.length):
            print(temp.value)
            temp = temp.next 
            
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
        self.length -= 1
        return temp      

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head,self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
        
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head,self.tail = None
        else:
            self.head = temp.next
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.value
    
    def set(self,index,value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value
        return temp
    
    def InsertAtIndex(self,value,index):
        if index < 0 or index > self.length:
            return False
        new_node = Node(value)
        temp = self.head
        if index == 0:
            new_node.next = self.head
            self.head= new_node
            # return self.prepend(value)
        else:
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            temp = self.head
            self.head = temp.next
            temp.next = None
            # return self.pop_first(index)
        before = self.head
        if index > 0:
            for _ in range(index-1):
                before = before.next
            temp = before.next
            before.next = temp.next
            temp.next = None
        self.length -= 1
        return temp 
    
    def reverse(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.tail
        self.tail = temp
        if self.length == 1:
            return temp
        before = None
        after = temp
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True
    
    def middle_value(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head.value
        fast = self.head
        slow = self.head
        if self.length > 1:
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
        return slow.value
    
    def has_loop(self):
        fast = self.head
        slow = fast
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def kth_node_from_the_end(self,k):
        if self.length == 0 or k > self.length:
            return None
        self.reverse()
        temp = self.head
        for i in range(k-1):
            temp = temp.next
        return temp.value
    
    def partition_list(self,x):
        dummy1 = Node(None)
        dummy2 = Node(None)
        if self.head is None:
            return None
        if self.length == 1:
            return self.head.value
        temp = self.head
        prev1 = dummy1
        prev2 = dummy2
        if self.length > 1:
            for i in range(self.length):
                if temp.value < x:
                    prev1.next = temp
                    prev1 = prev1.next
                else:
                    prev2.next = temp
                    prev2 = prev2.next
                temp = temp.next
            prev1.next = dummy2.next
            prev2.next = None
            self.head = dummy1.next
            
    def remove_duplicates(self):        
        set1 = set()
        temp = self.head
        before = None
        while temp is not None:
            if temp.value in set1:
                before.next = temp.next  # skip the duplicate
                self.length -= 1
            else:
                set1.add(temp.value)
                before = temp
            temp = temp.next

    def binary_to_decimal(self):
        temp = self.head
        value = 0
        for i in range(self.length):
            if temp.value == 1:
                value += 2**(self.length-i-1)
                temp = temp.next
        return value
    
    def reverse_between(self,start_index,end_index):
        if start_index == end_index:
            return True
        temp = self.head
        prev = None
        
        if start_index > 0:
            for i in range(start_index):
                prev = temp
                temp = temp.next
                
        connection = prev
        tail = temp
        before = None  
           
        for i in range(start_index,end_index+1):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
        if connection is not None:
            connection.next = before
        else:
            self.head = before
        
        tail.next = temp
                         
        return True  
                
    def bubble_sort(self):
        if not self.head:
            return None
        for i in range(self.length):
            swapped = False
            current = self.head
            while current and current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next
            if not swapped:
                break
        return True
                
    def Insertion_sort(self):
        if not self.head:
            return None
        dummy = Node(None)
        dummy.next = self.head
        prev, cur = self.head, self.head.next
        
        while cur:
            if cur.value > prev.value:
                prev = cur
                cur = cur.next 
                continue
            
            temp = dummy
            while cur.value > temp.next.value:
                temp = temp.next
            prev.next = cur.next 
            cur.next = temp.next
            temp.next = cur
            cur = prev.next
        return dummy.next
    
    def selection_sort(self):
        if not self.head:
            return None
        temp1 = self.head
        while temp1 != None:
            current = temp1
            temp2 = temp1.next
            while temp2 is not None:
                if current.value > temp2.value:
                    current = temp2
                temp2 = temp2.next 
            current.value, temp1.value = temp1.value, current.value
            temp1 = temp1.next
            
            
a = LinkedList(4)
a.append(2)
a.append(1)
a.append(5)
a.append(6)
a.append(3)
a.Insertion_sort()
a.print_list()