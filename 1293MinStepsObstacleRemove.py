from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        currlvl, nextlvl = [(0, 0, 0)], []
        minBlocker = [[float('inf')] * n for _ in range(m)]
        steps = 0

        while currlvl:
            steps += 1
            for curr in currlvl:
                x, y, ob = curr[0], curr[1], curr[2]
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x1, y1 = x + i, y + j
                    if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
                        continue

                    ob1 = ob + 1 if grid[x + i][y + j] == 1 else ob
                    if ob1 <= k:
                        if x1 == m - 1 and y1 == n - 1:
                            return steps

                        if ob1 < minBlocker[x1][y1]:
                            minBlocker[x1][y1] = ob1
                            nextlvl.append((x1, y1, ob1))
            currlvl, nextlvl = nextlvl, []

        return -1


