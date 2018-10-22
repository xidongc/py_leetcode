# class Solution(object):
#
#     def maximalRectangle(self, matrix):
#         """
#         :type matrix: List[List[str]]
#         :rtype: int
#         """
#
#         max_sqr = 0
#
#         if not matrix:
#             return max_sqr
#
#         col = len(matrix[0])
#         row = len(matrix)
#         height = [[0 for _ in range(col)] for _ in range(row)]
#
#         for r in range(row):
#             for c in range(col):
#                 if int(matrix[r][c]) == 0:
#                     height[r][c] = 0
#                 else:
#                     if r == 0:
#                         height[r][c] = 1
#                     else:
#                         height[r][c] = height[r-1][c] + 1
#
#         for r in range(row):
#             max_sqr = max(max_sqr, self.max_rec_hist(height[r]))
#         return max_sqr
#
#     def max_rec_hist(self, hist):
#         max_sqr = 0
#         vector = [0]
#         length = len(hist)
#
#         if not hist:
#             return max_sqr
#
#         for h in hist:
#             if h >= vector[-1]:
#                 vector.append(h)
#             else:
#                 tmp_arr = []
#
#                 while vector[-1] > h:
#                     tmp = vector.pop()
#                     tmp_arr.append(h)
#                     max_sqr = max(max_sqr, tmp*len(tmp_arr))
#
#                 vector.extend(tmp_arr)
#                 vector.append(h)
#
#         for i, v in enumerate(vector[1:]):
#             max_sqr = max((length - i)*v, max_sqr)
#
#         return max_sqr


# lmf暴力
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
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
                # for k in range(j + 1):
                # 这里用倒序因为不然k到j之间到minheight无法检查了
                    minHeight = min(minHeight,heights[k])
                    res = max(res, minHeight*(j-k+1))
        return res

input = [
  ["1","0","1","0","0"],
  ["1","1","1","0","1"],
  ["1","1","0","1","1"],
  ["1","0","0","1","0"]
]
heights = [3, 1, 3, 2, 2]

s = Solution()
print(s.maximalRectangle(input))
