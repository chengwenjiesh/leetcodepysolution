from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        total_profit = 0

        for i in range(1, len(prices)):
            total_profit += max(prices[i] - prices[i - 1], 0)

        return total_profit
        '''
        if len(prices) < 2:
            return 0

        buy, sell = float('-inf'), 0
        for price in prices:
            b, s = buy, sell
            buy = max(b, s - price)
            sell = max(s, b + price)
        return sell


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,5,4,3,2,1]))
