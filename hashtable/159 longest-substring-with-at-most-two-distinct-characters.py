class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 2:
            return len(s)
        dict = {}
        dict[s[0]] = 1
        i, j = 0, 1
        tempLen = 1
        res = 0
        while j < len(s):
            if s[j] not in dict:
                dict[s[j]] = 1
            else:
                dict[s[j]] += 1
            tempLen += 1
            while i < j - 1 and len(dict) > 2:
                if dict[s[i]] > 1:
                    dict[s[i]] -= 1
                else:
                    dict.pop(s[i])
                tempLen -= 1
                i += 1
            j += 1
            res = max(res,tempLen)
        return res
s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("ccaabbb"))
# dict.pop(key)