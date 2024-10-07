# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1 = list1
        h2 = list2
        head = ListNode()
        h3 = head

        while h1 and h2:
            nxt1 = h1.next
            nxt2 = h2.next
            if h1.val<=h2.val:
                h3.next = h1
                h1 = h1.next
    
            else:
                h3.next = h2
                h2 = h2.next
            h3 = h3.next
        
        if h1:
            h3.next = h1
        if h2:
            h3.next = h2

        return head.next
            
            


        
