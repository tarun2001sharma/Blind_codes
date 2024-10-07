# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Time Complexity:
        O(n * m), where n is the number of nodes in the root tree and m is the number of nodes in the subRoot tree. In the worst case, for each node in root, we perform an O(m) comparison with the subRoot tree using isSame.
Space Complexity:
        O(h1 + h2), where h1 is the height of the root tree and h2 is the height of the subRoot tree. This accounts for the recursion stack in both the isSubtree and isSame recursive calls.
        '''
        if not root:
            return False

        if root.val == subRoot.val:
            check = self.isSame(root, subRoot)
            if check:
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


        
