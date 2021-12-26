from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0

        buy, sell = float('-inf'), 0
        for price in prices:
            b, s = buy, sell
            buy = max(b, s - price)
            sell = max(s, b + price - fee)

        return sell


