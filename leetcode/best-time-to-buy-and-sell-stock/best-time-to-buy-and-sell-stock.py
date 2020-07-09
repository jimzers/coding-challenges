class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float('inf')
        max_profit = 0
        for num in prices:
            if num < lowest_price:
                lowest_price = num
            else:
                max_profit = max(max_profit, num - lowest_price)

        return max_profit
