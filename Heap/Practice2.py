import heapq 
from collections import deque
class TreeNode():
    def __init__(self,val=0):
        self.val = val 
        self.left = None 
        self.right = None 
    
    def Min_Heapify(self):
        smallest = self
        if self.left and self.left.val <= smallest.val:
            smallest = self.left
        if self.right and self.right.val <= smallest.val:
            smallest = self.right
        if self != smallest:
            self.val , smallest.val = smallest.val , self.val 
            smallest.Min_Heapify()

    def Build(self):
        if not self:
            return 
        if self.left:
            self.left.Build()
        if self.right:
            self.right.Build()
        self.Min_Heapify()

    def Print_Tree(self):
        arr = []
        queue = deque([self])
        while queue:
            curr = queue.popleft()
            arr.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return arr

    def array_to_Tree(self,arr):
        if not arr:
            return None 
        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1 
        while i < len(arr):
            curr = queue.popleft()
            if i < len(arr):
                curr.left = TreeNode(arr[i])
                queue.append(curr.left)
                i = i + 1 
            if i < len(arr):
                curr.right = TreeNode(arr[i])
                queue.append(curr.right)
                i = i + 1 
        return root
        

MyList = [6,9,7,8,3,2,1]
root = TreeNode()
root = root.array_to_Tree(MyList)
root.Build()
print("Min-Heapifiy using Scratch : ",root.Print_Tree())

        
heapq.heapify(MyList)
print('Min-Heapifiy using Heapq : ',(list(MyList)))

