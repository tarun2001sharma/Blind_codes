from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        i = 0
        valid = set()

        if k == 1:
            return len(nums) >= 2

        while i < len(nums) - 1:
            start = i
            while i < len(nums) - 1 and nums[i + 1] > nums[i] and i - start + 1 < k:
                i += 1

            if i - start + 1 == k:
                # Check if there's an adjacent valid subarray
                if start in valid:
                    return True
                # Mark the end of this valid subarray
                valid.add(i + 1)
            
            # Move to the next potential starting point
            i = start + 1

        return False
