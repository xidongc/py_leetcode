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
                        if (i == 0 and d[i][j-1] == 0) or (j ==0 and d[i-1][0] == 0):
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


s = Solution()
ob = [[0,1],[0,0]]
print(s.uniquePathsWithObstacles(ob))
