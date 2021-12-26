from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        size = len(prices)
        if k == 0:
            return 0
        elif k >= size // 2:
            result = 0
            for i in range(1, size):
                result += max(0, prices[i] - prices[i - 1])
            return result

        dp = [[0] * size for _ in range(k + 1)]
        for i in range(1, k + 1):
            maxProfitBuy = -prices[0]
            for j in range(1, size):
                dp[i][j] = max(dp[i][j - 1], maxProfitBuy + prices[j])
                maxProfitBuy = max(maxProfitBuy, dp[i - 1][j - 1] - prices[j])

        return dp[k][size - 1]


