# class Solution:
#     # def twoSum(self, nums: List[int], total: int) -> List[List[int]]:

#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = set()
#         numset = {}
#         for idx in range(len(nums)):
#             numset[nums[idx]] = idx
#         for i in range(len(nums)):
#             twosum = -nums[i]
#             for j in range(i+1, len(nums)):
#                 check = -nums[i] -nums[j]
#                 if check in numset.keys() and numset[check]!= i and numset[check]!= j:
#                     ans.add(tuple(sorted([nums[i], nums[j], check])))
        
#         return list(ans)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip duplicates for the first element
                continue
                
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res

            
        
