# Also refer 85 as follows up
class Solution:

    def largestRectangleArea(self, hist) -> int:
        # decreasing mono stack
        # to get next smaller height and previous smaller height
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
