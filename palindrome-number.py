class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            temp = str(x)[1:][::-1]
            return x == int(temp)
        else:
            temp = str(x)[::-1]
            return x == int(temp)
        
