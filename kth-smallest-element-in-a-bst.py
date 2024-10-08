# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Since it is a BST, its already in order. For such a problem we can't go above O(n) solution.
        We will use the concept of stack to keep track of the node visited, and pop out the smallest element each time. By this procedure we should get the k-th smallest element  in 
        The time complexity is O(H + k), where H is the height of the tree. In the worst case, this is O(n), where n is the number of nodes (for a completely unbalanced tree).

        '''
        stack = []
        curr = root
        count = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count += 1

            if count == k:
                return curr.val
            
            curr = curr.right

        # stack = []
        # stack.append(root)
        # curr = 0
        # target = None

        # while True:
        #     node = stack[-1]
        #     if node.left:
        #         stack.append(node.left)
        #     else:
        #         temp = stack.pop()
        #         curr += 1
        #         if curr == k:
        #             target = temp
        #             break
        #         stack.append(node.right)
        
        # return target.val

        
