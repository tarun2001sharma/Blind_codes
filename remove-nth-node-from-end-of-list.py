class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Step 1: Reverse the list
        last = self.reverseList(head)
        
        # Step 2: Remove the nth node from the beginning of the reversed list
        prev = None
        curr = last
        counter = 1
        
        # If we need to remove the first node in the reversed list
        if n == 1:
            last = curr.next  # Skip the first node (which is the nth from the end)
        else:
            while counter < n:
                prev = curr
                curr = curr.next
                counter += 1
            
            # Remove the nth node
            if prev:
                prev.next = curr.next

        # Step 3: Reverse the list back to its original order
        head = self.reverseList(last)
        
        return head

'''
One-pass approach below
'''
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # Create a dummy node that points to the head of the list
#         # This is helpful when we need to delete the head itself
#         dummy = ListNode(0)
#         dummy.next = head
        
#         # Initialize two pointers
#         first = dummy
#         second = dummy
        
#         # Move first pointer n+1 steps ahead so there is a gap of n between first and second
#         for _ in range(n + 1):
#             first = first.next
        
#         # Move both pointers until first reaches the end of the list
#         while first:
#             first = first.next
#             second = second.next
        
#         # second.next is the node to remove, adjust the pointers to remove it
#         second.next = second.next.next
        
#         # Return the head of the modified list
#         return dummy.next
