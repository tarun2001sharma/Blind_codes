class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a DP table of size (len(text1)+1) x (len(text2)+1)
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Fill the DP table
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    # If characters match, take the diagonal value and add 1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # Else take the maximum from the top or left cell
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # The bottom-right corner of the DP table contains the result
        return dp[len(text1)][len(text2)]
