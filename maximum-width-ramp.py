class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [-1]*n

        right_max[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(nums[i], right_max[i + 1])
        
        l, r = 0, 0
        max_width = 0

        while r < n:
            while l < r and nums[l] > right_max[r]:
                l += 1
            max_width = max(max_width, r - l)
            r += 1
        
        return max_width
