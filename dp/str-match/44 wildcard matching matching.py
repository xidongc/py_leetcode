# https://shmilyaw-hotmail-com.iteye.com/blog/2154716


class Solution(object):

    # dp
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == '*'

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[len(s)][len(p)]

    # sol-2 with two pointers
    def isMatch_2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sl, pl = len(s), len(p)
        si, pi = 0, 0
        sm, pm = -1, -1

        while si < sl:
            if pi < pl and (p[pi] == "?" or s[si] == p[pi]):
                pi += 1
                si += 1
            elif pi < pl and p[pi] == "*":
                sm, pm = si, pi
                pi += 1
            elif sm != -1 and pm != -1:
                si, pi = sm + 1, pm + 1
                sm += 1
            else:
                return False

        while pi < pl and p[pi] == "*":
            pi += 1

        if pi == pl and si == sl:
            return True
        return False
