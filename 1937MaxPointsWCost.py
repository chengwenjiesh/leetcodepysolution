from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points or not points[0]:
            return 0

        m, n = len(points), len(points[0])
        curr, nxt = points[0][:], [0] * n

        for i in range(1, m):
            # what's highest score from left
            # what's highest score from right
            lMax = rMax = 0
            for j in range(n):
                nxt[j] = max(curr[j] + points[i][j], lMax + points[i][j] - 1)
                lMax = max(curr[j], lMax - 1)
            for j in range(n - 1, -1, -1):
                nxt[j] = max(nxt[j], rMax + points[i][j] - 1)
                rMax = max(curr[j], rMax - 1)
            curr, nxt = nxt, [0] * n

        return max(curr)


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,2,3],[1,5,1],[3,1,1]]
    print(sol.maxPoints(grid))

