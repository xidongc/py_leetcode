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

# 递归超了memory
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         news = ''
#         for c in s:
#             if c.isalpha() or c.isdigit():
#                 news += c.lower()
#         def helper(s):
#             if len(s) < 2:
#                 return True
#             if s[0] != s[-1]:
#                 return False
#             return helper(s[1:-1])
#         return helper(news)