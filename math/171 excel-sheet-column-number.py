class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        a = 0
        for i in range(len(s)-1,-1,-1):
            num = ord(s[i]) - ord('A') + 1
            res += num * pow(26,a)
            a += 1
        return res
s = Solution()
print(s.titleToNumber('AB'))