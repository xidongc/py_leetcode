class Solution:

    def largest_rectangle_area(self, heights) -> int:
        # decreasing mono stack
        # to get next smaller height and previous smaller height
        # use trick to insert 0 in start and end of the heights to avoid corner case
        # add both left part and right part

        heights.append(0)
        heights.insert(0, 0)
        mono_stack = []
        max_result = 0
        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)

        for i, height in enumerate(heights):
            while mono_stack and heights[mono_stack[-1]] > height:
                ele = mono_stack.pop()
                right[ele] = i
            left[i] = mono_stack[-1] if mono_stack else 0
            mono_stack.append(i)

        for i in range(len(heights)):
            max_result = max(max_result, heights[i] * (right[i] - left[i] - 1))

        return max_result
