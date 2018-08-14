# 前缀和数组？
# HashMap
# 0%any=>0
class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False
        if k == 0:
            return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))
        sum = 0
        map = {0:-1}
        for i in range(len(nums)):
            sum += nums[i]
            r = sum % k
            if r not in map:
                map[r] = i
            elif r in map and i - map[r] > 1:
                return True
        return False

