class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        fresh = 0
        time = 0

        row = len(grid)
        col = len(grid[0])

        dq = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    dq.append((i, j))
        
        while dq and fresh > 0:
            for _ in range(len(dq)):
                r, c = dq.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if (new_r < 0 or new_c < 0 or new_r >= row or new_c >= col or grid[new_r][new_c] != 1):
                        continue
                    grid[new_r][new_c] = 2
                    dq.append((new_r, new_c))
                    fresh -= 1
            time += 1
        
        if fresh > 0:
            return -1
        else:
            return time


        
