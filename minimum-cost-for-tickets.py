class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(i):
            # runs in O(38 * n)
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = float('inf')

            for d,c in zip([1,7,30], costs):
                j = i 
                # we have to reach to the day where-in our pass expires
                # and get the index to be inculcated with the DP array
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            
            return dp[i]
        
        return dfs(0)
        

        
