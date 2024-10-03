class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        track = set()
        for i in nums:
            if i in track:
                return i
            else:
                track.add(i)
        return -1
        
