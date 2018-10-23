import queue


class Solution(object):

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board or len(board) == 0:
            return

        h = len(board)
        w = len(board[0])

        bool_matrix = [[False for _ in range(w)] for _ in range(h)]

        edge_nodes = []

        for x in range(h):
            edge_nodes.append((x, 0))
            edge_nodes.append((x, w-1))
            bool_matrix[x][0] = True
            bool_matrix[x][w-1] = True
        for y in range(w):
            edge_nodes.append((0, y))
            edge_nodes.append((h-1, y))
            bool_matrix[0][y] = True
            bool_matrix[h-1][y] = True

        q = queue.Queue()

        edge_nodes = list(set(edge_nodes))


        for node in edge_nodes:
            x, y = node
            if board[x][y] == "O":
                q.put(node)
                while not q.empty():
                    x, y = q.get()
                    if x+1 < h and bool_matrix[x+1][y] is False and board[x+1][y] == "O":
                        q.put((x+1, y))
                        bool_matrix[x+1][y] = True
                    if x-1 >= 0 and bool_matrix[x-1][y] is False and board[x-1][y] == "O":
                        q.put((x-1, y))
                        bool_matrix[x-1][y] = True
                    if y-1 >= 0 and bool_matrix[x][y-1] is False and board[x][y-1] == "O":
                        q.put((x, y-1))
                        bool_matrix[x][y-1] = True
                    if y+1 < w and bool_matrix[x][y+1] is False and board[x][y+1] == "O":
                        q.put((x, y+1))
                        bool_matrix[x][y+1] = True

        for i in range(h):
            for j in range(w):
                if bool_matrix[i][j] is False and board[i][j] == "O":
                    board[i][j] = "X"

        print(board)

s = Solution()
s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])