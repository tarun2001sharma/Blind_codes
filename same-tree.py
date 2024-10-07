# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Time Complexity:
        O(n) where n is the total number of nodes in the smaller tree (or both trees if they are identical). Each node is visited once.
        Space Complexity:
        O(h) where h is the height of the tree due to the recursive call stack. In the worst case (skewed tree), this could be O(n), but for a balanced tree, it would be O(log n).
        '''

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
