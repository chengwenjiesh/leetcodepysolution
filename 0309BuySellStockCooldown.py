from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # buy sell wait -> what's the max profit if doing this at i
        buy, sell, wait = float('-inf'), 0, 0
        for price in prices:
            b, s, w = buy, sell, wait
            wait = max(b, s, w)
            buy = max(b, w - price)
            sell = max(s, b + price)

        return max(wait, sell)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1,2,3,4,0,2]))

