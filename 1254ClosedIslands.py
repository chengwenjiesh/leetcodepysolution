from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # Interview with Ben Awad video?
        if not grid or not grid[0]:
            return 0

        m ,n = len(grid), len(grid[0])
        for i, j in [(i, 0) for i in range(m)] + \
                    [(i, n - 1) for i in range(m)] + \
                    [(0, j) for j in range(n)] + \
                    [(m - 1, j) for j in range(n)]:
            if grid[i][j] == 0:
                self.removeIsland(grid, i, j)

        closedIsland = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    closedIsland += 1
                    self.removeIsland(grid, i, j)

        return closedIsland

    def removeIsland(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 1:
            return

        grid[x][y] = 1
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            self.removeIsland(grid, x + i, y + j)



if __name__ == '__main__':
    sol = Solution()
    grid = [[1,1,1,1,1,1,1,0], \
            [1,0,0,0,0,1,1,0], \
            [1,0,1,0,1,1,1,0], \
            [1,0,0,0,0,1,0,1], \
            [1,1,1,1,1,1,1,0]]
    print(sol.closedIsland(grid))


