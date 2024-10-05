class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        answer = [1] * n  # Initialize answer array with 1s

        # Left pass: Calculate the product of elements to the left of each element
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Right pass: Calculate the product of elements to the right of each element
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


        # prod = 1
        # cnt = 0
        # for num in nums:
        #     if num == 0:
        #         cnt += 1
        #     else:
        #         prod = prod * num
        # if cnt > 1:
        #     prod = 0

        # print(prod)
        
        # ans = []
        # for num in nums:
        #     if num == 0:
        #         ans.append(prod)
        #     elif cnt > 0:
        #         ans.append(0)
        #     else:
        #         ans.append(int(prod/num))
        
        # return ans

        
