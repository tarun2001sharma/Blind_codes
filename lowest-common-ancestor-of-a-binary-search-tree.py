# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Time Complexity:
        Best case (Balanced BST): O(log n)
        Worst case (Skewed BST): O(n)
        Space Complexity: O(1) (Iterative, constant space).

        '''
        
        curr = root

        while curr:
            if p.val>curr.val and q.val>curr.val:
                curr = curr.right
            elif p.val<curr.val and q.val<curr.val:
                curr = curr.left
            else:
                return curr
        
