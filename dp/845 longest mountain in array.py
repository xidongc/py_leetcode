# 左右夹击找peak
class Solution(object):
    def longestMountain(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        dp_order = [1] * len(nums)
        dp_reorder = [1] * len(nums)
        res = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                dp_order[i] = dp_order[i-1] + 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                dp_reorder[i] = dp_reorder[i+1] + 1
        for a,b in zip(dp_order,dp_reorder):
            if a != 1 and b != 1:
                res = max(res,a + b - 1)
        return res
