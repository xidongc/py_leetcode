class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0 #the position of where zero is
        for i in range(len(nums)):
            if nums[i]:
                nums[zero],nums[i],zero = nums[i],nums[zero],zero + 1
