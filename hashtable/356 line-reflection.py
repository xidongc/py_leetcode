class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return False
        # Cannot set to 0 at the first time, since the number can be negative
        minValue = points[0][0]
        maxValue = points[0][0]
        resSet = set()
        for p in points:
            minValue = min(minValue,p[0])
            maxValue = max(maxValue, p[0])
            resSet.add((p[0],p[1]))
        #
        line = minValue + maxValue

        for p in points:
            if  (line - p[0],p[1]) not in resSet:
                return False
        return True
s = Solution()
print(s.isReflected([[1,1],[1,1],[1,1]]))
