class Solution:

    # Optimal Approach: O(n) time and O(1) space complexity
    # The minimum number of operations required is determined by the positive difference between each consecutive element in target. Each time we see a "rise" (an increase) in the values from target[i-1] to target[i], we would need an extra operation to cover that increase.
    def minNumberOperations(self, target: List[int]) -> int:
        # Initialize operations with the first element in the target array
        operations = target[0]
        
        # Traverse from the second element to the end
        for i in range(1, len(target)):
            # Only add the difference if current element is greater than the previous one
            if target[i] > target[i - 1]:
                operations += target[i] - target[i - 1]
        
        return operations

    '''
    The below is the naive solution which uses divide and conquer naively - O(n2) - O(n3) solution.
    '''
    # def minNumberOperations(self, target: List[int]) -> int:
        
    #     ans = 0

    #     def recur(initial):
    #         nonlocal ans  # Allow modification of ans in the outer function
    #         if not initial:  # Check if the list is empty
    #             return 0
    #         curr_min = min(initial)
    #         for i in range(len(initial)):
    #             initial[i] -= curr_min
            
    #         ans += curr_min
    #         x = 0
    #         y = 0
    #         while x < len(initial) and y < len(initial):
    #             if initial[y] == 0:
    #                 recur(initial[x:y])
    #                 x = y + 1
    #                 y = x
    #             else:
    #                 y += 1
    #         recur(initial[x:y])

    #         return curr_min
        
    #     recur(target)
    #     return ans  # Add a return statement to return the result of ans
