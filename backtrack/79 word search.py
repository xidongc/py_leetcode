class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, i, j):
                        return True
        return False

    def dfs(self, board, word, i, j):
        if word == '':
            return True
        res = False
        if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and board[i][j] == word[0]:
            board[i][j] = '#'
            res = self.dfs(board, word[1:], i + 1, j) or self.dfs(board, word[1:], i - 1, j) or self.dfs(board,word[1:], i,j + 1) or self.dfs(board, word[1:], i, j - 1)
            board[i][j] = word[0]
        return res
