class Solution(object):

    def coinChange(self, coins, amount):
        if amount == 0:
            return 0

        dp = [[amount + 1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] == j:
                    dp[i][j] = 1
                elif coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)

        if dp[len(coins)][amount] == amount + 1:
            return -1
        else:
            return dp[len(coins)][amount]
