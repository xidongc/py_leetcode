class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []
        Solution.res = []
        self.backtrack(s, wordDict, 0, "")
        return Solution.res

    def backtrack(self, s,  wordDict, start, tempStr):

        for i in range(start, len(s)):
            if s[start : i + 1] not in wordDict or not self.hasWord(wordDict, s[i + 1:]):
                continue
            else:
                if i == len(s) - 1:

                    Solution.res.append(tempStr + s[start:])
                    return
                else:
                    self.backtrack(s, wordDict, i + 1, tempStr + s[start : i + 1] + " ")
    def hasWord(self, wordDict, string):
        # pineapple or catdog
        for i in range(len(string)):
            if string[i:] in wordDict:
                return True
        return False
# Backtrack
# 不管了就这样吧
s = Solution()
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))