class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def traversal(self,root):
        temp = root
        while temp is not None:
            print(temp.val)
            temp = temp.next
    
    def addTwoNumbers(self, l1, l2) :
        dummy = ListNode()
        tmp = dummy
        total= carry= 0 
        while l1 or l2 or carry:
            total = carry
            if l1:
                total = l1.val + total
                l1 = l1.next 
            if l2:
                total = l2.val + total 
                l2 = l2.next 
            
            no = total % 10
            carry = total // 10 
            dummy.next = ListNode(no)
            dummy = dummy.next
        return tmp.next 


n3 = ListNode(3,None)
n2 = ListNode(2,n3)
root_l1 = ListNode(1,n2)

N3 = ListNode(3,None)
N2 = ListNode(2,N3)
root_l2 = ListNode(1,N2)

L3 = Solution()
merger = L3.addTwoNumbers(root_l1,root_l2)
L3.traversal(merger)

