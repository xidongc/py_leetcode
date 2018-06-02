class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #1
        # if not nums or len(nums) == 0:
        #     return 0
        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1
        # return count
        #2
        if not nums or len(nums) == 0:
            return 0
        map = {}
        map[0] = 1
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum - k) in map.keys():
                count += map[sum-k]
            if sum not in map.keys():
                map[sum] = 1
            else:
                map[sum] += 1
        return count
        
