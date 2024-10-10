class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            for j in wordDict:
                if i + len(j) <= len(s) and s[i:i+len(j)] == j:
                    dp[i] = dp[i + len(j)]
                if dp[i] == 1:
                    break
        
        return dp[0]
    
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True  # Base case: an empty suffix is always segmentable
        
#         for i in range(len(s) - 1, -1, -1):
#             for w in wordDict:
#                 if i + len(w) <= len(s) and s[i:i + len(w)] == w:
#                     dp[i] = dp[i + len(w)]
#                 if dp[i]:  # If segmentation is possible, break early
#                     break
        
#         return dp[0]
