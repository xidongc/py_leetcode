class Solution(object):
    def __init__(self):
        self.ret = []

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [0 for _ in range(target+1)]
        for i in range(1, target+1):
            for num in nums:
                if i > num:
                    dp[i] += dp[i-num]
                elif i == num:
                    dp[i] += 1
        print(dp)
        return dp[target]


s = Solution()
nums = [1,2,3]
target = 4
print(s.combinationSum4(nums, target))