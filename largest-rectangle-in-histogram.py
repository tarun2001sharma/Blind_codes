class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        In this approach we will solve the problem by storing the each block and its corresponding start position in a STACK data structure 
        O(N) solution
        '''

        stack = [] # pair: (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                area = (i - idx)*height
                maxArea = max(maxArea, area)
                start = idx
            stack.append((start, h))

        if stack:
            for i,h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

# class Solution:
#     '''
#     Naive approach - O(N2) solution
#     '''
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         max_area = 0
#         for i in range(len(heights)):
#             min_height = inf
#             for j in range(i, len(heights)):
#                 min_height = min(min_height, heights[j])
#                 max_area = max(max_area, min_height * (j - i + 1))
#         return max_area
            

        
