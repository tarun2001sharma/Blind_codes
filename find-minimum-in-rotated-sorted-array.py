class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1,2,4,5,6,7,0]
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l<=r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res
            
            m = (l + r)//2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m
        return res
        
