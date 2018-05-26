class Solution:

    def __init__(self):
        self.ret = []

    def wordBreak(self, s, wordDict):

        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp[i][j] means starting from [i for j ele can be slice
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for j in range(1, len(s)+1):
            for i in range(len(s)-j+1):
                if s[i:i+j] in wordDict:
                    dp[i][j] = 1
                else:
                    for k in range(i, i+j):
                        if dp[i][k] != 0 and dp[i+k][j-k] != 0:
                            dp[i][j] = 2
        if dp[0][len(s)] == 0:
            return self.ret
        curr = []
        self.dfs(s, curr, 0, dp)
        return self.ret

    def dfs(self, s, curr, start, dp):
        if start == len(s):
            self.ret.append(" ".join(curr))
            return
        for i in range(1, len(s)-start+1):
            if dp[start][i] == 1:
                curr.append(s[start:start+i])
                self.dfs(s, curr, start+i, dp)
                curr.pop()


sl = Solution()

s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(sl.wordBreak(s, wordDict))