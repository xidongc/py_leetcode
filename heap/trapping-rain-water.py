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

#lmf
# two pointers
# 从左右两边向中间靠近，分别算水量
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0,len(height) - 1
        res = 0
        maxLeft,maxRight = 0,0
        while left <= right:
            # 左边比较短，左边是下限
            if height[left] <= height[right]:
                # 都判断一下是不是最高点
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                # 右边是下限
                # 都判断一下是不是最高点
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res
s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
