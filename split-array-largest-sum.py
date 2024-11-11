class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def min_subarrays(max_sum):
            curr_sum = 0
            splits = 0

            for element in nums:
                if curr_sum + element <= max_sum:
                    curr_sum += element
                else:
                    curr_sum = element
                    splits += 1
            return splits + 1

        left = max(nums)
        right = sum(nums)

        while left<= right:
            mid = (left + right)//2

            if min_subarrays(mid) <= k:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        
        return ans
        
