class Solution(object):

    def spiralOrder(self, matrix):
        ret = list()
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return list()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(min(m, n)):
            ret.extend(matrix[i][i:n - i])
            for j in range(i + 1, m - i):
                ret.append(matrix[j][n - i - 1])
            if m - i - 1 > i:
                ret.extend(matrix[m - i - 1][n - i - 2:i:-1])
            if n - i - 1 > i:
                for j in range(m - i - 1, i, -1):
                    ret.append(matrix[j][i])

        return ret[0:m * n]
