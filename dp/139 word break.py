# AC, dp solution with O(n*2)
class Solution(object):

    def wordBreak(self, s, wordDict):
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True

        return dp[len(s)]


# TLE, brute force with dfs
class Solution(object):

    def wordBreak(self, s: str, wordDict):
        def dfs(index):
            if index == len(s):
                return True

            for i in range(index + 1, len(s) + 1):
                if s[index:i] in wordDict:
                    ret = dfs(i)
                    if ret:
                        return ret

        if dfs(0) is True:
            return True
        return False
