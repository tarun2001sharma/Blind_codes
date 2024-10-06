class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in brackets.keys():
                if stack:
                    prior = stack.pop()
                    if prior != brackets[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True
        
