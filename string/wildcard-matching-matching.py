# https://shmilyaw-hotmail-com.iteye.com/blog/2154716


# greedy solution using two pointers (most common)
class Solution(object):

    def isMatch(self, s, p):
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


# dp solution， improve on recursive solution below
class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
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


# More easy way to understand, recursive, TLE
class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def helper(si, pi):
            if pi == len(p):
                return si == len(s)

            if si < len(s) and (p[pi] == "?" or p[pi] == s[si]):
                return helper(si + 1, pi + 1)
            elif p[pi] == "*":
                while pi < len(p) and p[pi] == "*":
                    pi += 1
                while si < len(s):
                    if helper(si, pi):
                        return True
                    si += 1
                return helper(si, pi)

        return helper(0, 0)
