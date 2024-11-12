class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        cache = {}

        def dfs(r,c):
            if r == rows or c == cols:
                return 0
            if matrix[r][c] == 0:
                return 0

            if (r,c) in cache:
                return cache[(r,c)]
            
            cache[(r,c)] = 1 + min(dfs(r+1, c), dfs(r, c+1), dfs(r+1, c+1))

            return cache[(r,c)]
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res+= dfs(r,c)
        return res


        

# from typing import List
# import copy

# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         dp = copy.deepcopy(matrix)
#         row = len(dp)
#         col = len(dp[0])

#         for i in range(1, row):
#             for j in range(1, col):
#                 if matrix[i][j] == 1:
#                     dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

#         # Sum up all elements in dp to get the total count of square submatrices with all ones
#         return sum(sum(row) for row in dp)
