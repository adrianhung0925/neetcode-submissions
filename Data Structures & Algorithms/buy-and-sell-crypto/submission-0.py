class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_profit = 0
        for n in prices:
            if n < min_price:
                min_price = n
            if n - min_price > max_profit:
                max_profit = n - min_price
        return max_profit