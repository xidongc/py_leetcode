# https://leetcode.com/problems/longest-increasing-subsequence/description/
# dp with time complexity O(n^2)


class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        dp = [1 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
