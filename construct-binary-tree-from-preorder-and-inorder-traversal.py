# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        Time Complexity: O(n) (where n is the number of nodes).
        Space Complexity: O(n) in both the best and worst cases, but the recursion stack space can vary between O(log n) and O(n) depending on the balance of the tree.
        '''
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] =  idx
        
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = helper(pre_left + 1, pre_left + mid - in_left, in_left, mid - 1)
            root.right = helper(pre_left + mid - in_left + 1, pre_right, mid + 1, in_right)
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

        
