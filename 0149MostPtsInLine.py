from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        sz = len(points)
        if sz < 2:
            return sz
        mostPt = 1

        for i in range(len(points)):
            # {(1,3) : 2} with deltax = 1 deltay = 3, we have 2 other pts
            positions = {}
            samePt = 0
            sameLn = 0

            for j in range(i + 1, len(points)):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                if not dx and not dy:
                    samePt += 1

                xyGCD = self._gcd(dx, dy)
                if xyGCD:
                    dx /= xyGCD
                    dy /= xyGCD

                if (dx, dy) not in positions:
                    positions[(dx, dy)] = 1
                else:
                    positions[(dx, dy)] += 1
                sameLn = max(positions[(dx, dy)], sameLn)

            mostPt = max(mostPt, 1 + samePt + sameLn)

        return mostPt


    def _gcd(self, a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

