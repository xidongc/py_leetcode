class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        height = len(triangle)
        d = [[float("inf") for _ in range(k+1)] for k in range(height)]
        d[0][0] = triangle[0][0]
        dp = [triangle[0][0] for _ in range(height)]
        for i in range(1, height):
            for t in range(i+1):
                if t == 0:
                    d[i][t] = d[i-1][t] + triangle[i][t]
                elif t == i:
                    d[i][t] = d[i-1][t-1] + triangle[i][t]
                else:
                    d[i][t] = min(d[i-1][t-1], d[i-1][t]) + triangle[i][t]
            dp[i] = min(d[i])
        return dp[height-1]

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(s.minimumTotal(triangle))