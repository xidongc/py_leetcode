# # Get the ASCII number of a character
# number = ord(char)
#
# # Get the character given by an ASCII number
# char = chr(number)
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = [0] * 26
        for char in t:
            res[ord(char)-ord('a')] += 1
        for char in s:
            res[ord(char) - ord('a')] -= 1
        for i in range(26):
            if res[i]:
                return chr(i + ord('a'))
        return ''