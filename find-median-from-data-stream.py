class MedianFinder:

    def __init__(self):
        '''
        We are going to maintain two heaps - Small heap (Max Heap) and Large Heap (Min Heap)

        '''
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        '''
        By default add the incoming number to small heap
        After this, check if the
        Root (small heap) <= Root (large heap)
        '''

        # In Python, for Max Heap, we need to reverse the postive numbers to negative
        heapq.heappush(self.small, -1*num)

        if (self.small and self.large):
            # val = self.small.heappop()
            if -1*self.small[0] > self.large[0]:
                val = -1*heapq.heappop(self.small)
                heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*val)   
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)       

    def findMedian(self) -> float:
        # if len(small) == len(large): average of their roots
        # else: root of small heap

        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        else:
            return -self.small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
