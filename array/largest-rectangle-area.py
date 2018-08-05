class Solution(object):

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        max_area = 0

        if not heights:
            return max_area

        len_height = len(heights)

        stack = [0]
        for i, hi in enumerate(heights):
            if hi >= stack[-1]:
                stack.append(hi)
            else:
                tmp = []
                while stack[-1] > hi:
                    a = stack.pop()
                    tmp.append(hi)
                    max_area = max(max_area, len(tmp)*a)
                stack.extend(tmp)
                stack.append(hi)

        for i, x in enumerate(stack[1:]):
            max_area = max(max_area, (len_height-i)*x)

        return max_area

s = Solution()
heights = [3, 1, 3, 2, 2]
print(s.largestRectangleArea(heights))

