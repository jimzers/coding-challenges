class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        just grab every upward slope
        """
        total_profit = 0
        curr_hold = prices[0]

        for num in prices[1:]:
            if num > curr_hold:
                total_profit += num - curr_hold
            curr_hold = num
        return total_profit
