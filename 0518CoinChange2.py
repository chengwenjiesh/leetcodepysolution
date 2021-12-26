from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]

        return dp[amount]


    def change2d(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j] + (0 if j < coins[i] else dp[i][j - coins[i]])

        return dp[-1][amount]


if __name__ == '__main__':
    sol = Solution()
    print(sol.change(5, [1,2,5]))


