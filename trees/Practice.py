class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None 
    
    def Insert_Tree(self,data):
        new_node = Node(data)
        if self is None:
            return new_node
        if self.data > data :
            if self.left is None : 
                self.left = new_node
            else : 
                self.left.Insert_Tree(data)
        else : 
            if self.right is None : 
                self.right = new_node
            else : 
               self.right.Insert_Tree(data)         

    def Inorder(self,root):
        if root is None:
            return 
        if self.left :
            self.Inorder(root.left)
        print(root.data , end=" ")
        if self.right :
            self.Inorder(root.right) 
    
    def PostOrder(self):
        if self is None:
            return
        if self.left :
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.data , end=" ")
        
    def PreOrder(self):
        if self is None:
            return 
        print(self.data,end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()

    def LevelOrder(self):
        queue = []
        visited = []
        queue.append(root)
        visited.append(root.data)
        while queue :
            x = queue.pop(0)
            if x.left:
                queue.append(x.left)
                visited.append(x.left.data)
            if x.right :
                queue.append(x.right)
                visited.append(x.right.data)
        return visited       
if __name__ == '__main__':
    root = Node(10)
    arr = [2,3,20,11,5,17,21,25]
    for i in arr:
        root.Insert_Tree(i)
    print("Inorder ")
    root.Inorder(root)
    print("\nPost-Order ")
    root.PostOrder()
    print("\nPre-Order ")
    root.PreOrder()
    lst = root.LevelOrder()
    print("\nLevel Order : ",lst)



