# 这里因为用hashmap找重复很复杂，就用list[ord]
import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        tmpLen = 0
        if len(p) > len(s):
            return res
        start = 0
        pList = [0] * 26
        for pChar in p:
            pList[ord(pChar) - ord('a')] += 1
        sList = [0] * 26
        for i in range(len(s)):
            tmpLen += 1
            sList[ord(s[i]) - ord('a')] += 1
            if tmpLen < len(p):
                continue
            else:
                if sList == pList:
                    res.append(i - len(p) + 1)
                sList[ord(s[i - len(p) + 1]) - ord('a')] -= 1
        return res

