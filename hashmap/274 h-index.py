import collections
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        length = len(citations)
        countDict = collections.defaultdict(int)
        for i in range(length):
            if citations[i] >= length:
                countDict[length] += 1
            else:
                countDict[citations[i]] += 1
        count = 0
        for i in range(length,-1,-1):
            count += countDict[i]
            if count >= i:
                return i
        return 0
#  countDict 0:1 1:1 3:1 5:2
# 最多有length个数

s = Solution()
s.hIndex([0,1,3,5,6])