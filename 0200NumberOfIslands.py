class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        cnt = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.sinkIsland(grid, i, j)
                    cnt += 1
                    
        return cnt
    
    def sinkIsland(self, grid, row, col):
        grid[row][col] = "0"
        m, n = len(grid), len(grid[0])
        
        for (i2, j2) in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == "1":
                self.sinkIsland(grid, i2, j2)

if __name__ == '__main__':
    sol = Solution()
    print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
