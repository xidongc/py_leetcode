# 然后我们遍历数组，当遇到0时，将其和0序列后面一个数交换，然后将0序列的指针向后移。
# 当遇到2时，将其和2序列前面一个数交换，然后将2序列的指针向前移。
# 遇到1时，不做处理。
# 这样，当我们遍历到2序列开头时，实际上i之前有序，因为所有0都被交换到了前面，
# 所有2都被交换到了后面。
# 所以swap 0的时候可以吧i指针向右移
# 但是swap 2的时候不能动i指针直到nums[i] < 2

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            #             case 2
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            #             case2 结束后i不动继续检验 case1/case2
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 1:
                i += 1
