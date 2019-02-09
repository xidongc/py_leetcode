from collections import Counter


class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = list()
        size = len(s) - len(p) + 1
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)])
        if pCounter == sCounter:
            ret.append(0)

        for i in range(1, size):
            sCounter[s[i-1]] = sCounter.get(s[i-1], 1)-1
            if sCounter[s[i-1]] == 0:
                sCounter.pop(s[i-1])
            sCounter[s[len(p)+i-1]] = sCounter.get(s[len(p)+i-1], 0)+1
            if sCounter == pCounter:
                ret.append(i)
        return ret
