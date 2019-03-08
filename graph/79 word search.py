class Solution(object):

    def exist(self, board, word):

        # corner case
        if len(word) == 0:
            return True

        if len(board) == 0 or len(board[0]) == 0:
            return False

        condition = False
        m = len(board)
        n = len(board[0])

        visited = [[False for _ in range(n)] for _ in range(m)]
        positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(startX, startY, visited, target):
            nonlocal board
            # end condition
            if len(target) <= 0:
                return True

            # for iteration 
            condition = False
            for p in positions:
                x = startX + p[0]
                y = startY + p[1]
                if 0 <= x < m and 0 <= y < n and board[x][y] == target[0] and visited[x][y] is False:
                    visited[x][y] = True
                    condition = condition or dfs(x, y, visited, target[1:])
                    visited[x][y] = False

            return condition

        # find the first ele
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    condition = condition or dfs(i, j, visited, word[1:])
                    visited[i][j] = False

        return condition