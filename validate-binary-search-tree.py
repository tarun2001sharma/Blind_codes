# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        Time Complexity: O(n), where n is the number of nodes in the tree, because we visit each node exactly once.
        Space Complexity: O(h), where h is the height of the tree. In the worst  case (skewed tree), the space complexity is O(n) due to the recursion stack, but in the best case (balanced tree), it’s O(log n).
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, low =  float('-inf'), high = float('inf')) -> bool:
            if not root:
                return True
            if root.val >= high:
                return False
            if root.val <= low:
                return False
            return isValid(root.left, low, root.val) and isValid(root.right, root.val, high)
        
        return isValid(root)
        
