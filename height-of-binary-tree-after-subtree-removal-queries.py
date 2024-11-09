# from typing import Optional, List
# from heapq import heappush, heapreplace

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
#         ans = []
#         heights = {}
#         levels = {}
#         max_heights = {}  # To store max two heights for each level

#         # Calculate height of each node and maintain level information
#         def calculate_heights(node, depth):
#             if not node:
#                 return 0
#             left_height = calculate_heights(node.left, depth + 1)
#             right_height = calculate_heights(node.right, depth + 1)
#             height = 1 + max(left_height, right_height)
            
#             heights[node.val] = height
#             levels[node.val] = depth
            
#             # Maintain two highest heights for each level
#             if depth not in max_heights:
#                 max_heights[depth] = []
            
#             if len(max_heights[depth]) < 2:
#                 heappush(max_heights[depth], height)
#             elif height > max_heights[depth][0]:
#                 heapreplace(max_heights[depth], height)
            
#             return height

#         calculate_heights(root, 0)

#         # Process each query
#         for query in queries:
#             node_height = heights[query]
#             node_level = levels[query]

#             # Determine the height of the tree without this node's subtree
#             if len(max_heights[node_level]) == 2 and node_height == max_heights[node_level][1]:
#                 # Remove the highest subtree, use the second highest
#                 max_height = max_heights[node_level][0]
#             else:
#                 # Use the max height for the level if subtree was not removed
#                 max_height = max_heights[node_level][1] if max_heights[node_level] else 0
            
#             # Calculate the overall height of the tree after removal
#             remaining_tree_height = max(max_height, heights[root.val] - node_height)
#             ans.append(remaining_tree_height)

#         return ans

from typing import List, Tuple, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find_height(self, curr: Optional[TreeNode], level: int, node_level: List[int], node_height: List[int], top2_height: List[Tuple[int, int]]) -> int:
        if not curr:
            return 0

        # Recursively find heights of left and right subtrees
        height = 1 + max(
            self.find_height(curr.left, level + 1, node_level, node_height, top2_height),
            self.find_height(curr.right, level + 1, node_level, node_height, top2_height)
        )

        # Store the node's level and height
        node_level[curr.val] = level
        node_height[curr.val] = height

        # Maintain only the top 2 heights at each level
        if height > top2_height[level][0]:
            top2_height[level] = (height, top2_height[level][0])
        elif height > top2_height[level][1]:
            top2_height[level] = (top2_height[level][0], height)

        return height

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        n = 100001  # Assumes node values range from 1 to 100000
        node_level = [-1] * n  # Stores level of each node
        node_height = [-1] * n  # Stores height of each node
        top2_height = [(0, 0)] * n  # Top-2 heights at each level {maxHeight, secondMaxHeight}

        # Compute the height for each node starting from the root
        self.find_height(root, 0, node_level, node_height, top2_height)

        res = []
        for query_node in queries:
            level = node_level[query_node]
            height = node_height[query_node]

            # Determine the result based on whether the query_node is the tallest at that level
            max_height = top2_height[level][1] if top2_height[level][0] == height else top2_height[level][0]
            res.append(max_height + level - 1)

        return res

