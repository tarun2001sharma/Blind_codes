# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []

        curr = root
        queue.append(curr)
        ans = []

        
        while queue:
            level = []
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                # level.append(curr)
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:
                ans.append(level)
        
        return ans


        
