class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for price in prices[1:] :
            profit = price - buy_price
            max_profit = max(max_profit,profit)
            buy_price = min(buy_price,price)
        return max_profit