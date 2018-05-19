class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[i-j-1] * dp[j]
        return dp[n]

s = Solution()
print(s.numTrees(3))