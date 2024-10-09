# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once to calculate its contribution to the path sum.

        Space Complexity: O(h), where h is the height of the tree. This is the space used by the recursion stack. In the worst case (for a skewed tree), the recursion stack will have depth equal to the number of nodes, i.e., O(n). In the best case (balanced tree), the height of the tree will be O(log n).
        '''

        self.maxSum = -float('inf')

        def findMaxPath(node):
            if not node:
                return 0
            
            left_gain = max(findMaxPath(node.left), 0)
            right_gain = max(findMaxPath(node.right), 0)

            curr = node.val + left_gain + right_gain

            self.maxSum = max(curr, self.maxSum)

            return max(left_gain, right_gain) + node.val
        
        findMaxPath(root)
        return self.maxSum
        
