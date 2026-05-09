from collections import deque

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None 
 
# insert
    def insert(self,value):
        self.root = self.insert_recursively(self.root, value)
    
    def insert_recursively(self, current, value):
        if current is None:
            return Node(value)
        if value < current.value:
            current.left = self.insert_recursively(current.left, value)
        elif value > current.value:
            current.right = self.insert_recursively(current.right, value)
        return current

# pre order   
    def pre_order(self):
        return self._pre_order_recursively(self.root, [])         # node --> left --> right
        
    def _pre_order_recursively(self, current, result):
        if current:
            result.append(current.value)
            self._pre_order_recursively(current.left, result)
            self._pre_order_recursively(current.right, result)
        return result
    
# in order
    def in_order(self):
        return self._in_order_recursively(self.root, [])           # left --> node --> right
    
    def _in_order_recursively(self, current, result):
        if current:
            self._in_order_recursively(current.left, result)
            result.append(current.value)
            self._in_order_recursively(current.right, result)
        return result

# post order
    def post_order(self):
        return self._post_order_recursively(self.root, [])         # left --> right --> node
    
    def _post_order_recursively(self, current, result):
        if current:
            self._post_order_recursively(current.left, result)
            self._post_order_recursively(current.right, result)
            result.append(current.value)
        return result 
    
# DFS - Depth First Search
    def DFS(self):            # iterative pre-order traversal
        if not self.root:
            return []
        stack = [self.root]
        result = []
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

            
# BFS - Breadth First Search
    def BFS(self):                # level order traversal
        if not self.root:
            return []
        queue = deque([self.root])
        result = []
        while queue:
            current = queue.popleft()
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    
    def MaxDepth(self, node = None):
        if node is None:
            return 0
        left_depth = self.MaxDepth(node.left)
        right_depth = self.MaxDepth(node.right)
        return 1 + max(left_depth, right_depth)
    
    def get_maxdepth(self):
        return self.MaxDepth(self.root)
    
    # def MaxDepth(self):
    #     if not self.root:
    #         return 
    #     queue = deque([self.root])
    #     depth = 0
    #     while queue:
    #         for _ in range(len(queue)):
    #             current = queue.popleft()
    #             if current.left:
    #                 queue.append(current.left)
    #             if current.right:
    #                 queue.append(current.right)
    #         depth += 1
    #     return depth
    
    def Mindepth(self, node = None):
        if not node:
            return 0
        if not node.left:
            return 1 + self.Mindepth(node.right)
        if not node.right: 
            return 1 + self.Mindepth(node.left)
        return 1 + min(self.Mindepth(node.left), self.Mindepth(node.right))
    
    def get_minDepth(self):
        return self.Mindepth(self.root)
    
    def Symmetric_tree(self):
        if not self.root:
            return True
        queue = deque([self.root.left, self.root.right])
        while queue:
            t1= queue.popleft()
            t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.value != t2.value:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        return True

    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.value != q.value:
            return False
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
       
    def isSubTree(self, root, subroot):  
        # def isSameTree(s, t):
        #     if not s and not t:
        #         return True
        #     if not s or not t or s.value != t.value:
        #         return False
        #     return t.value == s.value or isSameTree(s.left, t.left) or isSameTree(s.right, t.right)
        if not root:
            return False
        if self.isSame(root, subroot):
            return True
        return self.isSame(root.left, subroot) or self.isSame(root.right, subroot)
    
    def Invert_bt(self):
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return self.root.value
            
    def hasPathSum(self, target):
        if not self.root:
            return False
        stack = [(self.root, target)]
        while stack:
            current, curr_sum = stack.pop()
            if not current.left and not current.right and current.value == curr_sum:
                return True
            if current.right:
                stack.append((current.right, curr_sum - current.value))
            if current.left:
                stack.append((current.left, curr_sum - current.value))
        return False                 
                     
    def isBalanced(self):
        if not self.root:
            return False
        def check_balanced(node):
            if not node:
                return True
            left_height = check_balanced(node.left)
            if left_height == -1:
                return False
            right_height = check_balanced(node.right)
            if right_height == -1:
                return False
            
            if abs(left_height - right_height) > 1:
                return False
            return 1 + max(left_height, right_height)
        return check_balanced(self.root) != -1
               
    def Diameter(self):
        if not self.root:
            return 
        self.diameter = 0
        
        def height(node):
            if not node:
                return 0 
            left_height = height(node.left)
            right_height = height(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            
            return 1 + max(left_height, right_height)
        height(self.root)
        return self.diameter  
    
    def isValidBST(self):
        if not self.root:
            return
        def validate(node, low=-float('inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.value < high):
                return False
            return (validate(node.left, low, node.value) and
                    validate(node.right, node.value, high))
        return validate(self.root)
    
a = BinaryTree()
a.insert(10)
a.insert(14)
a.insert(5)
a.insert(3)
a.insert(7)
a.insert(12)
a.insert(18)
print(a.isValidBST())