class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty_stack(self):
        return len(self.stack) == 0
    
    def print_list(self):
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i])
            
    def push(self,items):
        self.stack.append(items)
        return True
    
    def pop(self):
        if not self.is_empty_stack():
            pop_item = self.stack.pop()
            return pop_item
        return None
    
    def peek(self):
        if not self.is_empty_stack():
            return self.stack[-1]
        else:
            return None
    
    def length_stack(self):
        return len(self.stack)
    
    def parentheses_balanced(self,parentheses):
        self.stack = Stack()
        for i in parentheses:
            if i == '(':
                self.stack.push(i)
            elif i == ')':
                if self.stack.is_empty_stack():
                    return False
                else:
                    self.stack.pop()
        return self.stack.is_empty_stack()       
            
    def reverse(self,string):
        stack = Stack()
        reversed_string = ''
        for i in string:
            self.stack.append(i)
        while not self.is_empty_stack():
            reversed_string += self.stack.pop()
        return reversed_string
    
    def sort(self):
        sorted_stack = Stack()
        while not self.is_empty_stack():
            temp = self.pop()
            while not sorted_stack.is_empty_stack() and sorted_stack.peek() > temp:
                self.push(sorted_stack.pop())
            sorted_stack.push(temp)
        while not sorted_stack.is_empty_stack():
            self.push(sorted_stack.pop())     

a = Stack()
a.push(2)
a.push(4)
a.push(5)
a.push(1)
a.push(3)
print(a.reverse("venu"))
