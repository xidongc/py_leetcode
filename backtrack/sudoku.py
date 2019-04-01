class Solution(object):

    def isValidSudoku(self, board):

        # corner case
        if len(board) == 0 or len(board[0]) == 0 or len(board) != len(board[0]):
            return False

        for i in range(len(board)):
            rows = set()
            cols = set()
            sector = set()

            for j in range(len(board)):
                row_index = 3 * (i // 3)
                col_index = 3 * (i % 3)

                if board[i][j] in rows or board[j][i] in cols or \
                        board[row_index + j // 3][col_index + j % 3] in sector:
                    return False
                else:
                    if board[i][j] != ".":
                        rows.add(board[i][j])
                    if board[j][i] != ".":
                        cols.add(board[j][i])
                    if board[row_index + j // 3][col_index + j % 3] != ".":
                        sector.add(board[row_index + j // 3][col_index + j % 3])
        return True
