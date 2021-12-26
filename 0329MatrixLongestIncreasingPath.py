from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cached = [[0] * n for _ in range(m)]
        maxLen = 1

        for i in range(m):
            for j in range(n):
                currLen = self.searchPath(matrix, i, j, cached)
                maxLen = max(maxLen, currLen)

        return maxLen


    def searchPath(self, matrix, x, y, cached):
        if cached[x][y]:
            return cached[x][y]

        cached[x][y] = 1
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nextX = x + i
            nextY = y + j
            if 0 <= nextX < len(matrix) and 0 <= nextY < len(matrix[0]) \
                                        and matrix[nextX][nextY] > matrix[x][y]:
                cached[x][y] = max(cached[x][y], \
                                   1 + self.searchPath(matrix, nextX, nextY, cached))

        return cached[x][y]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
