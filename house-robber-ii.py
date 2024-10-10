class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper_rob(nums, idx):
            rob1 , rob2 = 0, 0
            for i in range(idx, len(nums)+idx-1):
                temp = max(nums[i] + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        if len(nums) == 1:
            return nums[0]
        
        res = max(helper_rob(nums, 0), helper_rob(nums, 1))
        return res
        
