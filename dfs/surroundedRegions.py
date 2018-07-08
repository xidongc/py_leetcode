class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        for row in range(len(board)):
            self.check(board,row,0)
            self.check(board,row,len(board[0]) - 1)
        for col in range(len(board[0])):
            self.check(board,0,col)
            self.check(board,len(board) - 1,col)
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '1':
                    board[row][col] = 'O'
                    
    def check(self, board, row, col):
        if board[row][col] == 'O':
            board[row][col] = '1'
            if row + 1 > 0 and row + 1 < len(board) - 1 and col > 0 and col < len(board[0]) - 1:
                self.check(board,row + 1, col)
            if row - 1 > 0 and row - 1 < len(board) - 1 and col > 0 and col < len(board[0]) - 1:
                self.check(board,row - 1, col)
            if row > 0 and row < len(board) - 1 and col + 1 > 0 and col + 1 < len(board[0]) - 1:
                self.check(board,row, col + 1)
            if row > 0 and row < len(board) - 1 and col - 1 > 0 and col - 1 < len(board[0]) - 1:
                self.check(board,row, col - 1)
                
# First, check the four border of the matrix. If there is a element is
# 'O', alter it and all its neighbor 'O' elements to '1'.

# Then ,alter all the 'O' to 'X'

# At last,alter all the '1' to 'O'
