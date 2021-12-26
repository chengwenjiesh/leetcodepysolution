from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for p in prices:
            b1, s1, b2, s2 = buy1, sell1, buy2, sell2
            buy1 = max(b1, 0 - p)
            sell1 = max(s1, b1 + p)
            buy2 = max(b2, s1 - p)
            sell2 = max(s2, b2 + p)

        return max(sell1, sell2)

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([1,2,3,6,0,4,1,2]))

