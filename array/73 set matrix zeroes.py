# Sol by xidong
class Solution(object):

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # corner case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        # Time Complexity: ~ O(m*n)
        m = len(matrix)
        n = len(matrix[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if visited[i][j] is False and matrix[i][j] == 0:
                    visited[i][j] = True
                    for x in range(i):
                        if matrix[x][j] != 0 and visited[x][j] is False:
                            matrix[x][j] = 0
                            visited[x][j] = True
                    for x in range(i + 1, m):
                        if matrix[x][j] != 0 and visited[x][j] is False:
                            matrix[x][j] = 0
                            visited[x][j] = True
                    for x in range(0, j):
                        if matrix[i][x] != 0 and visited[i][x] is False:
                            matrix[i][x] = 0
                            visited[i][x] = True
                    for x in range(j + 1, n):
                        if matrix[i][x] != 0 and visited[i][x] is False:
                            matrix[i][x] = 0
                            visited[i][x] = True

# 见笔记
class Solution:
    def setZeroes(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        row, col = len(matrix), len(matrix[0])
        col0 = 1
        for i in range(row):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range(row-1,-1,-1):
            for j in range(col-1,0,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

s = Solution()
s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])