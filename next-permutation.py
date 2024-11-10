class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3,2,4,1     3,2,4,6
        # 3,4,1,2     3,2,6,4

        
        n = len(nums)

        # detect the first non-decreasing element
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # find number to swap with
        if i >= 0:
            # start searching from the most least element of the non-decreasing series
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse the whole series from i to the end of the ist
        x, y = i +1, n-1
        while x < y:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1
            y -= 1
        

