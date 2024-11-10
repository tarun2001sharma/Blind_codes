class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r < 0 or r > row-1 or c < 0 or c > col-1:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            n = dfs(r + 1, c)
            w = dfs(r, c - 1)
            e = dfs(r, c + 1)
            s = dfs(r - 1, c)

            return 1 + n + w + e + s
        
        max_area = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area
            
        
