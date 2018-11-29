class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) <= 1:
            return s

        length = len(s)
        res = s[0]
        dp = [[0 for i in range(length)] for i in range(length)]
        for i in range(length-1,-1,-1):
            for j in range(i+1,length):
                dp[i][j] = s[i] == s[j] and (dp[i+1][j-1] or j-i <= 2)
                if dp[i][j] and (not res or len(res) < j-i+1):
                    res = s[i:j+1]
        return res
    # 'a'-> 'a'
    # 'aa' -> 'aa'
    # 'abcd' -> 'a'
# 非dp的机智做法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isPalindrome(s, start, end):
            if start < 0:
                return False
            return s[start:end + 1] == s[start:end + 1][::-1]

        curMax = 0
        start, end = 0, 0
        for i in range(len(s)):
            # 先走大的步，包括了两个点( i和i-curMax-1)，两个条件不同时满足
            # 每次尝试跨越上次的curmax
            if isPalindrome(s, i - curMax - 1, i):
                start, end = i - curMax - 1, i
                curMax += 2
            elif isPalindrome(s, i - curMax, i):
                # ccc
                start, end = i - curMax, i
                curMax += 1
        return s[start:end + 1]

