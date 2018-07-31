class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or not int(s[0]):
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(s) + 1):
            curSingleDigit = int(s[i-1])
            curTwoDigit = int(s[i-2:i])
            if not curSingleDigit and curTwoDigit > 26:
                return 0
            if curSingleDigit:
                dp[i] += dp[i - 1]
            if curTwoDigit > 9 and curTwoDigit < 27:
                dp[i] += dp[i - 2]
        return dp[len(s)]