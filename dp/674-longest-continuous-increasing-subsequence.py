class Solution(object):

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp_array = [1]*2  # space optimization
        max_len = 1

        for i, num in enumerate(nums[1:]):
            i += 1
            if num > nums[i-1]:
                dp_array[i % 2] = dp_array[(i-1) % 2] + 1
                max_len = max(max_len, dp_array[i % 2])
            else:
                dp_array[i % 2] = 1

        return max_len

