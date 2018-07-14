class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        for i in range(len(nums)):
            if nums[i] != nums[tmp]:
                nums[tmp]
                tmp = tmp+1