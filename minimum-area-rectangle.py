class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_size = float('inf')
        visited = set()

        for coordinates in points:
            x1 = coordinates[0]
            y1 = coordinates[1]

            for pt in visited:
                x2, y2 = pt[0], pt[1]
                if (x1, y2) in visited and (x2, y1) in visited:
                    area = abs(x1-x2) * abs(y1-y2)
                    min_size = min(min_size, area)
            
            visited.add((x1, y1))
        
        if min_size == float('inf'):
            return 0
        return min_size


        
