from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices has at least length 1
        lowest_price_hist = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - lowest_price_hist)
            if price < lowest_price_hist:
                lowest_price_hist = price

        return max_profit


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([6,5,4,3,2]))
