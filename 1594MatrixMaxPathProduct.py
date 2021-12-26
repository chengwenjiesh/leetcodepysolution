from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        minProduct = grid[:]
        maxProduct = grid[:]
        for i in range(1, m):
            minProduct[i][0] = maxProduct[i][0] = grid[i][0] * minProduct[i - 1][0]
        for j in range(1, n):
            minProduct[0][j] = maxProduct[0][j] = grid[0][j] * minProduct[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                maxUp = maxProduct[i - 1][j]
                maxLeft = maxProduct[i][j - 1]
                minUp = minProduct[i - 1][j]
                minLeft = minProduct[i][j - 1]

                minProduct[i][j] = min(grid[i][j] * maxUp, \
                                           grid[i][j] * minUp, \
                                           grid[i][j] * maxLeft, \
                                           grid[i][j] * minLeft)
                maxProduct[i][j] = max(grid[i][j] * maxUp, \
                                           grid[i][j] * minUp, \
                                           grid[i][j] * maxLeft, \
                                           grid[i][j] * minLeft)
        return -1 if maxProduct[m - 1][n - 1] < 0 else maxProduct[m - 1][n - 1] % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    grid = [[-1,-2,1],[1,-2,1],[3,-4,1]]
    print(sol.maxProductPath(grid))

