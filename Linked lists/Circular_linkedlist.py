class Node():
    def __init__(self,data):
        self.data = data 
        self.next = None 

    def Insert(self , data , Head):
        if Head is None :
            Head = Node(data)
            Head.next = Head
            return Head 
        else :
            tmp = Head
            if tmp.next is not None:
                new = Node(data)
                new.next = tmp.next
                tmp.next = new 
            else : 
                new = Node(data)
                tmp.next = new
                new.next = tmp
            return Head 
    
    def Insert_begin(self,data,Head):
        tmp = Head
        new = Node(data)
        if tmp.next is None:
            new.next = tmp
            tmp.next = new
            return self
        else:
            while tmp.next != Head:
                tmp = tmp.next
            tmp.next = new
            new.next = Head
            Head = new
            return Head
    
    def Insert_End(self,data,Head):
        tmp = Head 
        new = Node(data)

        if tmp.next is None :
            tmp.next = new
            new.next = Head
            return Head
        else:
            while tmp.next != Head:
                tmp = tmp.next
            tmp.next = new
            new.next = Head 
            return Head 
        
    def Insert_at_pos(self,data,pos,Head):
        tmp = Head 
        new = Node(data)
        index = 0
        if pos <= 0 or Head is None:
            Head = self.Insert_begin(data,Head)
            return Head
        while pos-1 != index and index < (pos-1):
            index += 1 
            tmp = tmp.next
        if pos-1 == index:
            new.next = tmp.next
            tmp.next = new 
        if (pos-1) < index:
            print("Out of Bound ")
        return Head
        
    def Delete_begining(self,Head):
        tmp = Head
        if Head is None:
            print("List is empty")
            return None
        if tmp.next == Head or tmp.next is None:
            return None 
        while tmp.next != Head :
            tmp = tmp.next
        tmp.next = Head.next 
        Head = Head.next 
        return Head
        
    def Traversal(self,Head):
        tmp = Head 
        if tmp is None:
            print("Empty List")
        while True:
            print(tmp.data)
            tmp = tmp.next
            if tmp == Head:
                break

Head = Node(10)
Head = Head.Insert(20,Head)
Head = Head.Insert(40,Head)
Head = Head.Insert(50,Head)
Head = Head.Insert(30,Head)
Head = Head.Insert_begin(5,Head)
Head = Head.Insert_End(60,Head)
Head = Head.Insert_at_pos(55,3,Head)
Head = Head.Delete_begining(Head)
if Head == None:
    print("Linked list is Empty")
else:
    Head.Traversal(Head)

        

        
