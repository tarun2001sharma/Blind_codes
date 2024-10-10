class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        totmax = max(nums)
        currmax, currmin = 1, 1

        for i in nums:
            # if not i:
            #     currmax, currmin = 1, 1
            #     continue
            temp = i * currmax
            currmax = max(currmax * i, currmin * i, i)
            currmin = min(temp, currmin * i, i)
            totmax = max(totmax, currmax)
        
        return totmax
