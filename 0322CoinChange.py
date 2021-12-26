from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    dp[num] = min(dp[num], dp[num - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.coinChange([1,2,5], 11))
