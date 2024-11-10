class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader, writer = 0, 0

        while reader < len(nums):
            if nums[reader] == val:
                reader += 1
            else:
                nums[writer] = nums[reader]
                reader += 1
                writer += 1
        
        return writer
        
