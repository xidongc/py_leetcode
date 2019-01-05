class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        same = (word1 == word2)
        left, right = -(2 ** 32) + 1, 2 ** 32 - 1
        res = 2 ** 32 - 1
        for i, w in enumerate(words):
            if w == word1:
                if same:
                    left, right = right, i
                else:
                    left = i
            elif w == word2:
                right = i
            res = min(res, abs(right - left))
        return res


s = Solution()
s.shortestWordDistance(['a','a'],'a','a')