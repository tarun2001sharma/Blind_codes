class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        def myPowRecur(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            if n%2 == 0:
                return myPowRecur(x*x, n//2)
            else:
                return x * myPowRecur(x*x, n//2)
        
        ans = myPowRecur(x, abs(n))
        return ans if n>=0 else 1/ans
        
