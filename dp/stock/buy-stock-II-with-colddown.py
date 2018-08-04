class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        s0 = [-100 for _ in range(len(prices))]
        s1 = [-100 for _ in range(len(prices))]
        s2 = [-100 for _ in range(len(prices))]

        s0[0] = 0
        s1[0] = -prices[0]

        for i, x in enumerate(prices[1:]):
            i = i+1
            s0[i] = max(s2[i-1], s0[i-1])
            s1[i] = max(s0[i-1]-x, s1[i-1])
            s2[i] = s1[i-1]+x

        return max(s0[len(prices)-1], s2[len(prices)-1])