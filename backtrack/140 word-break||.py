import collections


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]dis
        :rtype: List[str]
        """
        sDict = collections.defaultdict(list)

        def dfs(s):
            if not s:
                return [None]
            if s in sDict:
                return sDict[s]
            res = []
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    for tmpStr in dfs(s[n:]):
                        if tmpStr:
                            res.append(word + ' ' + tmpStr)
                        else:
                            res.append(word)
            sDict[s] = res
            return res

        return dfs(s)



s = Solution()
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))