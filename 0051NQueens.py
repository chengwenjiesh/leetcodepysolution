from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        result = []
        for y in range(n):
            self.formQueens(0, y, n, [], result)
        return result

    def formQueens(self, x, y, n, prevQueens, result):
        if not self.isValid(x, y, prevQueens):
            return

        prevQueens.append((x, y))
        if x == n - 1:
            result.append(self.formOutput(prevQueens, n))
            return

        for y in range(n):
            self.formQueens(x + 1, y, n, prevQueens[:], result)

    def isValid(self, x, y, queens):
        for qx, qy in queens:
            if qx == x or qy == y or qx - x == qy - y or qx + qy == x + y:
                return False
        return True

    def formOutput(self, prevQueens, n):
        output = [["." for j in range(n)] for i in range(n)]
        for i, j in prevQueens:
            output[i][j] = "Q"
        return [''.join(output[i]) for i in range(n)]

