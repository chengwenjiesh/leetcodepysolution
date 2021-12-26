class Solution:
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxSquare = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if not i or not j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

                maxSquare = max(maxSquare, dp[i][j])

        return maxSquare ** 2


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
