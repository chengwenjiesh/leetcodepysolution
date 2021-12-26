from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if i > 0 or j > 0:
                    left = grid[i][j - 1] if j > 0 else float('inf')
                    up = grid[i - 1][j] if i > 0 else float('inf')
                    grid[i][j] = min(left, up) + grid[i][j]

        return grid[m - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
