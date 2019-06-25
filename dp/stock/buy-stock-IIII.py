class Solution:

    def quickSolve(self, prices):
        ret = 0
        tmp = prices[0]
        for price in prices[1:]:
            if price - tmp > 0:
                ret += price-tmp
            tmp = price
        return ret

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2:
            return 0
        else:
            if k > len(prices)/2:
                return self.quickSolve(prices)

            buy = [0]
            buy.extend([float("-inf")]*k)
            sale = [0]*(k+1)

            for price in prices:
                j = 1
                while j <= k:
                    buy[j] = max(-price+sale[j-1], buy[j])
                    sale[j] = max(price+buy[j], sale[j])
                    j += 1

        return sale[k]
