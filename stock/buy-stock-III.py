class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_1 = float("-inf")
        buy_2 = float("-inf")
        sale_1 = sale_2 = 0
        for price in prices:
            buy_1 = max(-price, buy_1)
            sale_1 = max(price+buy_1, sale_1)
            buy_2 = max(-price+sale_1, buy_2)
            sale_2 = max(price+buy_2, sale_2)
        return sale_2

prices = [3,3,5,0,0,3,1,4]
s = Solution()
print(s.maxProfit(prices))