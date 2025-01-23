class Node :
    def __init__(self , d):
       self.data = d 
       self.next = None




def AddNew(N1,N2):
    temp = N1  # type: ignore
    while temp.next is not  None :
        temp = temp.next 

    temp.next = N2
    return N1

def traversal(N1):
    temp = N1  # type: ignore
    while temp != None :
        print(temp.data) 
        temp = temp.next 




if __name__ == '__main__':

    N1 = Node(10)
    N2 = Node(20) 
    N3 = Node(50)
    N4 = Node(60)
    N1.next = N2 
    N2.next = N3
    N3.next = N4  
    N5 = Node(70)
    AddNew(N1,N5) 
    traversal(N1)