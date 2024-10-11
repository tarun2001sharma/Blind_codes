class Solution:
    '''
    Again two solutions:
    - Dynamic Programming solution (O(MxN) time complexity, O(MxN) space complexity)
    - Combinatorial appraoch:
    The number of horizontal moves to do is h=m−1, the number of vertical
moves is v=n−1. That results in a simple formula C^{h}_{h+v} = (m+n−2)!/(m−1)!(n−1)!
     O((M+N)(log(M+N)loglog(M+N))^2) time complexity and O(1) space complexity

    '''
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                temp1 = dp[i-1][j] if i-1>=0 else 0
                temp2 = dp[i][j-1] if j-1>=0 else 0
                dp[i][j] = max(dp[i][j], temp1 + temp2)
        
        return dp[m-1][n-1]
    
        # def uniquePaths(self, m: int, n: int) -> int:
        # return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)
        
