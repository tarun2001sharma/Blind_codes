from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''BFS Method
        '''

        if not grid:
            return 0
        
        row = len(grid)
        col = len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            queue = deque()
            queue.append((r,c))
            grid[r][c] = '0'

            while queue:
                curr_x, curr_y = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = curr_x + dr, curr_y + dc

                    if new_r >= 0 and new_c >= 0 and new_r < row and new_c < col and grid[new_r][new_c] == '1':
                        queue.append((new_r, new_c))
                        grid[new_r][new_c] = '0'
        
        islands = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1
        
        return islands

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     '''
    #     Time Complexity:
    #     O(m * n), where m is the number of rows and n is the number of columns in the grid. Each cell is visited at most once.
    #     Space Complexity:
    #     O(m * n) in the worst case due to the recursion stack, where m is the number of rows and n is the number of columns.
    #     '''

    #     # This problem is similar to finding the number of connected components in a graph
    #     if not grid: return 0

    #     row = len(grid)
    #     col = len(grid[0])

    #     def dfs(i, j):
    #         if i < 0 or j < 0 or i >= row or j >= col:
    #             return
    #         if int(grid[i][j]) <= 0:
    #             return 
            
    #         grid[i][j] = '-1'
            
    #         dfs(i + 1, j)
    #         dfs(i, j + 1)
    #         dfs(i - 1, j)
    #         dfs(i, j - 1)
        
    #     counter = 0

    #     for i in range(row):
    #         for j in range(col):
    #             if grid[i][j] == '1':
    #                 counter += 1
    #                 dfs(i, j)
        
    #     return counter
        
