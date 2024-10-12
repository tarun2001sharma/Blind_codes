class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # [1,2,3]
        # [2,1,3] | 1 <-> 2
        # -> [2,3,1] | 1 <-> 3
        # [3,2,1] 1 <-> 3
        # [1,3,2] 2 <-> 3

        ans = []
        idx = 0

        def backtrack(idx):
            if idx == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        backtrack(idx)
        return ans


            
