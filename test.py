class Solution(object):

    def __init__(self):
        self.slice = []

    def is_slice_able(self, s, dic_set):
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dic_set:
                    dp[i] = True
        return dp[len(s)]

    def find_all_slices(self, s, dic_set):
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s))]
        for j in range(1, len(s)+1):
            for i in range(len(s)-j +1):
                if s[i:i+j] in dic_set:
                    print(i, j)
                    dp[i][j] = 1
                else:
                    for k in range(i+1, j):
                        if dp[i][k] != 0 and dp[i+k][j-k] != 0:
                            print(i, j)
                            dp[i][j] = 2
        if dp[0][len(s)] == 0:
            return self.slice

        curr = []

        self.dfs(s, curr, 0, dp)
        return self.slice

    def dfs(self, s, curr, start, dp):
        if start == len(s):
            self.slice.append(" ".join(curr))
        for i in range(start, len(s)+1-start):
            if dp[start][i] == 1:
                curr.append(s[start:start+i])
                self.dfs(s, curr, start+i, dp)
                curr.pop()


sl = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(sl.is_slice_able(s, wordDict))
print(sl.find_all_slices(s, wordDict))

