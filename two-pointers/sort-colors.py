class Solution:

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p1 = len(nums)-1
        i = 0
        if not nums or len(nums) <= 1:
            return

        while i <= p1:
            if nums[i] == 0:
                tmp = nums[p0]
                nums[p0] = nums[i]
                nums[i] = tmp
                p0 += 1
                i += 1
            elif nums[i] == 2:
                tmp = nums[p1]
                nums[p1] = nums[i]
                nums[i] = tmp
                p1 -= 1
            else:
                i += 1
