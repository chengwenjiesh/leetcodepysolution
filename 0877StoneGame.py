from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # pile should at lease be size 1
        sz = len(piles)
        dp = [[0] * sz for _ in range(sz)]

        for i in range(sz - 1, -1, -1):
            dp[i][i] = piles[i]
            for j in range(i + 1, sz):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[0][sz - 1] > 0

if __name__ == '__main__':
    print(Solution().stoneGame([1,2,3,4,5,7]))

