from collections import deque
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val = val 
        self.left = left
        self.right = right 
    
    def Build(self,val):
        if self:
            if self.val > val:
                if self.left:
                    self.left.Build(val)
                else:
                    self.left = TreeNode(val)
            else:
                if self.right:
                    self.right.Build(val)
                else:
                    self.right = TreeNode(val)
        return self
    def min_Heapify(self):
        if not self:
            return
        smallest = self
        if self.left and self.left.val < smallest.val:
            smallest = self.left 
        if self.right and self.right.val < smallest.val:
            smallest = self.right
        if self != smallest:
            self.val , smallest.val  = smallest.val , self.val
            smallest.min_Heapify()

    def printLevelOrder(self,root):
        if root is None:
            return
        
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            print(current.val, end=" ")
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        print()  # Newline after printing all levels

    def array_to_tree(self,arr):
        if not arr:
            return None
        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1
        while i < len(arr):
            current = queue.popleft()
            if i < len(arr):
                current.left = TreeNode(arr[i])
                queue.append(current.left)
                i += 1
            if i < len(arr):
                current.right = TreeNode(arr[i])
                queue.append(current.right)
                i += 1
        return root

    def Build_Heap(self):
        if not self:
            return 
        if self.left:
            self.left.Build_Heap()
        if self.right:
            self.right.Build_Heap()
        self.min_Heapify()
    

root = TreeNode()    
arr = [6,9,7,8,3,2,1]
res = []
breadth = []

root = root.array_to_tree(arr)
root.Build_Heap()
print('Breadth First After Heapify',root.printLevelOrder(root))
# res = root.Depth(res)
# breadth = root.Breadth(breadth)
# print('Depth First Algorithm',res)
# print('Breadth First Algorithm',breadth)
# z = []
# root.min_Heapify()
# print('Breadth First After Heapify',root.printLevelOrder(root))



