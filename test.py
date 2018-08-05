class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
# 暴力
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        heights = [0] * col
        res = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    heights[j] = 0
                    continue
                heights[j] += 1
                minHeight = heights[j]
                for k in range(j,-1,-1):
                    minHeight = min(minHeight,heights[k])
                    res = max(res, minHeight*(j-k+1))
        return res
# DP
s = Solution()
print(s.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"]]))

