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


# sol-2, using direction and seen matrix
class Solution(object):

    def spiralOrder(self, matrix):
        # corner case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return list()

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        seen = [[False for _ in range(n)] for _ in range(m)]

        di = 0
        rx, ry = 0, 0
        visited = list()

        for _ in range(m * n):
            seen[rx][ry] = True
            visited.append(matrix[rx][ry])
            if 0 <= rx + direction[di % 4][0] < m and 0 <= ry + direction[di % 4][1] < n and not \
            seen[rx + direction[di % 4][0]][ry + direction[di % 4][1]]:
                rx += direction[di % 4][0]
                ry += direction[di % 4][1]
            else:
                di += 1
                rx += direction[di % 4][0]
                ry += direction[di % 4][1]

        return visited

