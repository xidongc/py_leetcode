class Solution(object):

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        max_sqr = 0

        if not matrix:
            return max_sqr

        col = len(matrix[0])
        row = len(matrix)
        height = [[0 for _ in range(col)] for _ in range(row)]

        for r in range(row):
            for c in range(col):
                if int(matrix[r][c]) == 0:
                    height[r][c] = 0
                else:
                    if r == 0:
                        height[r][c] = 1
                    else:
                        height[r][c] = height[r-1][c] + 1

        for r in range(row):
            max_sqr = max(max_sqr, self.max_rec_hist(height[r]))
        return max_sqr

    def max_rec_hist(self, hist):
        max_sqr = 0
        vector = [0]
        length = len(hist)

        if not hist:
            return max_sqr

        for h in hist:
            if h >= vector[-1]:
                vector.append(h)
            else:
                tmp_arr = []

                while vector[-1] > h:
                    tmp = vector.pop()
                    tmp_arr.append(h)
                    max_sqr = max(max_sqr, tmp*len(tmp_arr))

                vector.extend(tmp_arr)
                vector.append(h)

        for i, v in enumerate(vector[1:]):
            max_sqr = max((length - i)*v, max_sqr)

        return max_sqr

input = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
heights = [3, 1, 3, 2, 2]

s = Solution()
print(s.maximalRectangle(input))