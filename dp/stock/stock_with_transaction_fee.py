class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        s0 = [-100 for x in range(len(prices))]
        s1 = [-100 for x in range(len(prices))]

        s0[0] = 0
        s1[0] = -prices[0]

        for i, x in enumerate(prices[1:]):
            i += 1
            s1[i] = max(s0[i-1]-x, s1[i-1])
            s0[i] = max(s1[i-1]+x-fee, s0[i-1])

        return max(s0[len(prices)-1], s1[len(prices)-1])