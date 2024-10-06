class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            # Check if the middle element is the target
            if nums[m] == target:
                return m

            # Check if the left half is sorted
            if nums[l] <= nums[m]:
                # Check if target is in the left half
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Narrow down to the left half
                else:
                    l = m + 1  # Narrow down to the right half

            # Otherwise, the right half must be sorted
            else:
                # Check if target is in the right half
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Narrow down to the right half
                else:
                    r = m - 1  # Narrow down to the left half

        # Target not found
        return -1
