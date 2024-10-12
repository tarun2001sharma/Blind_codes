class Solution:
    '''
    Time Complexity:
    The time complexity is O(4^n / √n). This is related to the Catalan number, which represents the number of valid parentheses combinations.
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return 
            # (())()
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result
