from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        color2Size = {}
        color = 2
        result = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    color2Size[color] = self.paintIsland(grid, i, j, color)
                    color += 1

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    usedColor = set()
                    candidate = 1
                    for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0 <= x + i < m and 0 <= y + j < n and grid[x + i][y + j] > 1 \
                                          and grid[x + i][y + j] not in usedColor:
                            usedColor.add(grid[x + i][y + j])
                            candidate += color2Size[grid[x + i][y + j]]
                    result = max(result, candidate)

        return result if result else m * n


    def paintIsland(self, grid, x, y, color):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        if grid[x][y] == 1:
            size = 1
            grid[x][y] = color
            for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
                size += self.paintIsland(grid, x + i, y + j, color)
            return size

        return 0


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,0],[1,1]]
    print(sol.largestIsland(grid))

