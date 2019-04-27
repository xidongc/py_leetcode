class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set()
        j = 0
        length = 0

        for i in range(len(s)):
            while j < len(s):
                if s[j] not in hashset:
                    hashset.add(s[j])
                    j += 1
                else:
                    break
            length = max(length, j - i)
            hashset.remove(s[i])
        return length
