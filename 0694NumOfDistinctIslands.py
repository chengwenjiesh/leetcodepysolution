class Solution:
    def numDistinctIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        islandShapes = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandShapes.add(self.probeShape(grid, i, j, 's'))

        for e in islandShapes:
            print(e)
        return len(islandShapes)

    def probeShape(self, grid, x, y, move):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
            return ''

        # four directions: u d l r
        grid[x][y] = 0
        return move + \
               self.probeShape(grid, x, y + 1, 'u') + \
               self.probeShape(grid, x, y - 1, 'd') + \
               self.probeShape(grid, x + 1, y, 'r') + \
               self.probeShape(grid, x - 1, y, 'l') + '0'


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,0,1]]
    print(sol.numDistinctIslands(grid))

