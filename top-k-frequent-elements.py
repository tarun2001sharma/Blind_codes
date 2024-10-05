class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Two solutions: 1. Heap (O(nlogk)) , 2. Bucket Sort (more efficient, O(n))
        '''

        # counter to counter the frequencies of each elements
        # O(n) time
        counter = {}
        for i in nums:
            counter[i] = 1 + counter.get(i, 0)
        
        #################################
        # 1st Solution
        heap = []

        '''
        Now there are two approaches here:
        1. Use Max heap that stores the frequencies in highest to lowest hierarchy. 
            --> Building Max heap = O(mlogm) ~ O(nlogn)
                here m = unique elements in num, m <= n
            --> Extracting top-k elements = O(klogm) ~ O(klogn)
            Total time complexity = O(mlogm) ~ O(nlogn)
        
        2. Use Min heap that stores top-k elements only. As soon as the heap size exceeds k, pop the minimum element (root node)
            --> Building the heap: O(n log k)
            --> Extracting the results: O(k log k)
            Total time complexity is O(n log k).
        '''
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap) # removes the lowest freq element
        
        return [num for freq, num in heap]

        ###########################
        # 2nd Solution
        # O(n) time complexity
        freq_bucket = []
        for _ in range(len(nums)+1):
            freq_bucket.append([])
        
        for num, freq in counter:
            freq_bucket[freq].append(num)
        
        ans = []
        freq= freq[::-1] #reverse the array
        for i in range(k):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

        
        
        
