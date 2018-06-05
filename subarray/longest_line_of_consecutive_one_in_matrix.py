class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or len(M) == 0 or not M[0] or len(M[0]) == 0:
            return 0
        maxval = 0
        row = len(M)
        col = len(M[0])
        res = [[[0 for i in range(4)] for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                if M[i][j] == 0:
                    continue
                for k in range(4):
                    res[i][j][k] = 1
                if j > 0:
                    res[i][j][0] += res[i][j-1][0] #Horizontal
                if j > 0 and i > 0:
                    res[i][j][1] += res[i-1][j-1][1] #Diagonal
                if i > 0:
                    res[i][j][2] += res[i-1][j][2] #Vertical
                if j < col - 1 and i > 0:
                    res[i][j][3] += res[i-1][j+1][3] #Anti-Diagonal
                maxval = max(maxval,max(res[i][j][0],res[i][j][1]))
                maxval = max(maxval,max(res[i][j][2],res[i][j][3]))
        return maxval
