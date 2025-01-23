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

    def Level():


if __name__ == '__main__':
