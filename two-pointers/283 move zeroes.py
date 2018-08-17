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


# sol2 by xidong
# 2 pointers

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = p2 = 0
        for num in nums:
            if num != 0:
                nums[p2] = num
                p1 += 1
                p2 += 1
            else:
                p1 += 1

        for i in range(p2, p1):
            nums[i] = 0
