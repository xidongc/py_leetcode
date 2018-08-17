
# 325
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0
        dict = {}
        low = 0
        res = 0
        for i in range(len(s)):
            # keeps the rightmost position of each char
            dict[s[i]] = i
            if len(dict) > k:
                low = min(dict.values())
                # remove one leftmost char and continue
                del dict[s[low]]
                low += 1
            res = max(i - low + 1, res)
        return res

s = Solution()
s.lengthOfLongestSubstringKDistinct("eceba",2)
