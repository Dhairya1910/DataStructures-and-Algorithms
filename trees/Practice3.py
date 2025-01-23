# class Node:
#     def __init__(self,data) :
#         self.data = data
#         self.right = None
#         self.left = None 
    
#     def Insert(self,data):

#             if self.data > data : 
#                 if self.left : 
#                     self.left.Insert(data)
#                 else : 
#                     self.left = Node(data)
#             else : 
#                 if self.right:
#                     self.right.Insert(data)
#                 else :
#                     self.right = Node(data)
      

#     def Traversal(self):
#         if self.left : 
#             self.left.Traversal()
#         print(self.data)
#         if self.right:
#             self.right.Traversal()

#     def Inorder(self,root):
#         res = []
#         if root :
#             res = self.Inorder(root.left)
#             res.append(root.data)
#             res = res + self.Inorder(root.right)
#         return res
    
#     def Max_Heapify(self,root): 
            
#             if root is None : 
#                 return 
            
#             largest = root
#             if root.left and root.left.data > root.data:
#                largest = root.left
#             if root.right and root.right.data > largest.data:
#                 largest = root.right
#             if largest != root: 
#                 root.data , largest.data = largest.data , root.data 
#                 self.Max_Heapify(largest)

                







# if __name__ == '__main__':

#     root = Node(10)
#     root.Insert(20)
#     root.Insert(25)
#     root.Insert(15)
#     root.Insert(5)
#     root.Insert(8)
#     root.Insert(7)
#     # arr = root.Inorder(root)
#     print(root.Inorder(root))
#     root.Max_Heapify(root)
#     print("After Max Heapifiy")
#     print(root.Inorder(root))

#     # root.Traversal()

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def Insert(self, data):
        if data < self.data:
            if self.left:
                self.left.Insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.Insert(data)
            else:
                self.right = Node(data)

    def Traversal(self):
        if self.left:
            self.left.Traversal()
        print(self.data)
        if self.right:
            self.right.Traversal()

    def Inorder(self, root):
        res = []
        if root:
            res = self.Inorder(root.left)
            res.append(root.data)
            res = res + self.Inorder(root.right)
        return res

    def Max_Heapify(self, root):
        if root is None:
            return

        largest = root
        if root.left and root.left.data > root.data:
            largest = root.left

        if root.right and root.right.data > largest.data:
            largest = root.right

        if largest != root:
            root.data, largest.data = largest.data, root.data
            self.Max_Heapify(largest)

if __name__ == '__main__':
    root = Node(10)
    root.Insert(20)
    root.Insert(25)
    root.Insert(15)
    root.Insert(5)
    root.Insert(8)
    root.Insert(7)

    print("Inorder Traversal before Max_Heapify:", root.Inorder(root))
    root.Max_Heapify(root)
    print("After Max Heapify")
    print("Inorder Traversal after Max_Heapify:", root.Inorder(root))
    print("Preorder Traversal after Max_Heapify:", root.preOrder(root))

