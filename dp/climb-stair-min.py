class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(cost))]
        for i in range(len(cost)):
            if i == 0:
                dp[i] = cost[i]
            elif i == 1:
                dp[i] = min(cost[i], cost[i-1])
            else:
                dp[i] = min(dp[i-2], dp[i-1])+cost[i]

        print(dp)
        return min(dp[len(cost)-1], dp[len(cost)-2])

cost = [1, 100, 1, 1, 1, 100,1,100,100]
s = Solution()
print(s.minCostClimbingStairs(cost))