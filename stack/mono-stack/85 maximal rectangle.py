class Solution(object):

    def maximalRectangle(self, matrix):

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
                        height[r][c] = height[r - 1][c] + 1

        for r in range(row):
            max_sqr = max(max_sqr, self.max_rec_hist(height[r]))
        return max_sqr

    def max_rec_hist(self, hist):
        max_sqr = 0

        stack = []
        hist.append(-1)
        left = [-1] * len(hist)
        right = [len(hist)] * len(hist)

        for i in range(len(hist)):
            while stack and hist[stack[-1]] >= hist[i]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        for i, v in enumerate(left):
            height = hist[i]
            max_sqr = max((right[i] - left[i] - 1) * height, max_sqr)

        return max_sqr
