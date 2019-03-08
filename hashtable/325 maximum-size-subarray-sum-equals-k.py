# 340
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums and k:
            return -1
        sum = 0
        res = 0
        map = {}
        for i in range(len(nums)):
            sum += nums[i]
            if sum == k:
                # If so, this would be the maximum one
                res = i + 1
            elif sum - k in map:
                res = max(res, i - map[sum-k])
            if sum not in map:
                map[sum] = i
        return res

# consecutive 相加等于什么什么的，都可以用差来做
# Edge case: nums = [], k=0