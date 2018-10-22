import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = collections.defaultdict(int)
        tDict = collections.defaultdict(int)
        for char in s:
            sDict[char] += 1
        for char in t:
            if char not in sDict or tDict[char] >= sDict[char]:
                return False
            else:
                tDict[char] += 1
        return len(s) == len(t)
