class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def Insert(self,N):
        tmp = self
        while tmp.right is not None:
            tmp = tmp.right
        tmp.right = N
        N.left = tmp
    
    def Insert_begin(self,N):
        tmp = self
        if tmp:
            tmp.left = N
            N.right = tmp
            return N
        else :
            return N 

    def Traverse(self):
        tmp = self
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.right
    
    def Searching(self,N):
        tmp = self
        index = 0
        while tmp.data != N:
            tmp = tmp.right
            index += 1
        if tmp.data == N: 
            print("Element found At",index+1,":",tmp.data)
        else:
            print("Not Found")
    def Length(self):
        tmp = self
        length = 0 
        while tmp is not None:
            length += 1 
            tmp = tmp.right
        print("Length of The Linked List is : ",length)
    
    def Specific_position(self,pos,N):
        tmp = self 
        index = 0 
        while tmp is not None:
            if index == pos-1:
                N.right = tmp.right
                tmp.right = N
                N.left = tmp 
                return self
            tmp = tmp.right
            index += 1
        if index == pos:
            tmp.right = N
            N.left = tmp
        return self 
    def Delete_begin(self):
        tmp = self 
        if tmp is None :
           return None 
        new_head = tmp.right
        if new_head is not None:
            new_head.left = None 
        return new_head
    def Delete_End(self):
        tmp = self
        while tmp.right is not None:
            tmp = tmp.right
        if tmp.left is not None:
            tmp.left.right = None 
        else :
            return None 
        return self
    def Delete_at_pos(self,pos):
        tmp = self
        new = self
        index = 0 
        while index != pos and tmp is not None:
            tmp = tmp.right
            index += 1 
        if index == pos:
            if tmp.right is not None:
                tmp.right.left = tmp.left
            if tmp.left is not None:
                tmp.left.right = tmp.right 
            return self
        else :
            return self
                  
        
Head = Node(10)
N1 = Node(15)
N2 = Node(20)
N3 = Node(30)
Head.Insert(N1)
Head.Insert(N2)
Head.Searching(15)
Head.Length()
Head = Head.Specific_position(3,N3)
# Head = Head.Insert_begin(N3)
# Head = Head.Delete_begin()
# Head = Head.Delete_End()
Head = Head.Delete_at_pos(1)
Head.Traverse()




        