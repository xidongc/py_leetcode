class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        curNum = s[0]
        prevCount = 0
        curCount = 0
        res = 0
        for pos in range(len(s)):
            if s[pos] == curNum:
                prevCount += 1
            else:
                break
        if pos == len(s) - 1 and s[pos] == s[pos - 1]: return 0
        curNum = s[pos]
        for i in range(pos, len(s)):
            if s[i] == curNum:
                curCount += 1
            else:
                res += min(prevCount, curCount)
                prevCount, curCount, curNum = curCount, 1, s[i]
        res += min(prevCount, curCount)
        return res


