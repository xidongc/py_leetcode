class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        nums.sort()
        for i in range(0, len(nums), 3):
            if i + 1 == len(nums):
                return nums[i]
            elif nums[i + 1] != nums[i]:
                return nums[i]

