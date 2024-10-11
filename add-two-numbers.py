# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()  # Dummy head to make it easier to handle edge cases
        curr = head
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            # Get values from the current nodes or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            num = total % 10
            
            # Create a new node with the current digit
            curr.next = ListNode(num)
            curr = curr.next

            # Move to the next nodes in l1 and l2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next  # Return the next node since the head is a dummy node
