class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        board = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        return self.findProb(n, board, k, row, column)

    def findProb(self, n, board, k, row, col):
        if row < 0 or row >= n or col < 0 or col >= n:
            return 0

        if k == 0:
            return 1

        if board[k][row][col] != 0:
            return board[k][row][col]

        currProb = 0.0
        for i, j in [(1,-2), (1,2), (-1,2), (-1, -2), (2,1), (2,-1), (-2,1), (-2,-1)]:
            currProb += 1 / 8 * self.findProb(n, board, k - 1, row + i, col + j)

        board[k][row][col] = currProb
        return currProb


