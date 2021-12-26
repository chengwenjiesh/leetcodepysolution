from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row, col, block = set(), set(), set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in row:
                    return False
                row.add(board[i][j])

                if board[j][i] != "." and board[j][i] in col:
                    return False
                col.add(board[j][i])

                x, y = 3 * (i // 3) + (j // 3), 3 * (i % 3) + (j % 3)
                if board[x][y] != "." and board[x][y] in block:
                    return False
                block.add(board[x][y])

        return True

