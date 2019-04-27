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
            return h > x >= 0 and w > y >= 0

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


# Sol-2 memorize dfs AC, TC: O(n*m)
class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # corner case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cache = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        def dfs(i, j, cache):
            if cache[i][j] != 1:
                return cache[i][j]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if self.inposition(x, y, len(matrix), len(matrix[0])) and matrix[i][j] < matrix[x][y]:
                    cache[i][j] = max(cache[i][j], dfs(x, y, cache) + 1)
            return cache[i][j]

        longest = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest = max(longest, dfs(i, j, cache))
        return longest

    def inposition(self, i, j, m, n):
        return 0 <= i < m and 0 <= j < n


# Sol-3 sorted dp, original idea from hua hua
class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        positions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        longest = 0
        tmp = list()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tmp.append((matrix[i][j], i, j))

        tmp.sort(key=lambda x: -x[0])

        for t in tmp:
            (num, i, j) = t
            for p in positions:
                x = i + p[0]
                y = j + p[1]
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[i][j] < matrix[x][y]:
                    dp[i][j] = max(dp[i][j], dp[x][y] + 1)

            longest = max(longest, dp[i][j])
        return longest
