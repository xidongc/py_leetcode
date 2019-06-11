class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if len(nums) == 0:
            return -1  # not found

        local_max, global_max = float("-inf"), float("-inf")
        for num in nums:
            local_max = max(0, local_max) + num
            global_max = max(global_max, local_max)

        return global_max
