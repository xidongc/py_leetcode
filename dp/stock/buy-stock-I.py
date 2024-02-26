#一次买卖
class Solution:
    def maxProfit(self, prices):
        maxRes = 0
        maxTmp = 0
        for i in range(1,len(prices)):
            maxTmp = max(0,  maxTmp + prices[i] - prices[i-1])
            maxRes = max(maxRes,maxTmp)
        return maxRes


class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0
        min_val, max_val = prices[0], 0
        for price in prices[1:]:
            max_val = max(max_val, price - min_val)
            min_val = min(min_val, price)
        return max_val
