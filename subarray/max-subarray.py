class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            dp[i] = max(nums[i], sum)
            if sum < 0:
                sum = 0

        dp.sort(reverse=True)

        return dp[0]

s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))