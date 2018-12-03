#一次买卖
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = ret = 0

        if len(prices) < 2:
            return ret
        else:
            j = i+1
            while j < len(prices):
                if prices[j] - prices[i] > ret:
                    ret = prices[j] - prices[i]
                if prices[j] < prices[i]:
                    i = j
                j += 1
                while j < len(prices) and prices[j] == prices[j-1]:
                    j += 1

        return ret
#     lmf
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxRes = 0
        maxTmp = 0
        for i in range(1,len(prices)):
            maxTmp = max(0,  maxTmp + prices[i] - prices[i-1])
            maxRes = max(maxRes,maxTmp)
        return maxRes

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))