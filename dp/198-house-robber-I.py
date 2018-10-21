class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        i = 1
        dp_array = [0] * 3
        dp_array[0] = nums[0]
        dp_array[1] = max(nums[0], nums[1])

        for i, num in enumerate(nums[2:]):
            i += 2
            dp_array[i % 3] = max(dp_array[(i-1) % 3], dp_array[(i-2) % 3] + num)

        return dp_array[i % 3]

