class Node : 
    def __init__(self,Data):
        self.Data = Data
        self.Next = None


    def Traversal(self):
        temp = self
        while temp != None:
            print(temp.Data)
            temp = temp.Next
    
    def AddBegin(self,N2):
        N2.Next = self
        self = N2
        return self
    
    def ByIndex(self,number):
        temp = self
        for x in range(number):
            temp = temp.Next
        temp2 = temp.next 
        


        

        

if __name__ == '__main__':
    
    N1 = Node(10)
    N2 = Node(20)
    N3 = Node(40)
    N4 = Node(50)

    N1.Next = N2 
    N2.Next = N3 
    N3.Next = N4 

    N5 = Node(60)
    N1 = N1.AddBegin(N5)
    N1.Traversal()