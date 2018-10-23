class Solution(object):

    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        [1,3,4,2,2]
        nums.sort()

        for i, num in enumerate(nums):
            if nums[i] == nums[i-1]:
                return nums[i]

        return None
