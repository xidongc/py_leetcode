import collections


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l, r = 0, 0
        curSum = 0
        res = len(nums) + 1
        while r < len(nums):
            while curSum < s and r < len(nums):
                curSum += nums[r]
                r += 1
            #  nums[r] excluded
            while curSum >= s and l < len(nums):
                res = min(res, r - l)
                curSum -= nums[l]
                l += 1
        if res == len(nums) + 1:
            return 0
        return res
