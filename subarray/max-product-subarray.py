class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            dp_min = [1 for _ in range(len(nums))]
            dp_max = dp_min[:]
            dp = dp_min[:]
            for i in range(len(nums)-1):
                if i == 0:
                    dp[i] = dp_max[i] = dp_min[i] = nums[i]
                dp_max[i+1] = max(dp_max[i]*nums[i+1],
                                  dp_min[i]*nums[i+1],
                                  nums[i+1])
                dp_min[i+1] = min(dp_max[i]*nums[i+1],
                                  dp_min[i]*nums[i+1],
                                  nums[i+1])
                dp[i+1] = max(dp[i], dp_max[i+1])

        return dp[len(nums)-1]

s = Solution()
nums = [2,3,-2,4]
print(s.maxProduct(nums))




