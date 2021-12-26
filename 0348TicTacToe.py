class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.antidiag = 0


    def move(self, x: int, y: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        candidate = 1 if player == 1 else -1
        if x == y:
            self.diag += candidate
        if x + y == self.size - 1:
            self.antidiag += candidate

        self.row[x] += candidate
        self.col[y] += candidate

        if self.row[x] == self.size or self.col[y] == self.size or self.diag == self.size \
                                                or self.antidiag == self.size:
            return 1
        if self.row[x] == -self.size or self.col[y] == -self.size or self.diag == -self.size \
                                                  or self.antidiag == -self.size:
            return 2

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
