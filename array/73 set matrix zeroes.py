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