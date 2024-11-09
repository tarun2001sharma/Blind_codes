class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node):
            if not node:
                return 0
            # Recursively find the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update the maximum diameter found so far
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)
        
        # Call the helper function with the root
        height(root)
        
        # The maximum diameter found
        return self.max_diameter
