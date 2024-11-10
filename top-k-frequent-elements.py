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
        # # 1st Solution
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
        
        for num, freq in counter.items():
            freq_bucket[freq].append(num)
        
        ans = []
        freq_bucket= freq_bucket[::-1] #reverse the array
        for i in range(k):
            for j in freq_bucket[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

    '''
    Using Quick- Select
    '''
    import random

    def partition(nums, left, right, pivot_idx):
        pivot_freq = nums[pivot_idx][1]

        # move the pivot to the end of the array
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        store_idx = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_idx], arr[i] = arr[i], arr[store_idx]
                store_idx += 1
        
        arr[right], arr[store_idx] = arr[store_idx], arr[right]
        return store_idx

    def quickselect(nums, left, right, k):
        '''
        select the k-th largest element in nums within left..right
        '''

        if left == right:
            return
        
        pivot_idx = random.rantint(left, right)

        # Find the pivot position in left and right sorted arrangement
        pivot_idx = partition(nums, left, right, pivot_idx)

        if pivot_idx == k:
            return
        
        elif pivot_idx < k:
            quickselect(nums, pivot_idx + 1, right, k)
        else:
            quickselect(nums, left, pivot_idx - 1, k)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        freq_list = list(freq.items)  #(element, frequency) pairs

        n = len(freq_list)
        quickselect(freq_list, 0, n-1, n-k)

        return [ele for ele, frew in freq_list[n-k:]]


        
        
        
