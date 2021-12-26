from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # word is not empty
        # board is at least 1*1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.findWord(board, i, j, word, 0):
                    return True

        return False

    def findWord(self, board, x, y, word, idx):
        if idx == len(word):
            return True

        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False

        if board[x][y] != word[idx]:
            return False

        board[x][y], buf = '*', board[x][y]

        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if self.findWord(board, x + i, y + j, word, idx + 1):
                return True

        board[x][y] = buf

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCC"))

