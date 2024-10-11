class Solution:
    '''
    - Dynamic Programming Solution (O(n2) time complexity)
    - Binary search solution (O(nlogn) solution)
    '''
   
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     def binary_search(sub, num):
    #         # Manually implementing binary search to find the index
    #         left, right = 0, len(sub) - 1
    #         while left <= right:
    #             mid = (left + right) // 2
    #             if sub[mid] < num:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #         return left
        
    #     sub = []  # This list will store the smallest possible tail values
        
    #     for num in nums:
    #         idx = binary_search(sub, num)  # Find where to place this number
            
    #         if idx == len(sub):
    #             sub.append(num)  # If num is larger than all elements, extend the list
    #         else:
    #             sub[idx] = num  # Otherwise, replace the element at the found index
        
    #     return len(sub)  # The length of the 'sub' list is the length of the LIS

    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * (len(nums))


        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        # print(LIS)
        return max(LIS)
        
