class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[m - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(3,7))

