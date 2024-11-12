# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            
            if not left or not right:
                return False

            if left.val != right.val:
                return False
            
            
            temp1 = dfs(left.left, right.right)
            temp2 = dfs(left.right, right.left)

            if temp1 and temp2:
                return True
            else:
                return False
        
        ans = dfs(root.left, root.right)
        return ans

        
