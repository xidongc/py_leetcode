class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[float("-inf") for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if obstacleGrid[i][j] == 1:
                        d[i][j] = 0
                    else:
                        if (i == 0 and d[i][j-1] == 0) or (j == 0 and d[i-1][0] == 0):
                            d[i][j] = 0
                        else:
                            d[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        d[i][j] = 0
                    else:
                        d[i][j] = (1-obstacleGrid[i-1][j]) * d[i-1][j] + \
                                  (1-obstacleGrid[i][j-1]) * d[i][j-1]
        return d[m-1][n-1]

# lmf
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or len(obstacleGrid) == 0 or not obstacleGrid[0] or obstacleGrid[0] == 0:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        res = [[0 for i in range(col)] for i in range(row)]
        # Find all the obstacles on row == 0 or col == 0
        for i in range(row):
            if obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                break
        for i in range(col):
            if obstacleGrid[0][i] == 0:
                res[0][i] = 1
            else:
                break
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    continue
                res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[row - 1][col - 1]


s = Solution()
ob = [[0,1],[0,0]]
print(s.uniquePathsWithObstacles(ob))
