class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or len(matrix[0]) <= 0:
            return 0

        h = len(matrix)
        w = len(matrix[0])

        memo_arr = [[0 for _ in range(w)] for _ in range(h)]
        max_len = 0

        def in_or_not(x, y):
            if h > x >= 0 and w > y >= 0:
                return True
            else:
                return False

        def bfs(i, j, matrix):
            # bfs i, j, and memorize
            nonlocal memo_arr, max_len
            dir_x = [1, -1, 0, 0]
            dir_y = [0, 0, 1, -1]
            ret = []

            if not in_or_not(i, j):
                return 0

            for t, x in enumerate(dir_x):
                if in_or_not(i+x, j+dir_y[t]) and matrix[i][j] > matrix[i+x][j+dir_y[t]]:
                    if memo_arr[i+x][j+dir_y[t]] != 0:
                        ret.append(memo_arr[i+x][j+dir_y[t]])
                    else:
                        ret.append(bfs(i+x, j+dir_y[t], matrix))
                else:
                    ret.append(0)

            memo_arr[i][j] = max(ret) + 1
            max_len = max(max_len, memo_arr[i][j])
            return max(ret) + 1

        for i in range(h):
            for j in range(w):
                bfs(i, j, matrix)

        return max_len
