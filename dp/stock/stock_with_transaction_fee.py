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
# lmf
#贪心算法 好难理解，记了
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        res = 0
        curProfit = 0
        low,high = prices[0],prices[0]
        for i in range(1,len(prices)):
            low = min(low,prices[i])
            high = max(high,prices[i])
            curProfit = max(curProfit,prices[i]-low-fee)
            if high - prices[i] >= fee:
                res += curProfit
                curProfit = 0
                low = high = prices[i]
        return res + curProfit

# to help rabbit better understand
class Solution(object):
    def maxProfit(self, prices: List[int], fee: int) -> int:

        # corner case
        if len(prices) <= 1:
            return 0

        sell = 0
        not_sell = -prices[0]
        buy = -prices[0]
        not_buy = 0

        for price in prices[1:]:
            tmp2 = not_sell
            tmp1 = sell
            tmp4 = not_buy
            tmp3 = buy

            sell = max(tmp2, tmp3) + price - fee
            not_sell = max(tmp2, tmp3)
            buy = max(tmp1, tmp4) - price
            not_buy = max(tmp1, tmp4)

        return max(sell, not_buy)


s = Solution()
s.maxProfit([1,3,2,8,4,9],2)