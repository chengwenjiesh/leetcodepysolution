class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not len(s) or not len(t):
            return 0

        m, n = len(s), len(t)
        # dp[i][j] means how many way to form t[0:i] in s[0:j]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[n][m]


