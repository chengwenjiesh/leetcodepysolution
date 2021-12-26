from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if board[i][j] == 'O':
                        self.flipConnected(board, i, j)

        trans = {'X':'X', 'O':'X', 'T':'O'}
        for i in range(m):
            for j in range(n):
                board[i][j] = trans[board[i][j]]

        return

    def flipConnected(self, board, x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return

        if board[x][y] == 'O':
            board[x][y] = 'T'
            for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
                self.flipConnected(board, x + i, y + j)


