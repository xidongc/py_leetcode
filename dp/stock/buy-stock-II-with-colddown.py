class Solution(object):

    def maxProfit(self, prices):
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

            sell = max(tmp2, tmp3) + price
            not_sell = max(tmp2, tmp3)
            buy = tmp4 - price
            not_buy = max(tmp1, tmp4)

        return max(sell, not_buy)
