# 354, https://leetcode.com/problems/russian-doll-envelopes/description/

# Sol-1 normal dp with time complexity: O(n^2), LTE
# no optimization


class Solution(object):

    def maxEnvelopes(self, envelopes):

        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        if not envelopes or len(envelopes) == 0:
            return 0

        # dp with time complexity: O(n^2)

        # sort envelopes
        envelopes.sort(key=lambda x:(x[0], x[1]))

        dp = [1 for _ in range(len(envelopes))]

        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# dp with optimization based on 300) longest increasing sub-sequence
# time complexity: O(nlgn), Accepted, by huijiang
# good explanation: https://leetcode.com/problems/russian-doll-envelopes/discuss/82751/
# O(Nlog(N))-python-solution-explained

# e =[[5,4],[6,4],[6,7],[2,3]]
# e.sort(key=lambda x: (x[0], -x[1]))
# [[2, 3], [5, 4], [6, 7], [6, 4]]
# Since the width is increasing, we only need to consider height.
# [3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3]
# when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]
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
print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))

