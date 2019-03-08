class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or int(s[0]) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1,len(s)):
            # if both single/dup requirements meet
            double = int(s[i-1:i+1])
            single = int(s[i])
            if double > 9 and double < 27:
                dp[i+1] += dp[i-1]
            if single != 0:
                dp[i+1] += dp[i]
            if single == 0 and (double >= 30):
                return 0
        return dp[-1]
# 从number->string decode
# https://leetcode.com/discuss/interview-question/124939/fb-phone-interview-a1b2z26-given-a-string-find-all-possible-codes-that-string-can-generate