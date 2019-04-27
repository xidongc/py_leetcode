class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for k in range(len(nums)):
            if k < 2 or nums[k] != nums[i - 2]:
                nums[i] = nums[k]
                i += 1
        return i
