class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nxt = nums[0]
        if len(nums) == 1:
            return True
        curr = nxt

        for i in range(1, len(nums)):
            if i > nxt:
                return False
            if nums[i] + i >= nxt:
                nxt = nums[i] + i
            if nxt >= len(nums) - 1:
                return True
        return False 
        
