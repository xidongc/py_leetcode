class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        adict = []
        bdict = []
        for i in range(len(s)):
            if s[i] not in adict:
                adict[s[i]] = t[i]
            if t[i] not in bdict:
                bdict[t[i]] = s[i]
            if adict[s[i]] != t[i] or bdict[t[i]] != s[i]:
                return False
        return True