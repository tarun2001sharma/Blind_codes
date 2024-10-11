class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        if not nums:
            return curr_sum

        maxSum = -float(inf)
        
        for i in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            maxSum = max(maxSum, curr_sum)
        return maxSum

        
