class Solution:
    def trap(self, height: List[int]) -> int:

        # Minimum(left, right) - height[i]
        # left and right pointers from two ends

        l, r = 0, len(height) - 1

        leftmax = height[l]
        rightmax = height[r]

        trap = 0

        while l < r:
            if leftmax <= rightmax:
                l += 1
                if height[l] > leftmax:
                    leftmax = height[l]
                else:
                    diff = leftmax - height[l]
                    trap += diff
            else:
                r -= 1
                if height[r] > rightmax:
                    rightmax = height[r]
                else:
                    diff = rightmax - height[r]
                    trap += diff 
        
        return trap


        # stack = []
        # store = 0

        # for i in range(len(height)):
        #     if height[i] < stack[-1]:
        #         stack.append((height[i], i))
        #     elif  height[i] == stack[-1]:
        #         stack.pop()
        #         stack.append((height[i], i))
        #     elif height[i] > stack[-1]:
        #         while height[i] > stack[-1]:
        #             stack.pop()
                  
