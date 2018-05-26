class Solution:
    def __init__(self):
        self.ret = []

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        curr = []
        self.cal(s, wordDict, curr)
        return self.ret

    def cal(self, s, wordDict, curr):
        if s == '':
            tmp = " ".join(curr)
            self.ret.append(tmp)
        for i in range(len(s)+1):
            if s[0:i] in wordDict:
                print(s[0:i])
                curr.append(s[0:i])
                self.cal(s[i:len(s)], wordDict, curr)
                curr.pop()

sl = Solution()

s = "catsanddog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

print(sl.wordBreak(s, wordDict))