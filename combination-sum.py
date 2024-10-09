class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(temp, curr_sum, start):
            # If the current sum matches the target, add the combination to the answer
            if curr_sum == target:
                ans.append(list(temp))
                return
            
            # If the current sum exceeds the target, we stop exploring this path
            if curr_sum > target:
                return
            
            # Iterate over the candidates starting from the 'start' index
            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                # Recursive call with updated sum and starting index 'i' (allowing same element again)
                backtrack(temp, curr_sum + candidates[i], i)
                temp.pop()  # Backtrack and explore other possibilities
        
        # Initial call to the backtrack function with an empty list, sum 0, and start index 0
        backtrack([], 0, 0)

        return ans
