class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: if the array is empty or contains one element, no profit can be made
        if not prices or len(prices) == 1:
            return 0
        
        min_price = float('inf')  # Initialize to a very large number
        max_profit = 0  # Initialize profit to 0
        
        for price in prices:
            # Update the minimum price so far
            min_price = min(min_price, price)
            # Calculate the potential profit with the current price
            profit = price - min_price
            # Update the maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit
