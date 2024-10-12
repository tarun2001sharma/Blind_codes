class Solution:
    #  the overall time complexity is O(logx)

    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        res = 0
        sign = -1 if x<0 else 1
        x = abs(x)

        while x!=0:
            digit = x % 10
            x = x // 10

            if (10 * res + digit) > INT_MAX:
                return 0
            res = res * 10 + digit
        
        return sign * res
        
