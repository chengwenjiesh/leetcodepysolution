from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        self.fillBank(m, n, 0, -1, pacific)
        self.fillBank(m, n, -1, 0, pacific)
        self.fillBank(m, n, -1, n - 1, atlantic)
        self.fillBank(m, n, m - 1, -1, atlantic)

        result = []
        self.findLands(heights, pacific)
        self.findLands(heights, atlantic)
        for (x, y) in pacific:
            if (x, y) in atlantic:
                result.append([x, y])
        return result

    def fillBank(self, row, col, x, y, ocean) -> None:
        if y == -1:
            # fill row
            for j in range(col):
                ocean.add((x, j))
        elif x == -1:
            # fill col
            for i in range(row):
                ocean.add((i, y))

    def findLands(self, heights, ocean: Set) -> None:
        gridQueue = deque()
        for (i, j) in ocean:
            gridQueue.append((i, j))

        m, n = len(heights), len(heights[0])
        while gridQueue:
            (x, y) = gridQueue.popleft()
            for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x + i < m and 0 <= y + j < n \
                                  and heights[x + i][y + j] >= heights[x][y] \
                                  and (x + i, y + j) not in ocean:
                    ocean.add((x + i, y + j))
                    gridQueue.append((x + i, y + j))


if __name__ == '__main__':
    sol = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(sol.pacificAtlantic(heights))

