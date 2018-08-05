class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = ret = tmp = 0
        if len(prices) < 2:
            return ret
        else:
            j = i+1
            while j < len(prices):
                if prices[j] - prices[i] > tmp:
                    tmp = prices[j] - prices[i]
                elif prices[j] - prices[i] < tmp:
                    i = j
                    ret += tmp
                    tmp = 0
                j += 1
                while j < len(prices) and prices[j] == prices[j-1]:
                    j += 1
            ret += tmp
        return ret

s = Solution()
prices = [1,2,3,4,5]
print(s.maxProfit(prices))