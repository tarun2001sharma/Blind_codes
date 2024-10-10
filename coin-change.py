class Solution:
    '''
    Time Complexity:
    Time Complexity: O(n * m), where n is the amount and m is the number of coins.
    We iterate over each amount from 1 to n (outer loop), and for each amount, we check each coin (inner loop). Thus, the time complexity is proportional to the product of the amount and the number of coins.

    Space Complexity:
    Space Complexity: O(n), where n is the amount.
    We use a one-dimensional DP array of size amount + 1 to store the minimum number of coins required for each amount.
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i-j] + 1, dp[i])
        
        if dp[amount] == amount + 1:
            return -1
        else: return dp[amount]
        
