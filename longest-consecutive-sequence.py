class Solution:
    # O(n) time solution
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        numset = set(nums)
        tot = 1
        for i in nums:
            length = 1
            if (i-1) not in numset:
                start = i
                while (i + length) in numset:
                    length += 1
                tot = max(tot, length)
        return tot
