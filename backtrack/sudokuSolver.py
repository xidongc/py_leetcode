class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.solve()
    def findUnassigned(self):
        for i in range(9):
            for j  in range(9):
                if self.board[i][j] == ".":
                    return i, j
        return -1,-1
    def solve(self):
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.isValid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False
    def isValid(self, row, col, num):
        return self.isRowValid(row, num) and self.isColValid(col, num) and self.isBoxValid(row - row % 3, col - col % 3, num)
    def isRowValid(self, row, num):
        for i in range(9):
            if self.board[row][i] == num:
                return False
        return True
    def isColValid(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True
    def isBoxValid(self, row, col, num):
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if self.board[row][col] == num:
                    return False
        return True
s = Solution()
s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
)
#tle, no idea why it happens.
