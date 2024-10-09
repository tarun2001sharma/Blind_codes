class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Time Complexity:
        O(m * n), where m is the number of rows and n is the number of columns in the grid. Each cell is visited at most once.
        Space Complexity:
        O(m * n) in the worst case due to the recursion stack, where m is the number of rows and n is the number of columns.
        '''
        if not grid: return 0

        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return
            if int(grid[i][j]) <= 0:
                return 
            
            grid[i][j] = '-1'
            
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
        
        counter = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    counter += 1
                    dfs(i, j)
        
        return counter
        
