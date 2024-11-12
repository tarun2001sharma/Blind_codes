from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Handle edge case for very short arrays
        if n < 2:
            return 0  # Not enough elements to form two adjacent subarrays
        
        # Special case: if there are only two elements and they are increasing
        if n == 2 and nums[1] > nums[0]:
            return 1
        
        curr = 1  # Length of the current strictly increasing subarray
        pre_max = 0  # Length of the previous strictly increasing subarray
        max_k = 0  # Maximum length of adjacent increasing subarrays
        abs_max = 0  # Longest increasing subarray length found

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                # Update absolute max for any increasing subarray found
                abs_max = max(abs_max, curr)
                
                # Check for adjacent increasing subarrays
                if pre_max > 0:
                    max_k = max(max_k, min(pre_max, curr))
                
                # Move current increasing subarray length to pre_max
                pre_max = curr
                curr = 1  # Reset for the next sequence

        # Final check after the loop to consider the last sequence
        abs_max = max(abs_max, curr)
        if pre_max > 0:
            max_k = max(max_k, min(pre_max, curr))

        # Final adjustment: if abs_max // 2 is greater than max_k, return it
        return max(max_k, abs_max // 2)
