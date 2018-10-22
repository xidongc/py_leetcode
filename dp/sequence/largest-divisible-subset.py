# https://leetcode.com/problems/largest-divisible-subset/description/
# dp alg, accpeted, time complexity: O(n^2)


class Solution(object):
    
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return []
        
        dp = [1 for _ in range(len(nums))]
        prev = [-1 for _ in range(len(nums))]
        ret = []
        
        nums.sort()
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
        
        start = dp.index(max(dp))
        
        while start != -1:
            ret.insert(-1, nums[start])
            start = prev[start]
            
        return ret