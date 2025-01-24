from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if currentProfit > 0:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit