class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left,right = 0, len(height) - 1
        maxRes = 0
        while left < right:
            maxRes = max((right - left) * min(height[left],height[right]),maxRes)
            # 这里找更大毫无意义因为取决于短板啊，只有短板升高才能真正升高
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxRes

# Sol - 2 (solution when 1st review)
class Solution(object):

    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0

        while i < j:
            if height[i] < height[j]:
                area = max(area, (j - i) * height[i])
                ref_i = height[i]
                while i < j and height[i] <= ref_i:
                    i += 1
            else:
                area = max(area, (j - i) * height[j])
                ref_j = height[j]
                while i < j and height[j] <= ref_j:
                    j -= 1

        return area