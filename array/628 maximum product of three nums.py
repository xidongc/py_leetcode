# 不足3个
# 最大的三个/最小的两个*最大的一个（可能有负数）
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) <= 3:
            product = 1
            for num in nums:
                product *= num
            return product
        else:
            length = len(nums)
            nums.sort()
            return max(nums[length - 1] * nums[length - 2] * nums[length - 3], nums[length - 1] * nums[0] * nums[1])

