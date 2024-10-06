class Solution:
    # O(n) solution
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        container = 0
        while l<r:
            area = (r - l) * min(height[l], height[r])
            container = max(container, area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return container


        
