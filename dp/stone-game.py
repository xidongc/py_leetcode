class Solution(object):

    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        if not piles:
            return False

        l = len(piles)
        half = sum(piles) / 2
        dp_arr = [[0 for _ in range(l)] for _ in range(l)]

        # init
        for i in range(l):
            dp_arr[i][i] = piles[i]

        for i in range(l - 1):
            dp_arr[i][i + 1] = max(piles[i], piles[i + 1])

        for i in range(l-3, -1, -1):
            for j in range(i+2, l):
                dp_arr[i][j] = max(piles[i] + min(dp_arr[i + 2][j], dp_arr[i + 1][j - 1]),
                                   piles[j] + min(dp_arr[i + 1][j - 1], dp_arr[i][j - 2]))

        return dp_arr[0][l - 1] > half

arr = [5,3,4,5]
s = Solution()
s.stoneGame(arr)
