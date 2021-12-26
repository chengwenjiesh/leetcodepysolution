class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.getIslandArea(grid, i, j))

        return maxArea

    def getIslandArea(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
            return 0

        grid[x][y] = 0
        return 1 + self.getIslandArea(grid, x + 1, y) + \
                   self.getIslandArea(grid, x - 1, y) + \
                   self.getIslandArea(grid, x, y + 1) + \
                   self.getIslandArea(grid, x, y - 1)

if __name__ == '__main__':
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))

