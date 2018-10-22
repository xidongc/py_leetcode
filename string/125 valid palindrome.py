class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        tempStr = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                tempStr += char.lower()
        return tempStr == tempStr[::-1]
s = Solution()
print(s.isPalindrome("0P"))