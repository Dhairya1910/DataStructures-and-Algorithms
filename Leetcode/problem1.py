
# Definition for singly-linked list.
class Solution:
    def traversal(self,root):
        temp = root
        while(temp != None):
            print(temp.val)
            temp = temp.next
        return temp
    
    def mergeTwoLists(self, list1 : Optional[ListNode], list2 : Optional[ListNode]) :
        list3 = ListNode(0)
        dummy = list3
        while list1 and list2 :
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next 
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1.next :
            dummy.next = list1
            list1 = list1.next 
            return list3.next
        if list2.next :
            dummy.next = list2
            list2 = list2.next 
            return list3.next
        






