class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum = nums[0]
        i = 0
        end = len(nums) - 1
        while sum > 0 and i < end:
            i += 1
            sum = max(nums[i], sum-1)
        if i == end:
            return True
        else:
            return False

s = Solution()
nums = [3,2,1,0,4]
print(s.canJump(nums))
