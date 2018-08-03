class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res = dict[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if dict[s[i]] < dict[s[i+1]]:
                res -= dict[s[i]]
            else:
                res += dict[s[i]]
        return res
s = Solution()
s.romanToInt("LVIII")