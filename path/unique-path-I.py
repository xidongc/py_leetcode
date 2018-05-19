class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[float("-inf") for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    d[i][j] = 1
                else:
                    d[i][j] = d[i-1][j] + d[i][j-1]

        return d[m-1][n-1]