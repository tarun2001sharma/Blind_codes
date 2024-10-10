# class Solution:
#     def numDecodings(self, s: str) -> int:
#         # 1234
#         # - ABCD, LCD, AWD

#         # 12 AB, L
#         # 33 CC

#         # 102
#         # - JB

#         if s[0] == '0':
#             return 0

#         dp = [0]*len(s)
#         dp[0] = 1

#         for i in range(1, len(s)):
#             if s[i] == '0':
#                 if s[i-1] == '0':
#                     return 0
#                 if s[i-1] == '1' or s[i-1] == '2':
#                     dp[i] = dp[i-1]
#             elif 0 < int(s[i]) < 7 and s[i-1] == '2':
#                 dp[i] = dp[i-1] + 1
#             elif s[i-1] == '1':
#                 dp[i] = dp[i-1] + 1
#             else:
#                 dp[i] = dp[i-1]
        
#         # if s[-1] == '0':
#         #     if (s[-2] != '1' or s[-2] != '2'):
#         #         return 0
        
#         return dp[len(s)-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(s) + 1):
            # Check if the current single character is valid
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Check if the last two characters form a valid two-digit number
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]


            


            
        
