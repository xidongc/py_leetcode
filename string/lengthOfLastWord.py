class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s.strip()
#         strip removes the space at both sides
        return len(s.split(' ')[-1])
# s.split() returns the list
        
