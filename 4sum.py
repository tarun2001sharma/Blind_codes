class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # def kSum(self, nums, target, k):
            # res = []
        nums.sort()
        return self.kSumRecursive(nums, target, 4, 0)
        
    def kSumRecursive(self, nums, target, k, start):
        res = []

        if k == 2:
            left, right = start, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < target:
                    left += 1
                else:
                    right -= 1
            return res
        
        # recursive calls to reduce k-sum to (k - 1)-sum
        for i in range(start, len(nums) - k + 1):
            # skip duplicates
            if i > start and nums[i] == nums[i-1]:
                continue
            for subset in self.kSumRecursive(nums, target - nums[i], k-1, i+1):
                res.append([nums[i]] + subset)
        
        return res
                        


        
