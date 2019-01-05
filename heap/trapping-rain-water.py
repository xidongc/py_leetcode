class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p1 = 0
        p2 = len(height) - 1
        trap_rain = 0

        while p1 < p2:
            if height[p1] <= height[p2]:
                curr = height[p1]
                curr_index = p1
                tmp = 0
                p1 += 1
                while height[p1] < curr:
                    tmp += height[p1]
                    p1 += 1
                trap_rain += (p1-curr_index-1)*curr-tmp
            else:
                curr = height[p2]
                curr_index = p2
                tmp = 0
                p2 -= 1
                while height[p2] < curr:
                    tmp += height[p2]
                    p2 -= 1
                trap_rain += (curr_index - p2 - 1)*curr-tmp
        print(trap_rain)
        return trap_rain


