class Solution(object):

    def numDecodings(self, s: str) -> int:

        # dp[i] = dp[i-1] + dp[i-2] and 10 < s[i-2:i] <= 26 rule out eg: "01"

        dp = [0 for _ in range(len(s) + 1)]
        dp[1] = 1 if 0 < int(s[0]) <= 9 else 0
        dp[0] = 1

        for i in range(2, len(s) + 1):
            dp[i] = dp[i - 1] if 0 < int(s[i - 1]) <= 9 else 0

            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
