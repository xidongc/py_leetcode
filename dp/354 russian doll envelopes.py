# 300 longest increasing subsequence
# e =[[5,4],[6,4],[6,7],[2,3]]
# e.sort(key=lambda x: (x[0], -x[1]))
# [[2, 3], [5, 4], [6, 7], [6, 4]]
# Since the width is increasing, we only need to consider height.
# [3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        res = [0] * len(envelopes)
        size = 0
        for envelop in envelopes:
            i,j = 0,size
            while i != j:
                m = (i + j) // 2
                if envelop[1] > res[m]:
                    i = m + 1
                else:
                    j = m
            res[i] = envelop[1]
            size = max(size, i + 1)
        return size
s = Solution()
s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])

