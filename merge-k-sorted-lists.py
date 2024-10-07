# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        This is not the most optimal solution but a brute-force solution.
        This is O(N.K) time complexity solution, however a O(N.logK) solution also exists.
        '''
        # k = len(lists)

        # head = ListNode()
        # curr = head

        # while curr:
        #     mini = None
        #     mini_idx = -1

        #     for i in range(k):
        #         if lists[i] and (mini is None or lists[i].val < mini.val):
        #             mini = lists[i]
        #             mini_idx = i
            
        #     # If no more nodes are left in all the lists, we are done
        #     if mini_idx == -1:
        #         break
             
        #     # Link the smallest node to the current node in the result list
        #     curr.next = mini
        #     curr = curr.next

        #     # Move the pointer forward in the list from which the smallest node was taken
        #     lists[mini_idx] = lists[mini_idx].next
        
        # return head.next

        '''
        This is the most optimal approach (below). It is O(N.logK) time complexity
        Even in this we can solve in two approaches:
        1. Merge Sort
        2. Heap
        '''

        # Maintain a min heap
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        head = ListNode()
        curr = head

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return head.next





        
