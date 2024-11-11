class Solution:

    def __init__(self, w: List[int]):
        # compute cumulative weight
        self.cumulative = []
        temp_w = 0
        for weight in w:
            temp_w += weight
            self.cumulative.append(temp_w)
        self.total_weight = temp_w
        

    def pickIndex(self) -> int:

        target = random.uniform(0, self.total_weight)

        # implement binary search to reach ot the target index
        left, right =  0, len(self.cumulative) - 1
        while left < right:
            mid = (left + right)//2
            if target < self.cumulative[mid]:
                right = mid
            else:
                left = mid + 1
        
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
