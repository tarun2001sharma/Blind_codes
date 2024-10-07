# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Time Complexity:
    O(n): We visit each node once, where n is the number of nodes in the tree.
        
        Space Complexity:
        O(h), where h is the height of the tree. In the worst case, if the tree is completely unbalanced, the recursion depth could be O(n), but in a balanced tree, it will be O(log n).
        '''
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        #recursively call the inverse subtree function to each children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
