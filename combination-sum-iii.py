class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, current_combination, current_sum):
            # Base case: if the combination has exactly k numbers and the sum is n
            if len(current_combination) == k and current_sum == n:
                result.append(list(current_combination))
                return
            
            # If the combination size exceeds k or sum exceeds n, prune the path
            if len(current_combination) > k or current_sum > n:
                return
            
            # Try adding numbers from 'start' to 9
            for num in range(start, 10):
                current_combination.append(num)
                backtrack(num + 1, current_combination, current_sum + num)
                current_combination.pop()  # Backtrack to explore another number
                
        # Start backtracking from 1
        backtrack(1, [], 0)
        return result
