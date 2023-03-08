# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, prices[0]

        for price in prices:
            profit = max(profit, (price-min_price))
            min_price = min(min_price, prices)

        return profit
