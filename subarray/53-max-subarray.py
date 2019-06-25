class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rangeSum = -float("inf")
        globalSum = -float("inf")
        for i, num in enumerate(nums):
            rangeSum = max(rangeSum, 0) + num
            globalSum = max(globalSum, rangeSum)
        return globalSum
