class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        i = 0
        pattern = ""
        while i < len(s) // 2:
            pattern += s[i]
            length = len(pattern)
            j = length
            while j+length<=len(s) and s[j:j+length] == pattern:
                j += length
            if j == len(s):
                return True
            i += 1
        return False
s = Solution()
print(s.repeatedSubstringPattern("abcabcabcd"))
