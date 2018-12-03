class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if 2*leftSum == total - nums[i]:
                return i
            leftSum += nums[i]
        return -1