class NumMatrix(object):
    # 因为为了防止lefttop坐标是（0，0）从而导致计算大小的时候index溢出
    # 所以dp多了一行一列
    # 所以dp的坐标比matrix都要大1

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        self.dp = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                self.dp[i][j] = self.dp[i][j-1] + self.dp[i-1][j] - self.dp[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
