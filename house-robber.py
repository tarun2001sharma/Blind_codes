# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         dp = [0] * 3
#         dp += nums
        
#         n= len(nums)

#         for i in range(3,n+3):
#             dp[i] += max(dp[i-2], dp[i-3])
        
#         # print(dp)
#         return max(dp[n+1], dp[n+2])

class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there is only one house, return its value
        if len(nums) == 1:
            return nums[0]
        
        # If there are two houses, return the maximum of the two
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Initialize the previous two houses' results
        prev2 = nums[0]  # Max money robbed up to house 0
        prev1 = max(nums[0], nums[1])  # Max money robbed up to house 1

        # Iterate from the third house to the last one
        for i in range(2, len(nums)):
            current = max(prev1, nums[i] + prev2)  # Rob current or skip it
            prev2 = prev1  # Update prev2 to the value of prev1
            prev1 = current  # Update prev1 to the current value

        # The final result is stored in prev1
        return prev1

        
