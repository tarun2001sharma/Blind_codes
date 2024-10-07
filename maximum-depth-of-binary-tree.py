# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Time Complexity:
        O(n), where n is the number of nodes in the tree. We visit each node once.
        Space Complexity:
        O(h), where h is the height of the tree. In the worst case (skewed tree), the height could be O(n), but for a balanced tree, it would be O(log n)
        '''
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

        from collections import deque


'''
The below solution is just the BFS solution with O(n) time and space complexity. Just for practice and non-recursive approach
'''
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         # Initialize a queue for BFS
#         queue = deque([root])
#         depth = 0
        
#         # Perform BFS
#         while queue:
#             depth += 1
#             # Process all nodes at the current level
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 # Add the children of the current node to the queue
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
        
#         return depth
        
