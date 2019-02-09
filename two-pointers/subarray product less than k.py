class Solution(object):

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = 1
        ret = list()
        ret_number = 0
        while start < len(nums):
            if self.prod(nums[start:end]) < k and end <= len(nums):
                ret.append(nums[start:end])
                ret_number += 1
                end += 1
            else:
                start += 1
                end = start+1
        return ret_number

    def prod(self, nums):
        seed = 1
        for num in nums:
            seed *= num
        return seed
