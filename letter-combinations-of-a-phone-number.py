class Solution:
    '''
    O(3^n * 4^m), where:
    n is the number of digits that map to 3 letters (2, 3, 4, 5, 6, 8).
    m is the number of digits that map to 4 letters (7, 9).
    This is because, for each digit, we explore multiple branches, and the total combinations grow exponentially with the number of digits.
    Space Complexity:
    O(n) for the recursion call stack, where n is the number of digits.

    '''
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return ''

        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append(''.join(path))
                return
            
            pos = phone_map[digits[index]]
            
            for letter in pos:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
        
        backtrack(0, [])
        return res
        
