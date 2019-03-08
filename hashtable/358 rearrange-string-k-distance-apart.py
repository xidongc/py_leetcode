import collections
# collections.Counter(list)
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        countMap = collections.defaultdict(int)
        validMap = collections.defaultdict(int)
        res = ""
        for char in s:
            countMap[char] += 1
        for i in range(len(s)):
            candidateChar = self.findMaxPos(countMap,validMap, i)
            if candidateChar == '':
                return ""
            validMap[candidateChar] = i + k
            countMap[candidateChar] -= 1
            res += candidateChar
        return res
    def findMaxPos(self, countMap, validMap, curPos):
        candidateChar = ''
        maxCount = 0
        for char,count in countMap.items():
            if count > 0 and count > maxCount and curPos >= validMap[char]:
                maxCount = count
                candidateChar = char
        return candidateChar