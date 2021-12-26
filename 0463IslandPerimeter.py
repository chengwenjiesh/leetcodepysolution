from typing import List

class Solution:
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        island = neighbor = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    island += 1
                    if i + 1 < m and grid[i + 1][j] == 1:
                        neighbor += 1
                    if j + 1 < n and grid[i][j + 1] == 1:
                        neighbor += 1

        return 4 * island - 2 * neighbor

    def islandPerimeter(self, grid):
        cnt = 0

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if x + i < 0 or y + j < 0 or x + i >= m or y + j >= n \
                                                  or grid[x + i][y + j] == 0:
                            cnt += 1
        return cnt


